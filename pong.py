import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)   
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle. Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddle_a_up(event):
    y = paddle_a.ycor()
    if y <= 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down(event):
    y = paddle_a.ycor()
    if y >= -230:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up(event):
    y = paddle_b.ycor()
    if y <= 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down(event):

    y = paddle_b.ycor()
    if y >= -230:
        y -= 20
        paddle_b.sety(y)
    

# Keyboard binding
turtle.getcanvas().bind('<Up>', paddle_b_up)
turtle.getcanvas().bind('<Down>', paddle_b_down)
turtle.getcanvas().bind('<w>', paddle_a_up)
turtle.getcanvas().bind('<s>', paddle_a_down)


wn.listen()
# wn.onkey(paddle_a_up, "w")
# wn.onkey(paddle_a_down, "s")
# wn.onkey(paddle_b_up, "Up")
# wn.onkey(paddle_b_down, "Down")



# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1