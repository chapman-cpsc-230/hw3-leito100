
"""
File: <turtlestar.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<Drawing a star from user inputs.>
"""


import turtle

bob = turtle.Pen()

sides = int(input("Enter an odd natural number greater than 5:"))
side_len = int(input("Enter a natural number:"))

for i in range(sides):
        bob.forward(side_len)
        bob.left(180 - 180.0/sides)
        bob.forward(side_len)


inp = raw_input ("Hit <enter> to quit")

turtle.bye()
