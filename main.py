from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Score
import time


food = Food()
screen = Screen()
scoreboard = Score()



screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

my_snake = Snake()

screen.update()


screen.listen()
screen.onkey(fun=my_snake.c_up, key="Up")
screen.onkey(fun=my_snake.c_down, key="Down")
screen.onkey(fun=my_snake.c_left, key="Left")
screen.onkey(fun=my_snake.c_right, key="Right")


game_on = True
while game_on:
    time.sleep(.08)

    my_snake.move()

    # wall collision
    if my_snake.head.xcor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() < -290 or my_snake.head.ycor() \
            > 290:
        scoreboard.reset()
        my_snake.reset()

    # tail collision
    for seg in my_snake.segment[1:]:
        if my_snake.head.distance(seg) < 10:
            scoreboard.reset()
            my_snake.reset()

    if food.distance(my_snake.head) < 15:
        my_snake.extend()
        food.refresh()
        scoreboard.add_score()
    screen.update()












screen.exitonclick()