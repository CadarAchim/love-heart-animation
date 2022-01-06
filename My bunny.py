import turtle

t = turtle.Turtle()
turtle.title("For My Bunny")

screen=turtle.Screen()
screen.bgcolor("black")

t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)

t.end_fill()

t.up()
t.setpos(-65, 150)
t.down()
t.color('lightgreen')
t.write("I LOVE YOU", font=("Verdana", 14, "bold"))

t.ht()

turtle.mainloop()