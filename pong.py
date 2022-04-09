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
window.setup(width=1000, height=500)
window.tracer(0)

# George (Left Paddle)
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('black')

# Jennifer (Right Paddle)
rightPaddle = t.Turtle()

# Thr Child (Ball)

# Main Game Loop
while True:
    window.update()
    
