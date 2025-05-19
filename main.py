import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("lightskyblue")
t=turtle.Turtle()
t.penup()
t.goto(0,210)
t.pendown()
t.pencolor('darkblue')
t.write('The Beach', font=("Arial", 35, "bold"), align="center")
t.hideturtle()

t.penup()
t.goto(-450,-50)
t.color("blue")
t.begin_fill()
t.pendown()
t.forward(800)
t.right(90)
t.forward(300)
t.right(90)
t.forward(800)
t.right(90)
t.forward(300)
t.right(90)
t.end_fill()


t.penup()
t.goto(-450,-250)
t.color("tan")
t.begin_fill()
t.pendown()
t.forward(900)
t.left(90)
t.forward(200)
t.left(90)
t.forward(800)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.penup()
t.goto(250, 150)
t.color("yellow")
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-200,-100)
t.color("saddlebrown")
t.begin_fill()
t.pendown()
t.setheading(90)
t.forward(60)
t.right(90)
t.forward(10)
t.right(90)
t.forward(60)
t.right(90)
t.forward(10)
t.end_fill()

t.penup()
t.goto(-195,-40)
t.color("green")
t.pendown()
t.setheading(60)

for _ in range(5):
    t.begin_fill()
    t.circle(30,60)
    t.left(120)
    t.circle(30,60)
    t.end_fill()
t.setheading(t.heading()+72)

t.penup()
t.goto(50,-180)
t.color('limegreen')
t.begin_fill()
t.pendown()
t.circle(20)
t.end_fill()
t.penup()
t.goto(200,-150)
t.color("gray")
t.pendown()
t.setheading(90)
t.forward(50)

t.color('purple')
t.begin_fill()
t.right(90)
t.circle(40,180)
t.end_fill()

t.penup()
t.goto(-200,200)
t.color('white')
t.begin_fill()
t.pendown()
for _ in range(3):
    t.circle(20)
    t.forward(20)

t.end_fill()

t.penup()
t.goto(-50,-180)
t.color("orange")
t.begin_fill()
t.pendown()
for _ in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

t.penup()
t.goto(120, -190)
t.color("pink")
t.begin_fill()
t.pendown()
t.setheading(0)
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(60)
t.right(90)
t.forward(20)
t.end_fill()

t.penup()
t.goto(120, -190)
t.color("red")
t.begin_fill()
t.pendown()
t.setheading(0)
for _ in range(2):
 t.forward(60)
 t.right(90)
 t.forward(20)
 t.right(90)
t.end_fill()

t.color("white")
for x in range(125, 175, 10):
 t.penup()
 t.goto(x, -190)
 t.setheading(270)
 t.pendown()
 t.forward(20)



t.penup()
t.goto(-120, -190)
t.color("dimgray")
t.begin_fill()
t.pendown()
t.circle(10)
t.end_fill()


t.penup()
t.goto(-100, -180)
t.begin_fill()
t.pendown()
t.circle(7)
t.end_fill()






t.penup()
t.goto(-100, 180)
t.pendown()
t.color("black")
t.setheading(60)
t.forward(10)
t.backward(10)
t.setheading(120)
t.forward(10)
t.backward(10)


t.penup()
t.goto(-60, 160)
t.pendown()
t.setheading(60)
t.forward(10)
t.backward(10)
t.setheading(120)
t.forward(10)
t.backward(10)


t.penup()
t.goto(0, 170)
t.pendown()
t.setheading(60)
t.forward(10)
t.backward(10)
t.setheading(120)
t.forward(10)
t.backward(10)































turtle.done()


































turtle.done()