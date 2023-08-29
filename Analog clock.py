
import turtle
import time

obj=turtle.Turtle()
obj.speed(0)
obj.color("red")
obj.pensize(3)
obj.penup()
obj.setpos(0,-100)
obj.pendown()
obj.circle(100)
dial=turtle.Turtle()
dial.color("blue")
dial.penup()
dial.setpos(0,0)
dial.pendown()

dial2=turtle.Turtle()
dial2.color("yellow")
dial2.penup()
dial2.setpos(0,0)
dial2.pendown()

dial3=turtle.Turtle()
dial3.color("red")
dial3.penup()
dial3.setpos(0,0)
dial3.pendown()

for num in range(0,60):
  obj.penup()
  obj.setpos(0,0)
  obj.pendown()
  obj.pensize(1)
  obj.penup()
  obj.forward(80)
  obj.pendown()
  obj.forward(20)
  obj.penup()
  obj.setpos(0,0)
  obj.right(6)
obj.pensize(3)
for num in range(0,12):
  obj.penup()
  obj.setpos(0,0)
  obj.pendown()
  obj.penup()
  obj.forward(70)
  obj.pendown()
  obj.forward(30)
  obj.penup()
  obj.setpos(0,0)
  obj.right(30)

dial.setheading(90)
dial.pensize(10)
dial.speed(0)

dial2.setheading(90)
dial2.pensize(10)
dial2.speed(0)

dial3.setheading(90)
dial3.pensize(10)
dial3.speed(0)

for hour in range(0,60):
  for min in range(0,60):
    for sec in range(0,60):
    
      time.sleep(1)
      dial.forward(100)
      dial.clear()
      dial.setpos(0,0)
      dial.right(6)
    dial2.forward(70)
    dial2.clear()
    dial2.setpos(0,0)
    dial2.right(6)
  dial3.forward(50)
  dial3.clear()
  dial3.setpos(0,0)
  dial3.right(48)
    
















  
