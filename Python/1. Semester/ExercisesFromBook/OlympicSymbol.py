#drawing the olympic symbol using turtle

import turtle
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.color('blue')
turtle.circle(45)

turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.color('black')
turtle.circle(45)

turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.color('red')
turtle.circle(45)

turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.color('yellow')
turtle.circle(45)

turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.color('green')
turtle.circle(45)

turtle.done()
