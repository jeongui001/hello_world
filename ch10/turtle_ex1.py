# turtle_ex1.py

import turtle

p = turtle.Pen()
p.shape('turtle')

for x in range(0,100,1):
    p.forward(x)
    p.left(90)