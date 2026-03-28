import turtle


screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(900, 700)
screen.title("Орнамент")
turtle.tracer(0)

t = turtle.Turtle()
t.width(2)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_petal(size, color):
    t.color("black", color)
    t.begin_fill()
    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
    t.end_fill()


def draw_flower(x, y, size):
    move(x, y)
    for _ in range(6):
        draw_petal(size, "pink")
        t.left(60)

    move(x, y)
    t.color("black", "yellow")
    t.begin_fill()
    t.circle(size // 3)
    t.end_fill()


def draw_leaf(x, y, size):
    move(x, y)
    t.setheading(45)
    t.color("black", "lightgreen")
    t.begin_fill()
    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
    t.end_fill()


def draw_ornament():
    for x in range(-300, 301, 150):
        draw_flower(x, 0, 40)

    for x in range(-225, 226, 150):
        draw_leaf(x, 120, 30)
        draw_leaf(x + 40, 120, 30)

    for x in range(-225, 226, 150):
        draw_leaf(x, -120, 30)
        draw_leaf(x + 40, -120, 30)


draw_ornament()

turtle.done()
