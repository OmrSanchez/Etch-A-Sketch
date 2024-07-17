from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def move_back():
    tim.bk(10)


def clear_screen():
    tim.setheading(0)
    tim.teleport(x=0, y=0)
    tim.clear()


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()




