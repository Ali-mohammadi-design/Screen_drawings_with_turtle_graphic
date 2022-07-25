from turtle import Turtle,Screen
timy=Turtle()
screen=Screen()
def move():
    timy.forward(10)
def  right():
    timy.right(5)
def backward():
    timy.backward(10)
def  left():
    timy.left(5)
def  right90():
    timy.right(90)
def curve_right():
    timy.right(5)
    timy.forward(5)
def curve_left():
    timy.left(5)
    timy.forward(5)
def clear():
    timy.penup()
    timy.goto(0, 0)
    timy.clear()
    timy.pendown()

print(timy.position())
screen.listen()
screen.onkey(key="w",fun=move)
screen.onkey(key="d",fun=curve_right)
screen.onkey(key="a",fun=curve_left)
screen.onkey(key="s",fun=backward)
screen.onkey(key="t",fun=right90)
screen.onkey(key="space",fun=clear)

screen.exitonclick()
