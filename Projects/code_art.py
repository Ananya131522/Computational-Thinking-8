import turtle 

t = turtle.Turtle()

t.goto (-100,0)
t.speed (10)

colors = ["Orchid","Violet","Plum"]
for i in range (10000):
    t.color(colors[i % 3])
    t.forward(100 + i)
    t.left(120+1)

t.penup()
t.goto(5,5)
t.pendown()
colors = ["SteelBlue", "DodgerBlue", "DeepSkyBlue"]
for i in range (100):
    t.color(colors[i % 3])
    t.forward(100 + i)
    t.left(120 + 1)