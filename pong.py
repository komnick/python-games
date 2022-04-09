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
window.bgcolor('white')
window.setup(width=800, height=600)
window.tracer(0)

# George (Left Paddle)
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('black')
leftPaddle.shapesize(stretch_width=5, stretch,len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# Jennifer (Right Paddle)
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('black')
rightPaddle.shapesize(stretch_width=5, stretch,len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# Thr Child (Ball)

# Main Game Loop
while True:
    window.update()
    
