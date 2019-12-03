import turtle
import winsound

global a,b
a=0
b=0

wn=turtle.Screen()
wn.title('Classic pong game')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0,0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.dx=.2
ball.dy=.2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: {}  | Player B: {}'.format(a,b),align='center',font=('Courier',18,'normal'))

#Functions
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#driver function
while True:
	wn.update()

	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	if ball.ycor()>290:
		ball.dy*=-1
		ball.sety(290)
		winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

	if ball.ycor()<-290:
		ball.dy*=-1
		ball.sety(-290)
		winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

	if ball.xcor()>390:
		a+=1
		pen.clear()
		pen.write('Player A: {}  | Player B: {}'.format(a,b),align='center',font=('Courier',18,'normal'))
		ball.goto(0,0)
		ball.dx=.3
		ball.dy=.3
		ball.dx*=-1

	if ball.xcor()<-390:
		b+=1
		pen.clear()
		pen.write('Player A: {}  | Player B: {}'.format(a,b),align='center',font=('Courier',18,'normal'))
		ball.goto(0,0)
		ball.dx=.3
		ball.dy=.3
		ball.dx*=-1

	if paddle_a.ycor()>255:
		paddle_a.sety(255)

	if paddle_b.ycor()>255:
		paddle_b.sety(255)

	if paddle_a.ycor()<-255:
		paddle_a.sety(-255)

	if paddle_b.ycor()<-255:
		paddle_b.sety(-255)

	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+45 and ball.ycor()>paddle_b.ycor()-45):
		ball.setx(340)
		if ball.dx>0:
			ball.dx+=0.05
			ball.dy+=0.05
		ball.dx*=-1
		winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+45 and ball.ycor()>paddle_a.ycor()-45):
		ball.setx(-340)
		if ball.dx>0:
			ball.dx+=0.05
			ball.dy+=0.05
		ball.dx*=-1
		winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

