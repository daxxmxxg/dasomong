import turtle
import maze
# key

def Right():
    user.setheading(0)
    user.forward(20)

def Left():
    user.setheading(180)
    user.forward(20)

def Up():
    user.setheading(90)
    user.forward(20)

def Down():
    user.setheading(270)
    user.forward(20)
# user character
user = turtle.Turtle()
user.shape("turtle")
user.color("lime")
user.width(5)

user.penup()
user.right(90)
user.forward(180)
user.left(180)
user.pendown()
user.forward(40)
user.right(90)

# user move(?)
turtle.onkeypress(Right, "Right")
turtle.onkeypress(Left, "Left")
turtle.onkeypress(Up, "Up")
turtle.onkeypress(Down, "Down")
turtle.listen()
    
