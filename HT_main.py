import turtle


mat1 = input("Enter first material: ")
mat2 = input("Enter second material: ")

T1 = float(input("Enter the temprature of {}: ".format(mat1)))
T2 = float(input("Enter the temprature of {}: ".format(mat2)))

wn = turtle.Screen()
wn.setup(width=1280, height=720)
wn.bgcolor("black")

# obj1 is main block displaying two different materials 
# obj2 is the line representing two different objects (on the left and on the right)
# obj3 is red square representing heat


obj1 = turtle.Turtle()
obj1.hideturtle()
obj1.color("dark gray")
obj1.shape("square")
obj1.penup()
obj1.shapesize(10, 40)


obj2 = turtle.Turtle()
obj2.hideturtle()
obj2.color("dark blue")
obj2.shape("square")
obj2.penup()
obj2.shapesize(20, 0.1)


obj3 = turtle.Turtle()
obj3.hideturtle()
obj3.color("dark orange")
obj3.shape("square")
obj3.penup()
obj3.shapesize(3, 3)

obj1.showturtle()
obj2.showturtle()
obj3.showturtle()

txt1 = turtle.Turtle()
txt1.hideturtle()
txt1.color("white")
txt1.penup()

txt2 = turtle.Turtle()
txt2.hideturtle()
txt2.color("white")
txt2.penup()

txt1.goto(-250, 140)
txt1.write(
    "{}".format(mat1),
    font=("Courier", 24, "normal")
)

txt2.goto(200, 140)
txt2.write(
    "{}".format(mat2),
    font=("Courier", 24, "normal")
)

if T1 > T2:
    deltaT = T1 - T2

elif T1 < T2:
    deltaT = T2 - T1


while True:
    wn.update()

    obj3.goto(deltaT, 0)

