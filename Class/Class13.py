# 컴퓨팅과데이터처리 13주차 과제
# 2021024202 김관우

import random
import turtle as t


def turn_right():
    t.setheading(0)
    t.forward(10)


def turn_up():
    t.setheading(90)
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


def turn_down():
    t.setheading(270)
    t.forward(10)


def play():
    global score
    global speed
    t.forward(10)

    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(speed)

    if t.xcor() > 350 or t.xcor() < -350:
        t.left(180)
    if t.ycor() > 350 or t.ycor() < -350:
        t.left(180)
    if t.distance(ts) < 15:
        score += 1
        speed += 2
        t.write(score)
        repaint_score()

        stat_x = random.randint(-150, 150)
        stat_y = random.randint(-150, 150)
        ts.goto(stat_x, stat_y)

    if t.distance(te) > 15:
        t.ontimer(play, 100)
    else:
        t.write("Game Over", False, "center", ("", 20))


def start():
    global playing
    if not playing:
        playing = True
        t.clear()
        play()


def repaint_score():
    tc.clear()
    tc.speed(0)
    tc.write("Score : " + str(score), False, "center", ("", 20, 'normal'))


score = 0
speed = 1
playing = False

t.setup(800, 800)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

tc = t.Turtle()
tc.hideturtle()
tc.penup()
tc.goto(-300, 350)
tc.write("Score : " + str(score), False, "center", ("", 20, 'normal'))

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

t.write("Press Space to start game", False, "center", ("", 20 ))

t.onkeypress(start, "space")

t.listen()
t.mainloop()
