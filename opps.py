from turtle import Turtle,Screen
timmy=Turtle()

timmy.shape("turtle")
timmy.color("red")
for i in range(0,4):

    timmy.forward(200)
    timmy.right(90)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
