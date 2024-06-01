import turtle
import time

def draw_heart():
    t = turtle.Turtle()
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

# Setup screen
screen = turtle.Screen()
screen.title("For My Bunny")
screen.bgcolor("black")

# Run the heart drawing in a loop
while True:
    draw_heart()
    time.sleep(1)
    screen.clear()  # Clear the screen to draw the heart again
    screen.bgcolor("black") 
