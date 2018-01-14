import turtle

george = turtle.Turtle()
george.width(5)
george.hideturtle()
george.speed(0)

# Draw Maze
def drawMazeSection(t):
  for i in range(2):
    t.pendown()
    t.forward(170)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(170)
    t.right(90)
    t.forward(100)
    t.right(90)
  t.right(90)
  t.forward(50)
  t.left(90)
  t.forward(30)
  t.penup()
  t.forward(40)
  t.pendown()
  t.forward(240)
  t.penup()
  t.forward(40)
  t.pendown()
  t.forward(30)

# Maze Color
colors = ["red", "blue", "Yellow"]
y = 160

# Maze
for color in colors:
  george.color(color)
  george.penup()
  george.goto(-190, y)
  george.pendown()
  drawMazeSection(george)
  y = y - 110
