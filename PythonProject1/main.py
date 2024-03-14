import turtle
from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_rectangle(self, rectangle):
        if (rectangle.lowleft.x < self.x < rectangle.upright.x):
            if (rectangle.lowleft.y < self.y < rectangle.upright.y):
                return True
        return False

    def __str__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y)


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def __str__(self):
        return "Lower Left:: " + str(self.lowleft) + "  Upper Right:: " + str(self.upright)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.upright.y)  # starting point
        canvas.pendown()

        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.goto(self.upright.x, self.lowleft.y)
        canvas.goto(self.upright.x, self.upright.y)
        canvas.goto(self.lowleft.x, self.upright.y)


window = turtle.Screen()

geoff = turtle.Turtle()

lowleft = Point(randint(-200, 0), randint(-200, 0))
upright = Point(randint(lowleft.x + 1, lowleft.x + 400),
                randint(lowleft.y + 1, lowleft.y + 400))
rect = GuiRectangle(lowleft, upright)

rect.draw(geoff)

window.exitonclick()
