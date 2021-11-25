# 컴퓨팅과데이터처리 12주차 과제
# 2021024202 김관우

import turtle as t


def draw_func(func: str, x_minimum, x_maximum, space=0.1):
    x = x_minimum
    exec(func, None, locals())
    t.up()
    t.goto(x, locals()['y'])
    t.down()
    while x <= x_maximum:
        x += space
        exec(func, None, locals())
        t.goto(x, locals()['y'])


def draw_line(dest: tuple, src: tuple):
    t.up()
    t.goto(src[0], src[1])
    t.down()
    t.goto(dest[0], dest[1])


X_MIN = -5
X_MAX = 5
Y_MIN = -5
Y_MAX = 5
SPACE = 0.1

functions: list[str] = ["y=x*x", "y=abs(x)", "y=0.5*x+1"]

t.setworldcoordinates(X_MIN, Y_MIN, X_MAX, Y_MAX)
t.pensize(2)

# Drawing axis
draw_line((X_MIN, 0), (X_MAX, 0))
draw_line((0, Y_MIN), (0, Y_MAX))

t.color("green")

for i in functions:
    draw_func(i, X_MIN, X_MAX, SPACE)

input()
