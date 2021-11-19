# 컴퓨팅과데이터처리 12주차 과제
# 2021024202 김관우

import turtle as t


def draw_func(func: str, x_minimum):
    x = x_min
    exec(func, None, locals())
    t.up()
    t.goto(x, locals()['y'])
    t.down()
    while x <= x_max:
        x += space
        exec(func, None, locals())
        t.goto(x, locals()['y'])


def draw_line(dest: tuple, src: tuple):
    t.up()
    t.goto(src[0], src[1])
    t.down()
    t.goto(dest[0], dest[1])


x_min = -5
x_max = 5
y_min = -5
y_max = 5

space = 0.1

functions: list[str] = ["y=x*x", "y=abs(x)", "y=0.5*x+1"]

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.pensize(2)

# Drawing axis
draw_line((x_min, 0), (x_max, 0))
draw_line((0, y_min), (0, y_max))

t.color("green")

for i in functions:
    draw_func(i, x_min)

input()
