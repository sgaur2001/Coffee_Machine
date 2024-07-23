import turtle as t
import random

timmy = t.Turtle()

dirction = [0, 90, 180, 270]

for i in range(10):
    timmy.color("red")
    timmy.forward(30)
    timmy.setheading(random.choice(dirction))
creen=Screen()
reen.exitonclick()