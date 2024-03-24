import turtle

window = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")

def triangulo():
    for i in range(3):
        turtle.color("blue")
        turtle.pensize(7)
        turtle.forward(100)
        turtle.right(120)
        
def cuadrado():
    for i in range(4):
        turtle.color("green")
        turtle.forward(100)
        turtle.right(90)

def poligono():
    for i in range(5):
        turtle.color("red")
        turtle.forward(100)
        turtle.right(360/5)

def lado6():
    for i in range(6):
        turtle.color("black")
        turtle.forward(100)
        turtle.right(360/6)

def lado7():
    for i in range(7):
        turtle.color("pink")
        turtle.forward(100)
        turtle.right(360/7)

def lado8():
    for i in range(8):
        turtle.color("orange")
        turtle.forward(100)
        turtle.right(360/8)

def lado9():
    for i in range (9):
        turtle.color("purple")
        turtle.forward(100)
        turtle.right(360/9) 


   

    

triangulo()
cuadrado()
poligono()
lado6()
lado7()
lado8()
lado9()
turtle.exitonclick()