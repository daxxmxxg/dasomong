import turtle

map = turtle.Turtle()
map.width(5)
map.hideturtle()
map.speed(0)

def draw_Map_of_Maze(t):
    for i in range(3):
        t.pendown()
        t.forward(150)
        t.penup()
        t.forward(30)
        t.pendown()
        t.forward(150)
        t.right(80)
        t.forward(100)
        t.right(80)
  t.right(80)
  t.forward(50)
  t.left(80)
  t.forward(30)
  t.penup()
  t.forward(40)
  t.pendown()
  t.forward(200)
  t.penup()
  t.forward(40)
  t.pendown()
  t.forward(30)

colors = ["red", "blue", "yellow"]
y = 150

for color in colors:
    map.color(color)
    map.penup()
    map.goto(-180,y)
    draw_Map_of_Maze(map)
    y = y - 100
