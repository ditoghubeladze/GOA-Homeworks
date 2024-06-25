from turtle import *

#we want to paint a house

#step 1: draw a square
speed(7)
width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward (70)
left(90)
color ("yellow")
begin_fill()
forward(120) # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200,200)
pendown()
# roof 
color("red")
begin_fill()
right(150)
forward(200)  
left(120)
forward(200)
end_fill()

penup()
goto(15,40)
pendown()

#windows(kompiuteris ara saxlsis (haha ra sasacilo iyo dagvyare xalxi))

color("cyan")
begin_fill()
right(150)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

penup()
goto(145,40)
pendown()

#window 2
begin_fill()
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

penup()
goto(0,0)
pendown()













exitonclick()