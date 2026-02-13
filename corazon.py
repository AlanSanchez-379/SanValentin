import math
import random
import time
from turtle import *

def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

def _small_heart_points(size, detail=40):
    pts = []
    for i in range(detail + 1):
        t = i * 2 * math.pi / detail
        x = 16 * math.sin(t) ** 3 * size
        y = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * size / 13
        pts.append((x, y))
    return pts

def draw_small_heart(x, y, size=6, color_fill="pink"):
    penup()
    goto(x, y)
    pendown()
    color(color_fill)
    begin_fill()
    pts = _small_heart_points(size, detail=30)
    for px, py in pts:
        goto(x + px, y + py)
    end_fill()
    penup()

def draw_lily(x, y, size=12, petal_color="#d6b3e6", center_color="#f7e6ff"):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    color(petal_color)
    begin_fill()
    petals = 6
    for i in range(petals):
        setheading(i * (360 / petals) - 30)
        forward(size * 0.2)
        circle(size, 60)
        left(120)
        circle(size, 60)
        penup()
        goto(x, y)
        pendown()
    end_fill()
    penup()
    goto(x, y - size * 0.15)
    color(center_color)
    pendown()
    begin_fill()
    circle(size * 0.18)
    end_fill()
    penup()

def draw_gerbera(x, y, size=10, petal_color="#f3c1db", center_color="#fce7f2"):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    petals = 18
    for i in range(petals):
        angle = i * (360 / petals)
        setheading(angle)
        penup()
        forward(size * 0.15)
        pendown()
        color(petal_color)
        begin_fill()
        circle(size * 0.45, 90)
        left(90)
        circle(size * 0.45, 90)
        end_fill()
        penup()
        goto(x, y)
        pendown()
    penup()
    goto(x, y - size * 0.05)
    color(center_color)
    pendown()
    begin_fill()
    circle(size * 0.22)
    end_fill()
    penup()

def draw_heart(scale=12, steps=800, bg="#0b0b0b", color_fill="#ff3b3b", message=None):
    setup(width=900, height=750)
    bgcolor(bg)
    tracer(1.8, 25)  
    speed(1)
    hideturtle()
    penup()

    t0 = 0.0
    x0 = heart_x(t0) * scale
    y0 = heart_y(t0) * scale
    goto(x0, y0)
    pendown()

    color(color_fill)
    begin_fill()
    for i in range(steps + 1):
        t = i * (2 * math.pi) / steps
        x = heart_x(t) * scale
        y = heart_y(t) * scale
        goto(x, y)
        if i % 120 == 0:
            update()
    end_fill()
    update()

    colors = ["#ff8fa3", "#ff5c8a", "#ffd1dc", "#ff3b3b"]
    for _ in range(12):
        t = random.random() * 2 * math.pi
        r = random.uniform(0.18, 0.78)
        x = heart_x(t) * scale * r
        y = heart_y(t) * scale * r
        draw_small_heart(x, y, size=random.uniform(scale * 0.12, scale * 0.45), color_fill=random.choice(colors))
        update()
        time.sleep(0.05)
    update()

    if message:
        penup()
        goto(0, scale * 0.5)
        color("white")
        font_size = max(14, int(scale * 1.2))
        write(message, align="center", font=("Arial", font_size, "bold"))
    update()

    flower_positions = [
        (-scale * 18, scale * 6),
        (scale * 18, scale * 6),
        (-scale * 26, -scale * 8),
        (scale * 26, -scale * 10),
        (-scale * 8, -scale * 22),
        (scale * 8, -scale * 22),
    ]
    lily_colors = ["#c39bd3", "#d6b3e6", "#e8daef"]
    gerbera_colors = ["#f3c1db", "#ffd6e8", "#f7cfe6"]
    for i, (fx, fy) in enumerate(flower_positions):
        if i % 2 == 0:
            draw_lily(fx, fy, size=scale * 0.9, petal_color=random.choice(lily_colors))
        else:
            draw_gerbera(fx, fy, size=scale * 0.9, petal_color=random.choice(gerbera_colors))
        update()
        time.sleep(0.35)

    penup()
    goto(0, - (scale * 22))
    showturtle()
    tracer(1, 10)
    done()

if __name__ == "__main__":
    mensaje = "¿Quieres ser mi San Valentín?"
    draw_heart(scale=14, steps=1200, message=mensaje)
  
