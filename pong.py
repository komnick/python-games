#! /usr/bin/python3

'''simple pong'''
'''
Nathan
4/8/22
Dads teaching me coding for games, this is pong | . |
'''

import turtle as t
print('Starting Pong...')

window = t.Screen()
window.title('Pong by Nathan')
window.bgcolor('blue')
window.setup(width=800, height=600)
window.tracer(0)

# George (Left Paddle)
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('black')
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# Jennifer (Right Paddle)
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('black')
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# The Child (Ball)
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('orange')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

#Function
def leftPaddleUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def leftPaddleDown():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)    

def leftPaddleLeft():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def leftPaddleRight():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)    

def rightPaddleUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def rightPaddleDown():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def rightPaddleLeft():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def rightPaddleRight():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(leftPaddleLeft, "a")
window.onkeypress(leftPaddleRight, "d")
window.onkeypress(rightPaddleUp, "w")
window.onkeypress(rightPaddleDown, "s")
window.onkeypress(rightPaddleLeft, "a")
window.onkeypress(rightPaddleRight, "d")

# Main Game Loop
while True:
    window.update()
    
