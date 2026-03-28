import turtle as t

# ---------- базовые настройки ----------
t.speed(0)
t.hideturtle()
t.colormode(255)   # чтобы удобно задавать RGB
t.penup()

# ---------- 1. Функция треугольника ----------

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

# ---------- 2. Квадрат из двух треугольников ----------

def draw_square(x, y, size, color1, color2, diag="main"):
    """
    Рисует квадрат с нижним левым углом в (x, y) и стороной size.
    diag = "main"  – диагональ из (x, y) в (x+size, y+size)
    diag = "anti"  – диагональ из (x+size, y) в (x, y+size)
    color1, color2 – цвета двух треугольников.
    """
    if diag == "main":
        # треугольник 1: нижний левый, нижний правый, верхний правый
        p1 = (x, y)
        p2 = (x + size, y)
        p3 = (x + size, y + size)
        # треугольник 2: нижний левый, верхний левый, верхний правый
        p4 = (x, y)
        p5 = (x, y + size)
        p6 = (x + size, y + size)
    else:
        # диагональ из (x+size, y) в (x, y+size)
        # треугольник 1: нижний левый, нижний правый, верхний левый
        p1 = (x, y)
        p2 = (x + size, y)
        p3 = (x, y + size)
        # треугольник 2: нижний правый, верхний левый, верхний правый
        p4 = (x + size, y)
        p5 = (x, y + size)
        p6 = (x + size, y + size)

    draw_triangle(p1, p2, p3, color1)
    draw_triangle(p4, p5, p6, color2)

# ---------- 3. Узор плитки ----------

# параметры сетки
N = 8          # количество квадратов по стороне (можно подправить под ваш рисунок)
SIZE = 40      # размер одного квадрата

# палитра (подберите оттенки под свою картинку)
light1 = (200, 230, 255)
light2 = (170, 210, 245)
mid1   = (120, 170, 220)
dark1  = (40,  80, 150)

# сдвинем рисунок влево-вниз, чтобы он был по центру
start_x = - (N * SIZE) // 2
start_y = - (N * SIZE) // 2

for i in range(N):
    for j in range(N):
        x = start_x + j * SIZE
        y = start_y + i * SIZE

        # логика цвета: тёмное "X" по диагоналям
        on_main_diag = (i == j)
        on_anti_diag = (i + j == N - 1)

        if on_main_diag and on_anti_diag:
            # центр (если N нечётное) – самый тёмный
            c1, c2 = dark1, dark1
        elif on_main_diag or on_anti_diag:
            # диагонали – более тёмные
            c1, c2 = dark1, mid1
        else:
            # фон – светлые оттенки
            # чуть разнообразим: чётные/нечётные клетки
            if (i + j) % 2 == 0:
                c1, c2 = light1, light2
            else:
                c1, c2 = light2, light1

        # все квадраты делаем с одной диагональю (как на рисунке)
        draw_square(x, y, SIZE, c1, c2, diag="main")

t.done()