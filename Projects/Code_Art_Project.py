import turtle 

t = turtle.Turtle()

t.goto (-100,0)
t.speed (10)

#this draws the pink pentagon
colors = ["MediumVioletRed","DeepPink", "PaleVioletRed","HotPink","LightPink","Pink"]
for i in range (100):
    t.color(colors[i % 6])
    t.forward(100 + 1)
    t.left(72 + 5)

t.penup ()
t.goto (0,0)
t.pendown ()

#this draws the purple one
colors = ["Orchid","Violet","Plum"]
for i in range (100):
    t.color(colors[i % 3])
    t.forward(100 + 1)
    t.left(72 + 5)

t.penup ()
t.goto (0,-2)
t.pendown ()

#this draws the green octagon
colors = ["SpringGreen", "MediumAquamarine", "ForestGreen", "SeaGreen"]
for i in range (100):
    t.color(colors[i % 3])
    t.forward(50 + 1)
    t.left(45 + 5)

t.penup ()
t.goto (-2,2)
t.pendown ()

#this draws the blue octagon
colors = ["SteelBlue", "DodgerBlue", "DeepSkyBlue", "CornflowerBlue"]
for i in range (100):
    t.color(colors[i % 3])
    t.forward(50 + 1)
    t.left(45 + 5)

t.penup ()
t.goto (0,0)
t.pendown ()

#this draws the yellow square) 
colors = ["PapayaWhip","LightGoldenrodYellow", "LemonChiffon" , "LightYellow"]
for i in range (100):
    t.color(colors[i % 3])
    t.forward(100 + 1)
    t.left(90+ 5)

turtle.exitonclick()

