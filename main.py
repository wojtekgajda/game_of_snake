from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Game of Snake")

on_move = True

snake = Snake()
score = Score()

food = Food()
food.appearance()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while on_move:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.snake_head.distance(food) < 20:
        food.appearance()
        snake.create_single_segment()
        score.score_counter()

    if snake.snake_head.xcor() > 299 or snake.snake_head.xcor() < -299:
        # on_move = False
        # score.end_game()
        score.reset()
        snake.snake_reset()

    if snake.snake_head.ycor() > 299 or snake.snake_head.ycor() < -299:
        # on_move = False
        # score.end_game()
        score.reset()
        snake.snake_reset()
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 2:
            # on_move = False
            score.reset()
            snake.snake_reset()

screen.exitonclick()
