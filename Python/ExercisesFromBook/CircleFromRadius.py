# write a program that takes a user input of a radius and turns it into four drawn circles using turtle

radius = eval(input('Enter a radius: '))

import turtle

turtle.penup()
turtle.forward(radius)
turtle.pendown()
turtle.circle(radius)

turtle.right(180)
turtle.color('red')
turtle.circle(radius)
turtle.penup()

turtle.forward(radius * 2)
turtle.pendown()
turtle.color('blue')
turtle.circle(radius)

turtle.right(180)
turtle.color('yellow')
turtle.circle(radius)

turtle.done()

