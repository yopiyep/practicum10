import turtle as t


t.speed(0)
t.hideturtle()
t.colormode(255)   
t.penup()


def draw_triangle(p1, p2, p3, color):
    """
    p1, p2, p3 – кортежи (x, y)
    color – цвет (имя или (r, g, b))
    """
    t.fillcolor(color)
    t.pencolor(color)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()
    t.penup()


def draw_square(x, y, size, color1, color2, diag="main"):
    if diag == "main":
        p1 = (x, y)
        p2 = (x + size, y)
        p3 = (x + size, y + size)
        p4 = (x, y)
        p5 = (x, y + size)
        p6 = (x + size, y + size)
    else:
        p1 = (x, y)
        p2 = (x + size, y)
        p3 = (x, y + size)
        p4 = (x + size, y)
        p5 = (x, y + size)
        p6 = (x + size, y + size)

    draw_triangle(p1, p2, p3, color1)
    draw_triangle(p4, p5, p6, color2)


N = 8          
SIZE = 40      

light1 = (200, 230, 255)
light2 = (170, 210, 245)
mid1   = (120, 170, 220)
dark1  = (40,  80, 150)

start_x = - (N * SIZE) // 2
start_y = - (N * SIZE) // 2

for i in range(N):
    for j in range(N):
        x = start_x + j * SIZE
        y = start_y + i * SIZE

        on_main_diag = (i == j)
        on_anti_diag = (i + j == N - 1)

        if on_main_diag and on_anti_diag:
            c1, c2 = dark1, dark1
        elif on_main_diag or on_anti_diag:
            c1, c2 = dark1, mid1
        else:
            if (i + j) % 2 == 0:
                c1, c2 = light1, light2
            else:
                c1, c2 = light2, light1

        # все квадраты делаем с одной диагональю (как на рисунке)
        draw_square(x, y, SIZE, c1, c2, diag="main")

t.done()
