from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()

s.listen()
s.onkey(fun=snake.up, key="Up")
s.onkey(fun=snake.down, key="Down")
s.onkey(fun=snake.left, key="Left")
s.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.change_location()
        scoreboard.increase_score()
        scoreboard.display_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.game_over()
        game_is_on = False
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

s.exitonclick()
