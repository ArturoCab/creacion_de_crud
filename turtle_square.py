import turtle

window = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.pensize(3)
tortuga.pencolor("deeppink")

for i in range(4):
    tortuga.forward(100)
    tortuga.right(90)

window.mainloop()
