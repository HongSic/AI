import turtle
turtle.shape('turtle')

def Forward():
      turtle.forward(10)

def Back():
    turtle.back(10)

def Left():
    turtle.lt(10)

def Right():
    turtle.rt(10)

def penUp():
    turtle.penup()

def penDown():
    turtle.pendown()

turtle.onkeypress(penUp,'a' )
turtle.onkeypress(penDown,'s' )
turtle.onkeypress(Forward, "Up")
turtle.onkeypress(Back, "Down")
turtle.onkeypress(Left, "Left") #turtle.onkeypress(Left, turtle.lt(10))와 동일
turtle.onkeypress(Right, "Right")
turtle.listen()
turtle.done()
