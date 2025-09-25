# Explain about conditional statement in python along with examples.


# Conditional Statement:- 
# A conditional statements are used to continue the flow of the code without inturpting anything in the code. 
# The conditions statments are used to say that if a condtion is X then use that conditon. If not x use an other statement
# or function.

# ex:- 

Weather = True

creator = ("Nischay" , "Sidhaard")
if Weather:
    print(f"Welcome to Weather app. Made by {creator}")
else:
    print(f"The weather app is offline today due to an error. Please contact {creator} .")

print("")

rain = False
sun = True
day = True
clouds = True

if sun and day and clouds:
    print("Today we have sun outside. That is awsome right. and also it looks like a day after many days. ")
elif rain:
    print("Today it is raining again. ")
