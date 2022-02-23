from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def all_clear():
    t.clear()
    t.reset()

s.onkey(key='w', fun=move_forward)
s.onkey(key='s', fun=move_backward)
s.onkey(key='a', fun=turn_left)
s.onkey(key='d', fun=turn_right)
s.onkey(key='c', fun=all_clear)

