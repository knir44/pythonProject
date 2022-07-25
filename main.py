import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(height = 400,width = 500)
user_bet = screen.textinput(title ="Make your bet", prompt ="Which turtle will win the race? Enter a color: ")



colors =["red","orange","yellow","green","blue","purple"]
turtle_pivot =[-100,-60,-20,20,60,100]
all_turtle = []


for turtule_index in range(0,6):
    new_turtle = t.Turtle(shape ="turtle")
    new_turtle.color(colors[turtule_index])
    new_turtle.penup()
    new_turtle.goto(x = -240, y = turtle_pivot[turtule_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


        rand_distace = random.randint(0,10)
        turtle.forward(rand_distace)




screen.exitonclick()