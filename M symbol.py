from turtle import *;

pos = [(-75, 0), (63, 0)]
bgcolor('black')
right(90)

for x,y in pos:
    up()
    goto(x, y)
    down()
    begin_fill()
    color('blue')
    for i in range(2):
        forward(200)
        left(90)
        forward(30)
        left(90)
    end_fill()

up()
goto(-75, 0)
down()
fillcolor('blue')
begin_fill()
left(35)
for i in range(2):
    forward(120)
    left(55)
    forward(30)
    left(125)
end_fill()

up()
goto(92.5, 0)
down()
fillcolor('blue')
begin_fill()
right(70)
for i in range(2):
    forward(120)
    right(55)
    forward(30)
    right(125)
end_fill()
