from turtle import Turtle,Screen
import random
screen=Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

# tim1=Turtle(shape="turtle")
# tim2=Turtle(shape="turtle")
# tim3=Turtle(shape="turtle")
# tim4=Turtle(shape="turtle")
# tim5=Turtle(shape="turtle")
# tim1.color("yellow")
# tim2.color("red")
# tim3.color("green")
# tim4.color("orange")
# tim5.color("purple")
# tim1.penup()
# tim2.penup()
# tim3.penup()
# tim4.penup()
# tim5.penup()
# tim1.goto(x=-250,y=0)
# tim2.goto(x=-250,y=-40)
# tim3.goto(x=-250,y=20)
# tim4.goto(x=-250,y=-20)
# tim5.goto(x=-250,y=40)
color=["red",'blue',"orange",'green','yellow']
turtles_list=[]
t=-40
for i in range(0,5):
    turtles=Turtle(shape="turtle")
    turtles.penup()
    turtles.color(color[i])
    turtles.goto(x=-250,y=t)
    t+=20
    turtles_list.append(turtles)

if user_bet:
    is_race_on=True

while is_race_on:
    
    for turtle in turtles_list:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=(turtle.pencolor())
            if winning_color==user_bet:
                print("You have 'won' the race! ",winning_color," has won the race")
                break
            else:
                print("You have 'lost' the race! ",winning_color," has won the race")
                break
        distance=random.randint(0,10)
        turtle.forward(distance)
        turtle.speed("fastest")







screen.exitonclick()