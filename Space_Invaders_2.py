_author_ = "Stephen Mayanja"
_class_ = "SEIS 603"
_semester_ ="Summer class"

import turtle
from turtle import *
import os
import random

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


# #draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(6)
border_pen.pendown()

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

border_pen.hideturtle()


#hide the default turtle
turtle.ht()
#this save memory
turtle.setundobuffer(1)
#this speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        #boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if(self.xcor() >= (other.xcor() - 20)) &  (self.xcor() <= (other.xcor() + 20))& (self.ycor() >= (other.ycor() - 20)) &(self.ycor() <= (other.ycor() + 20)):
                return True
        else:
            return False




class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1




class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        self.speed = 6
        self.setheading(random.randint(0,360))

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color,startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"

    def fire(self):
        if self.status == "ready":
            self.status = "firing"

    def move(self):
        #move if fired
         if self.status == "firing":
             self.fd(self.speed)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
    def draw_border(self):
        self.pen.speed(0)

#create game object
game = Game()

#create my sprites
player = Sprite("triangle", "white",0,0)
# enemy = Enemy("circle","red", -100, 0)
missile = Missile("triangle", "yellow", 0,0)

#keyboard binding
wn.onkey(player.turn_left, "Left")
wn.onkey(player.turn_right, "Right")
wn.onkey(player.accelerate, "Up")
wn.onkey(player.decelerate, "Down")
wn.listen()



#main game loop
while True:
    player.move()
    # enemy.move()




wn.mainloop()