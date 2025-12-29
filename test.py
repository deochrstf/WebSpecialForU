import turtle

# Setup layar
screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#fde6f0")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

IKAT_X, IKAT_Y = 0, 40   # titik kumpul tangkai

# ---------------- FUNGSI ----------------
def petal(radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(x, y, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color("black", color)
    t.begin_fill()
    for _ in range(8):       # kelopak mekar
        petal(50, 80)
        t.left(45)
    t.end_fill()

    # tengah bunga
    t.penup()
    t.goto(x, y - 12)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(14)
    t.end_fill()

def draw_stem_to_center(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.width(4)
    t.goto(IKAT_X, IKAT_Y)
    t.width(1)

# ---------------- POSISI BUNGA ----------------
flowers = [
    (-150, 180, "pink"),
    (-70, 220, "lightblue"),
    (70, 220, "violet"),
    (150, 180, "orange"),
    (0, 150, "red"),
]

# 🔹 TANGKAI DI BELAKANG
for x, y, _ in flowers:
    draw_stem_to_center(x, y - 20)

# 🔹 BUNGA DI DEPAN
for x, y, c in flowers:
    draw_flower(x, y, c)

# Teks (opsional)
t.penup()
t.goto(0, -200)
t.color("deeppink")
t.write(
    "It's Made For Youu 💐",
    align="center",
    font=("Comic Sans MS", 32, "bold")
)

turtle.done()