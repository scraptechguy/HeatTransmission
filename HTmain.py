import turtle

# table of specific heat capacities [in Joules per kilogram Kelvin]

materials = {
    "iron": "440", "steel": "452"
}


while True:
    
    mat1 = input("Enter the first material: ")

    try:
        materials[mat1]
        break

    except KeyError:
        print("Input value's got to be in the list of materials.")


while True:
    
    mat2 = input("Enter the second material: ")

    try:
        materials[mat2]
        break

    except KeyError:
        print("Sorry, input value's got to be in the list of materials.")




while True:

    try:
        T1 = float(input("Enter the temperature of {}: ".format(mat1)))
        break

    except ValueError:
        print("Sorry, temperature has got to be a number.")


while True:

    try:
        T2 = float(input("Enter the temperature of {}: ".format(mat2)))
        break

    except ValueError:
        print("Sorry, temperature has got to be a number.")


wn = turtle.Screen()
wn.setup(width=1280, height=720)
wn.bgcolor("black")
wn.tracer(0)

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

# text writing names of the two materials

txt1 = turtle.Turtle()
txt1.hideturtle()
txt1.color("white")
txt1.penup()

txt1.goto(-250, 140)
txt1.write(
    "{}".format(mat1),
    font=("Courier", 24, "normal")
)

txt1.goto(200, 140)
txt1.write(
    "{}".format(mat2),
    font=("Courier", 24, "normal")
)

# text writing delta temperature

txt2 = turtle.Turtle()
txt2.hideturtle()
txt2.color("white")
txt2.penup()

txt2.goto(-300, -300)


if T1 > T2:
    deltaT = T1 - T2
    obj3.goto(-deltaT, 0)

elif T1 < T2:
    deltaT = T2 - T1
    obj3.goto(deltaT, 0)


print("SHC of first material is " + materials[mat1])
print("SHC of second material is " + materials[mat2])

while True:
    wn.update()

    # text writing delta temperature

    txt2.clear()
    txt2.write(
        "delta T is {} degrees celsius".format(deltaT),
        font=("Courier", 25, "normal")
    )

