import turtle as t
import random


colors = ["red", "blue", "green", "pink", "violet", "yellow"]
turtle_list = []

my_screen = t.Screen()
my_screen.setup(500, 400)
my_screen.colormode(255)
my_screen.bgcolor("pink")
user_bet = my_screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")

is_race_on = False


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def set_appearance():
    for i in range(0, 6):
        new_turtle = t.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        turtle_list.append(new_turtle)


def set_start():
    border = 100
    for tur in turtle_list:
        tur.setheading(90)
        tur.fd(border)
        tur.setheading(180)
        tur.fd(240)
        tur.setheading(0)
        border -= 50


set_appearance()
set_start()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print("You win.")
            else:
                print(f"You lose. The turtle winner is {turtle.pencolor()} turtle.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


my_screen.exitonclick()