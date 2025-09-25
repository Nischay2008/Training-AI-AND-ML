# mini_chrome.py
# A tiny Chromium-based browser: tabs, URL bar, back/forward/reload/home.

import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QLineEdit,
    QTabWidget, QWidget, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


HOME_URL = "https://www.google.com"


class WebView(QWebEngineView):
    """Custom view so target=_blank links open in a new tab."""
    def __init__(self, parent=None, on_new_tab=None):
        super().__init__(parent)
        self.on_new_tab = on_new_tab

    def createWindow(self, _type: QWebEnginePage.WebWindowType):
        # When a site tries to open a new window, create a new tab instead.
        if self.on_new_tab is not None:
            return self.on_new_tab()
        return super().createWindow(_type)


class MiniChrome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Chrome")
        self.resize(1100, 720)

        # Tabs
        self.tabs = QTabWidget(movable=True, tabsClosable=True, documentMode=True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.on_tab_changed)

        # Address bar
        self.urlbar = QLineEdit()
        self.urlbar.setPlaceholderText("Search or enter address")
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # Toolbar
        nav = QToolBar("Navigation")
        nav.setIconSize(nav.iconSize())  # default size
        self.addToolBar(nav)

        self.act_back = QAction("◀", self)
        self.act_back.setStatusTip("Back")
        self.act_back.triggered.connect(lambda: self.current_view().back())
        nav.addAction(self.act_back)

        self.act_forward = QAction("▶", self)
        self.act_forward.setStatusTip("Forward")
        self.act_forward.triggered.connect(lambda: self.current_view().forward())
        nav.addAction(self.act_forward)

        self.act_reload = QAction("⟳", self)
        self.act_reload.setStatusTip("Reload")
        self.act_reload.triggered.connect(lambda: self.current_view().reload())
        nav.addAction(self.act_reload)

        self.act_home = QAction("🏠", self)
        self.act_home.setStatusTip("Home")
        self.act_home.triggered.connect(self.navigate_home)
        nav.addAction(self.act_home)

        nav.addSeparator()
        nav.addWidget(self.urlbar)

        self.act_new_tab = QAction("＋", self)
        self.act_new_tab.setStatusTip("New Tab")
        self.act_new_tab.triggered.connect(lambda: self.add_tab(HOME_URL, "New Tab"))
        nav.addAction(self.act_new_tab)

        # Central widget
        wrapper = QWidget()
        layout = QVBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tabs)
        self.setCentralWidget(wrapper)

        # Shortcuts
        self.act_back.setShortcut("Alt+Left")
        self.act_forward.setShortcut("Alt+Right")
        self.act_reload.setShortcut("Ctrl+R")
        self.act_new_tab.setShortcut("Ctrl+T")

        # Start with one tab
        self.add_tab(HOME_URL, "Home")

    # ---- Tabs & views ----
    def current_view(self) -> QWebEngineView:
        return self.tabs.currentWidget()

    def add_tab(self, url: str, label: str):
        view = WebView(on_new_tab=self.create_blank_tab)
        view.setUrl(self._normalize_url(url))
        view.urlChanged.connect(self.update_urlbar)
        view.loadFinished.connect(lambda ok, v=view: self.tab_loaded(ok, v))

        idx = self.tabs.addTab(view, label)
        self.tabs.setCurrentIndex(idx)
        self.tabs.setTabIcon(idx, QIcon())  # placeholder
        view.setFocus()
        return view

    def create_blank_tab(self):
        """Used by target=_blank; returns the view so WebEngine can render into it."""
        view = WebView(on_new_tab=self.create_blank_tab)
        view.urlChanged.connect(self.update_urlbar)
        view.loadFinished.connect(lambda ok, v=view: self.tab_loaded(ok, v))
        idx = self.tabs.addTab(view, "New Tab")
        self.tabs.setCurrentIndex(idx)
        return view

    def close_tab(self, index: int):
        if self.tabs.count() == 1:
            if QMessageBox.question(self, "Quit", "Close the last tab and exit?") == QMessageBox.Yes:
                self.close()
            return
        widget = self.tabs.widget(index)
        self.tabs.removeTab(index)
        widget.deleteLater()

    def on_tab_changed(self, index: int):
        view = self.tabs.widget(index)
        if isinstance(view, QWebEngineView):
            self.update_urlbar(view.url())

    def tab_loaded(self, ok: bool, view: QWebEngineView):
        idx = self.tabs.indexOf(view)
        title = view.title() if ok else "Load Failed"
        self.tabs.setTabText(idx, title)

    # ---- Navigation ----
    def navigate_home(self):
        self.current_view().setUrl(QUrl(HOME_URL))

    def navigate_to_url(self):
        text = self.urlbar.text().strip()
        if not text:
            return
        url = self._normalize_url(text)
        self.current_view().setUrl(url)

    def update_urlbar(self, qurl: QUrl):
        if self.current_view() and qurl == self.current_view().url():
            self.urlbar.blockSignals(True)
            self.urlbar.setText(qurl.toString())
            self.urlbar.setCursorPosition(0)
            self.urlbar.blockSignals(False)

    # ---- Helpers ----
    def _normalize_url(self, text: str) -> QUrl:
        """
        Accepts:
          - raw domain (example.com)
          - full url (https://example.com)
          - search terms (“cats and dogs”)
        """
        # If it looks like a URL without scheme, add https
        if "." in text and " " not in text and not text.startswith(("http://", "https://")):
            text = "https://" + text
        # If it's not a URL, treat as a search query
        if " " in text or not text.startswith(("http://", "https://")) and "." not in text:
            from urllib.parse import quote_plus
            text = f"https://www.google.com/search?q={quote_plus(text)}"
        return QUrl(text)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Mini Chrome")
    window = MiniChrome()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
