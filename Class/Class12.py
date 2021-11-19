import turtle

t = turtle.Turtle()
turtle.colormode(255)
t.speed(20)


def f(n):
    c = 255 / n
    rgb = [0, 0, 0]
    for i in range(n):
        rgb[0] = 0
        rgb[2] = 255
        for j in range(n):
            t.pencolor(int(rgb[0]), int(rgb[1]), int(rgb[2]))
            t.pensize(2)
            t.fd(15 * n)
            t.rt(180 - ((n - 2) * 180 / n))
            rgb[0] += c
            rgb[2] -= c
        t.left(180 - ((n - 2) * 180 / n))
        rgb[1] += c


for i in range(3, 11):
    f(i)
input()