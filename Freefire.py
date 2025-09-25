"""
freefire_mini.py
A minimal Free Fire-style battle-royale prototype using Pygame.

Controls:
 - WASD: move
 - Mouse: aim
 - Left click: shoot (auto fire while held, uses ammo)
 - R: reload
 - Space: sprint (consumes stamina)
 - ESC: quit / back to menu
 - H: debug - take damage (for quick testing)

Notes:
 - This is a small single-file prototype made for learning / expansion.
 - Replace art/shapes with sprites to improve visuals.
"""

import pygame
import sys
import random
import math
from collections import deque
from datetime import timedelta

pygame.init()
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Free Fire Mini — Pygame Prototype")
CLOCK = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK = (18,18,18)
GRAY = (130,130,130)
GREEN = (54,209,88)
RED = (229,57,53)
YELLOW = (255,202,40)
BLUE = (66,135,245)
ORANGE = (255,140,0)

# Fonts
FONT = pygame.font.SysFont("Arial", 18)
FONT_BIG = pygame.font.SysFont("Arial", 36, bold=True)

# Game constants
MAP_W, MAP_H = 2000, 2000  # large map
PLAYER_SPEED = 240  # pixels per second
BULLET_SPEED = 900
FIRE_RATE = 6.5  # bullets per second
MAG_SIZE = 30
RELOAD_TIME = 1.2
MAX_BOTS = 12
SAFEZONE_SHRINK_INTERVAL = 8_000  # ms between shrinks
SAFEZONE_SHRINK_AMOUNT = 0.78  # scale multiplier each shrink stage
SAFEZONE_DAMAGE = 8  # damage per second outside safezone
BOT_SPAWN_PADDING = 200

# Utility funcs
def vec_from_angle(angle_radians):
    return pygame.math.Vector2(math.cos(angle_radians), math.sin(angle_radians))

def clamp(x, a, b):
    return max(a, min(b, x))

# Camera
class Camera:
    def __init__(self, w, h):
        self.offset = pygame.Vector2(0,0)
        self.w, self.h = w, h
    def apply(self, pos):
        return pygame.Vector2(pos) - self.offset
    def update(self, target_pos):
        # center camera on target
        self.offset.x = clamp(target_pos.x - WIDTH/2, 0, MAP_W - WIDTH)
        self.offset.y = clamp(target_pos.y - HEIGHT/2, 0, MAP_H - HEIGHT)

# Entities
class Player:
    def __init__(self, x, y, color=(100,200,250)):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2(0,0)
        self.size = 18
        self.color = color
        self.health = 100
        self.armor = 0  # placeholder (no armor mechanics currently)
        self.speed = PLAYER_SPEED
        self.reload_timer = 0
        self.fire_cooldown = 0
        self.mag = MAG_SIZE
        self.reserve_ammo = 90
        self.kills = 0
        self.alive = True
        self.stamina = 100
        self.sprint = False
        self.name = "You"

    def update(self, dt, keys, mouse_pos, bullets, camera):
        if not self.alive: return
        move = pygame.math.Vector2(0,0)
        if keys[pygame.K_w]: move.y -= 1
        if keys[pygame.K_s]: move.y += 1
        if keys[pygame.K_a]: move.x -= 1
        if keys[pygame.K_d]: move.x += 1
        if move.length_squared() > 0:
            move = move.normalize()
        # sprint when holding space and has stamina
        self.sprint = keys[pygame.K_SPACE] and self.stamina > 6
        spd = self.speed * (1.6 if self.sprint else 1.0)
        self.pos += move * spd * dt
        # clamp to map
        self.pos.x = clamp(self.pos.x, 0, MAP_W)
        self.pos.y = clamp(self.pos.y, 0, MAP_H)

        # stamina regen/usage
        if self.sprint and move.length_squared()>0:
            self.stamina = max(0, self.stamina - 48*dt)
        else:
            self.stamina = clamp(self.stamina + 28*dt, 0, 100)

        # handle shooting cooldowns
        if self.fire_cooldown > 0:
            self.fire_cooldown -= dt
        if self.reload_timer > 0:
            self.reload_timer -= dt
            if self.reload_timer <= 0:
                # finish reload
                needed = MAG_SIZE - self.mag
                take = min(needed, self.reserve_ammo)
                self.mag += take
                self.reserve_ammo -= take

    def shoot(self, target_world_pos, bullets):
        if not self.alive: return
        if self.reload_timer > 0: return
        if self.fire_cooldown > 0: return
        if self.mag <= 0:
            # auto start reload
            self.reload_timer = RELOAD_TIME
            return
        # spawn bullet toward target
        dir = (pygame.Vector2(target_world_pos) - self.pos)
        if dir.length_squared() == 0:
            dir = pygame.Vector2(1,0)
        dir = dir.normalize()
        b = Bullet(self.pos.x + dir.x*20, self.pos.y + dir.y*20, dir*BULLET_SPEED, owner=self)
        bullets.append(b)
        self.mag -= 1
        self.fire_cooldown = 1.0 / FIRE_RATE

    def reload(self):
        if self.reload_timer > 0: return
        if self.mag >= MAG_SIZE: return
        if self.reserve_ammo <= 0: return
        self.reload_timer = RELOAD_TIME

    def draw(self, surface, camera):
        screen_pos = camera.apply(self.pos)
        # body
        pygame.draw.circle(surface, self.color, (int(screen_pos.x), int(screen_pos.y)), self.size)
        # direction indicator (toward mouse)
        mx, my = pygame.mouse.get_pos()
        world_mouse = pygame.Vector2(mx, my) + camera.offset
        dir = (world_mouse - self.pos)
        if dir.length_squared()>0:
            dir = dir.normalize()
            end = screen_pos + dir* (self.size+8)
            pygame.draw.line(surface, WHITE, screen_pos, end, 2)
        # name
        name_txt = FONT.render(self.name, True, WHITE)
        surface.blit(name_txt, (screen_pos.x - name_txt.get_width()/2, screen_pos.y - self.size - 18))

class Bot:
    def __init__(self, x, y, color=(220,120,120)):
        self.pos = pygame.math.Vector2(x,y)
        self.size = 16
        self.color = color
        self.health = 100
        self.speed = PLAYER_SPEED * 0.9
        self.state = "wander"  # wander, chase, flee
        self.target = None
        self.fire_cooldown = 0
        self.mag = MAG_SIZE
        self.alive = True
        self.name = "Bot"

    def update(self, dt, player, bullets, world_bullets):
        if not self.alive: return
        # simple perception: if player within 350 and line-of-sight (no obstacles here), chase
        to_player = player.pos - self.pos
        dist = to_player.length()
        if player.alive and dist < 420:
            # engage
            self.state = "chase"
            self.target = player
            # move toward player somewhat
            dir = to_player.normalize()
            self.pos += dir * self.speed * dt * (1.0 if dist>100 else 0.6)
            # shooting logic
            if dist < 480:
                # try to shoot occasionally
                if self.fire_cooldown <= 0 and self.mag>0:
                    # aim with small inaccuracy
                    angle = math.atan2(dir.y, dir.x)
                    spread = random.uniform(-0.15, 0.15)
                    final_dir = vec_from_angle(angle + spread)
                    b = Bullet(self.pos.x + final_dir.x*20, self.pos.y + final_dir.y*20, final_dir*BULLET_SPEED, owner=self)
                    world_bullets.append(b)
                    self.mag -= 1
                    self.fire_cooldown = 1.0 / (FIRE_RATE*0.8)
                if self.fire_cooldown > 0:
                    self.fire_cooldown -= dt
                if self.mag <= 0:
                    # simple reload (instant-ish)
                    self.mag = MAG_SIZE
        else:
            # wander
            self.state = "wander"
            if not hasattr(self, 'wander_target') or (self.wander_target - self.pos).length() < 12:
                tx = clamp(self.pos.x + random.uniform(-300,300), 0, MAP_W)
                ty = clamp(self.pos.y + random.uniform(-300,300), 0, MAP_H)
                self.wander_target = pygame.math.Vector2(tx, ty)
            dir = (self.wander_target - self.pos)
            if dir.length_squared()>0:
                dir = dir.normalize()
                self.pos += dir * self.speed * dt * 0.6

    def draw(self, surface, camera):
        if not self.alive: return
        screen_pos = camera.apply(self.pos)
        pygame.draw.circle(surface, self.color, (int(screen_pos.x), int(screen_pos.y)), self.size)
        name_txt = FONT.render(self.name, True, WHITE)
        surface.blit(name_txt, (screen_pos.x - name_txt.get_width()/2, screen_pos.y - self.size - 18))

class Bullet:
    def __init__(self, x, y, vel, owner):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2(vel)
        self.radius = 4
        self.owner = owner
        self.lifetime = 2.6  # seconds

    def update(self, dt):
        self.pos += self.vel * dt
        self.lifetime -= dt

    def draw(self, surface, camera):
        screen_pos = camera.apply(self.pos)
        pygame.draw.circle(surface, ORANGE, (int(screen_pos.x), int(screen_pos.y)), self.radius)

class Loot:
    def __init__(self, x, y, kind):
        self.pos = pygame.math.Vector2(x,y)
        self.kind = kind  # "med", "ammo"
        self.size = 10

    def draw(self, surface, camera):
        sp = camera.apply(self.pos)
        if self.kind == "med":
            pygame.draw.rect(surface, (200,40,60), (sp.x-10, sp.y-10, 20, 20), border_radius=4)
            txt = FONT.render("+HP", True, WHITE)
            surface.blit(txt, (sp.x-16, sp.y-34))
        elif self.kind == "ammo":
            pygame.draw.rect(surface, (30,30,30), (sp.x-10, sp.y-10, 20, 20), border_radius=4)
            txt = FONT.render("AM", True, WHITE)
            surface.blit(txt, (sp.x-14, sp.y-34))

# Game manager
class Game:
    def __init__(self):
        self.camera = Camera(MAP_W, MAP_H)
        self.player = Player(MAP_W/2, MAP_H/2)
        self.bots = []
        self.bullets = []
        self.world_bullets = []  # bullets fired by bots
        self.loot = []
        self.spawn_bots(MAX_BOTS)
        self.start_ticks = pygame.time.get_ticks()
        # safezone: center and radius
        self.safe_center = pygame.math.Vector2(MAP_W/2, MAP_H/2)
        self.safe_radius = min(MAP_W, MAP_H) * 0.45
        self.last_shrink = pygame.time.get_ticks()
        self.shrink_stage = 0
        self.game_over = False
        self.winner = None

    def spawn_bots(self, count):
        self.bots = []
        for i in range(count):
            x = random.uniform(BOT_SPAWN_PADDING, MAP_W-BOT_SPAWN_PADDING)
            y = random.uniform(BOT_SPAWN_PADDING, MAP_H-BOT_SPAWN_PADDING)
            b = Bot(x,y)
            b.name = f"Bot{i+1}"
            self.bots.append(b)

    def update(self, dt, keys, mouse, mouse_pressed):
        if self.game_over:
            return
        # Player update
        mx, my = mouse
        world_mouse = pygame.Vector2(mx, my) + self.camera.offset
        self.player.update(dt, keys, world_mouse, self.bullets, self.camera)

        # Shooting (auto while held)
        if mouse_pressed[0]:
            self.player.shoot(world_mouse, self.bullets)
        # Reload
        if keys[pygame.K_r]:
            self.player.reload()

        # Update bots
        for b in self.bots:
            b.update(dt, self.player, self.bullets, self.world_bullets)

        # Update bullets
        for bl in self.bullets[:]:
            bl.update(dt)
            # remove if lifetime or out of map
            if bl.lifetime <= 0 or not (0<=bl.pos.x<=MAP_W and 0<=bl.pos.y<=MAP_H):
                self.bullets.remove(bl)
                continue
            # collision with bots
            for bot in self.bots:
                if not bot.alive: continue
                if (bot.pos - bl.pos).length_squared() <= (bot.size+bl.radius)**2:
                    bot.health -= 40
                    try: self.bullets.remove(bl)
                    except: pass
                    if bot.health <= 0:
                        bot.alive = False
                        self.player.kills += 1
                        # drop loot
                        if random.random() < 0.75:
                            for _ in range(random.randint(1,2)):
                                kind = random.choice(["med","ammo"])
                                l = Loot(bot.pos.x + random.uniform(-20,20), bot.pos.y + random.uniform(-20,20), kind)
                                self.loot.append(l)
                    break

            # avoid hitting owner
        # bullets from bots hitting player
        for bl in self.world_bullets[:]:
            bl.update(dt)
            if bl.lifetime <= 0 or not (0<=bl.pos.x<=MAP_W and 0<=bl.pos.y<=MAP_H):
                self.world_bullets.remove(bl)
                continue
            if (self.player.pos - bl.pos).length_squared() <= (self.player.size+bl.radius)**2 and self.player.alive:
                # player hit
                self.player.health -= 22
                try: self.world_bullets.remove(bl)
                except: pass

        # bullets from player hitting bots handled above
        # collect loot
        for l in self.loot[:]:
            if (self.player.pos - l.pos).length_squared() <= (self.player.size + l.size)**2:
                if l.kind == "med":
                    self.player.health = clamp(self.player.health + 45, 0, 100)
                elif l.kind == "ammo":
                    self.player.reserve_ammo += 24
                self.loot.remove(l)

        # safezone shrink logic
        now = pygame.time.get_ticks()
        if now - self.last_shrink > SAFEZONE_SHRINK_INTERVAL and self.shrink_stage < 6:
            # shrink toward center
            # pick new center near current center slightly random
            self.safe_center += pygame.math.Vector2(random.uniform(-80,80), random.uniform(-80,80))
            self.safe_radius *= SAFEZONE_SHRINK_AMOUNT
            self.last_shrink = now
            self.shrink_stage += 1

        # apply damage if outside safezone
        dist_out = (self.player.pos - self.safe_center).length() - self.safe_radius
        if dist_out > 0 and self.player.alive:
            self.player.health -= SAFEZONE_DAMAGE * dt
        # bots also take damage outside
        for b in self.bots:
            if not b.alive: continue
            if (b.pos - self.safe_center).length() > self.safe_radius:
                b.health -= SAFEZONE_DAMAGE * dt
                if b.health <= 0:
                    b.alive = False

        # update camera to player
        self.camera.update(self.player.pos)

        # check death
        if self.player.health <= 0 and self.player.alive:
            self.player.alive = False
            self.game_over = True
            self.winner = "Bots"
        # check if all bots dead -> player wins
        if all(not b.alive for b in self.bots):
            self.game_over = True
            self.winner = "You"

    def draw_map(self, surface):
        # draw simple grid map background
        tile = 80
        # determine visible region in map coords
        left = int(self.camera.offset.x // tile * tile)
        top = int(self.camera.offset.y // tile * tile)
        cols = int(WIDTH / tile) + 3
        rows = int(HEIGHT / tile) + 3
        for i in range(cols):
            for j in range(rows):
                x = left + i*tile
                y = top + j*tile
                rect = pygame.Rect(x - self.camera.offset.x, y - self.camera.offset.y, tile-2, tile-2)
                shade = 34 + ((i+j)&1)*6
                pygame.draw.rect(surface, (shade, shade+8, shade-4), rect)

    def draw(self, surface):
        # world
        self.draw_map(surface)
        # safezone
        sc = self.camera.apply(self.safe_center)
        pygame.draw.circle(surface, (40,40,140), (int(sc.x), int(sc.y)), int(self.safe_radius), width=4)
        pygame.draw.circle(surface, (20,20,60,100), (int(sc.x), int(sc.y)), int(self.safe_radius), width=0)

        # loot
        for l in self.loot:
            l.draw(surface, self.camera)
        # bots
        for b in self.bots:
            b.draw(surface, self.camera)
        # player
        if self.player.alive:
            self.player.draw(surface, self.camera)
        # bullets
        for bl in self.bullets:
            bl.draw(surface, self.camera)
        for bl in self.world_bullets:
            bl.draw(surface, self.camera)

        # HUD (screen space)
        # top-left info
        hud_txt = FONT.render(f"HP: {int(self.player.health)}   Armor: {int(self.player.armor)}   Ammo: {self.player.mag}/{self.player.reserve_ammo}   Kills: {self.player.kills}", True, WHITE)
        surface.blit(hud_txt, (12,12))
        # mini-timer
        elapsed_ms = pygame.time.get_ticks() - self.start_ticks
        timer_txt = FONT.render(f"Time: {str(timedelta(milliseconds=elapsed_ms))[:-4]}", True, WHITE)
        surface.blit(timer_txt, (12, 34))
        # low-health flash
        if self.player.health < 35 and self.player.alive:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            alpha = int((1 - self.player.health/35) * 80)
            s.fill((255,20,20, alpha))
            surface.blit(s, (0,0))

        # draw minimap (small)
        minimap_w = 180
        minimap_h = 180
        mm_x = WIDTH - minimap_w - 12
        mm_y = 12
        pygame.draw.rect(surface, (18,18,18), (mm_x, mm_y, minimap_w, minimap_h))
        # draw safezone and players relative
        scale_x = minimap_w / MAP_W
        scale_y = minimap_h / MAP_H
        # safezone on mini
        rcx = mm_x + self.safe_center.x * scale_x
        rcy = mm_y + self.safe_center.y * scale_y
        rr = self.safe_radius * scale_x
        pygame.draw.circle(surface, (40,60,140), (int(rcx), int(rcy)), int(rr), width=2)
        # bots
        for b in self.bots:
            if not b.alive: continue
            bx = mm_x + b.pos.x * scale_x
            by = mm_y + b.pos.y * scale_y
            pygame.draw.circle(surface, RED, (int(bx), int(by)), 4)
        # player dot
        px = mm_x + self.player.pos.x * scale_x
        py = mm_y + self.player.pos.y * scale_y
        pygame.draw.circle(surface, GREEN, (int(px), int(py)), 5)

        # draw reload status if reloading
        if self.player.reload_timer > 0:
            pct = 1 - self.player.reload_timer / RELOAD_TIME
            pygame.draw.rect(surface, (0,0,0), (WIDTH/2 - 100, HEIGHT - 48, 200, 10), border_radius=5)
            pygame.draw.rect(surface, BLUE, (WIDTH/2 - 100, HEIGHT - 48, 200*pct, 10), border_radius=5)

        # center crosshair
        pygame.draw.circle(surface, WHITE, (WIDTH//2, HEIGHT//2), 4, 1)

    def restart(self):
        self.__init__()  # re-init everything

# Simple menu to launch the game
def main_menu():
    menu_running = True
    title = FONT_BIG.render("Free Fire Mini — Pygame Prototype", True, WHITE)
    subtitle = FONT.render("Press ENTER to start — ESC to quit — Click to aim/shoot", True, GRAY)
    while menu_running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    menu_running = False
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
        SCREEN.fill(DARK)
        SCREEN.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
        SCREEN.blit(subtitle, subtitle.get_rect(center=(WIDTH//2, HEIGHT//2 + 8)))
        pygame.display.flip()
        CLOCK.tick(FPS)

def game_loop():
    game = Game()
    mouse_held = False
    # For continuous shooting: we will track mouse button
    running = True
    while running:
        dt = CLOCK.tick(FPS) / 1000.0
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
                if ev.key == pygame.K_r:
                    game.player.reload()
                if ev.key == pygame.K_h:
                    game.player.health -= 20
                if ev.key == pygame.K_F5:
                    game.restart()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    mouse_held = True
            if ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_held = False

        # update
        game.update(dt, keys, mouse, (mouse_pressed[0] or mouse_held, False, False))
        # draw
        SCREEN.fill((12,12,16))
        game.draw(SCREEN)

        # draw overlay messages if game over
        if game.game_over:
            txt = FONT_BIG.render("YOU WIN!" if game.winner=="You" else "YOU DIED", True, WHITE)
            sub = FONT.render("Press R to restart or ESC to exit to menu", True, GRAY)
            SCREEN.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
            SCREEN.blit(sub, sub.get_rect(center=(WIDTH//2, HEIGHT//2 + 28)))
            # allow restart
            # if player presses R -> restart
            if keys[pygame.K_r]:
                game.restart()

        pygame.display.flip()

# Run
if __name__ == "__main__":
    main_menu()
    while True:
        game_loop()
        # after exiting game loop, go back to menu
        main_menu()
