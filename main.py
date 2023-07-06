from Snake import Snake
from turtle import Screen
import time



#turtle creation
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

my_snake= Snake()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.right,"Right")
screen.onkey(my_snake.left,"Left")


def update():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        my_snake.move_snake()


update()













#function calls

screen.exitonclick()
