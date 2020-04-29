import turtle

t = turtle.Pen()

my_color = ("red", "green", "yellow", "black" )

for i in range(5):
    t.penup()
    t.goto(0, -i*10)
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(10+i*10)

turtle.done()