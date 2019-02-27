import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Miku Space Game")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("yellow")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

#drwa the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-290,280)
scorestring ="Score: %s" %score
score_pen.write(scorestring,False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed=30

number_of_enemies=8

enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed = 8

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(1,1)
bulletspeed = 150


bulletstate ="ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate ="fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollosion(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 40:
        return True

    else:
        return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
# move the enemy back and down
        if enemy.xcor()> 280:
#moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)

            enemyspeed *= -1

        # check for collision between the bullet and the enemy
        if isCollosion(bullet, enemy):

            #Reset the Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(x,y)


             # update the score

            score += 20
            scorestring = "Score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring,False, align= "left", font =("Arial",14,"normal"))
        
        if isCollosion(player,enemy):
            player.hideturtle()
            enemy.heading()
            print("Game Over")
            break

        #move the Bullet

        if bulletstate =="fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor()>275:
            bullet.hideturtle()
            bulletstate = "ready"


