import turtle

def move_forward(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

def move_backward(distance):
    turtle.penup()
    turtle.backward(distance)
    turtle.pendown()

def center_circle(radius):
    turtle.right(90)
    move_forward(radius)
    turtle.left(90)
    turtle.circle(radius)
    turtle.left(90)
    move_forward(radius)
    turtle.right(90)

def circs(num, rad):
    turtle.tracer(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward((num * rad) / 3.14)
    turtle.right(90)
    turtle.pendown()
    step = 360 / num
    for i in range(num):
        turtle.right(step)
        move_forward(rad * 2)
        center_circle(rad)
    turtle.right(90)
    turtle.penup()
    turtle.forward((num * rad) / 3.14)
    turtle.left(90)
    turtle.tracer(1)

    

turtle.speed(0)
turtle.goto(50,50)
for num in range(1,100, 5):
    circs(num, 4)

turtle.done()