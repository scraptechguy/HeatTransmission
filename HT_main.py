import turtle

wn = turtle.Screen()
wn.setup(width=1280, height=720)
wn.bgcolor("black")

# obj1 is main block displaying two different materials 
# obj2 is the line representing two different objects (on the left and on the right)
# obj3 is red square representing heat


obj1 = turtle.Turtle()
obj1.hideturtle()
obj1.color("white")
obj1.shape("square")
obj1.penup()
obj1.shapesize(10, 40)


obj2 = turtle.Turtle()
obj2.hideturtle()
obj2.color("blue")
obj2.shape("square")
obj2.penup()
obj2.shapesize(20, 0.1)


obj3 = turtle.Turtle()
obj3.hideturtle()
obj3.color("red")
obj3.shape("square")
obj3.penup()
obj3.shapesize(3, 3)



obj1.showturtle()
obj2.showturtle()
obj3.showturtle()



while True:
    wn.update()

