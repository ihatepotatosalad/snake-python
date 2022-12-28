import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score_Board
screen = Screen()

screen.setup(width=600, height=600)


screen.bgcolor('black')

screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score_Board()
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.snake_move()

    if snake.snake_head.distance(food) < 15:
        food.respawn()
        snake.extend()
        score_board.add_to_score()
    if snake.snake_head.xcor() > 290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290 or snake.snake_head.xcor() < -290:
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_is_on = False

score_board.game_over()

screen.exitonclick()
