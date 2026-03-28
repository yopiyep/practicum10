import turtle
import random

turtle.tracer(0)
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#0b1026")  # тёмное ночное небо
screen.title("Ночной городской пейзаж")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_rectangle(x, y, width, height, color):
    t.color(color)
    move_to(x, y)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.right(0)


def draw_triangle_roof(x, y, width, height, color):
    t.color(color)
    move_to(x, y)
    t.begin_fill()
    t.forward(width)
    t.goto(x + width / 2, y + height)
    t.goto(x, y)
    t.end_fill()


def draw_window(x, y, w=8, h=12, color="#ffd166"):
    draw_rectangle(x, y, w, h, color)


def draw_stars(count):
    t.color("white")
    for _ in range(count):
        x = random.randint(-480, 480)
        y = random.randint(50, 330)
        size = random.randint(1, 3)
        move_to(x, y)
        t.dot(size)


def draw_moon(x, y, r):
    t.color("#f6c667")
    move_to(x, y - r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    t.color("#0b1026")
    move_to(x + r * 0.4, y - r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def draw_building(x, ground_y, width, height, color):
    draw_rectangle(x, ground_y, width, height, color)

    roof_type = random.choice(["flat", "triangle", "tower"])

    if roof_type == "triangle":
        roof_h = random.randint(20, 50)
        draw_triangle_roof(x, ground_y + height, width, roof_h, color)

    elif roof_type == "tower":
        tower_w = width * 0.25
        tower_h = random.randint(20, 60)
        tower_x = x + random.randint(0, int(width - tower_w))
        draw_rectangle(tower_x, ground_y + height, tower_w, tower_h, color)

    draw_windows(x, ground_y, width, height)


def draw_windows(x, y, width, height):
    window_w = 8
    window_h = 12
    step_x = 18
    step_y = 22

    start_x = x + 8
    start_y = y + 8

    for wx in range(int(start_x), int(x + width - window_w - 5), step_x):
        for wy in range(int(start_y), int(y + height - window_h - 5), step_y):
            if random.random() < 0.45:
                color = random.choice(["#ffd166", "#ffe082", "#ffef9f"])
                draw_window(wx, wy, window_w, window_h, color)


def draw_city():
    ground_y = -330
    x = -500

    while x < 500:
        width = random.randint(50, 100)
        height = random.randint(120, 350)
        color = random.choice(["#1f1633", "#24183d", "#2d204a", "#362657"])
        draw_building(x, ground_y, width, height, color)

        x += random.randint(40, 80)

draw_stars(180)
draw_moon(-120, 240, 35)
draw_city()

turtle.done()