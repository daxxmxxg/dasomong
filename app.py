import turtle as t
import maze

def Right():
    t.setheading(0)
    t.forward(20)

def Left():
    t.setheading(180)
    t.forward(20)

def Up():
    t.setheading(90)
    t.forward(20)

def Down():
    t.setheading(270)
    t.forward(20)

def Map():
    

# Main Start

name = input("Please Typing your name: ")

t.shape("turtle")
t.speed(0)
t.onkeypress(Right, "Right")
t.onkeypress(Left, "Left")
t.onkeypress(Up, "Up")
t.onkeypress(Down, "Down")
t.listen()
    
