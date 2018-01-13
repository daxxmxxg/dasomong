import turtle as t

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

t.shape("turtle")
t.speed(0)
t.onkeypress(Right, "Right")
t.listen()
    
