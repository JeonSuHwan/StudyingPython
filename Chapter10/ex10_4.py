import turtle as t

t.bgcolor("black")
t.pencolor("yellow")
t.speed(0)

rotate=4
radius=100

for x in range(100):
    t.forward(6)
    t.right(rotate)
    t.circle(radius)
    rotate*=1.02
    radius*=0.98
