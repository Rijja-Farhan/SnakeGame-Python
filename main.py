from Snake import Snake
from turtle import Screen
import time
from Food import Food
from scroreboard import scoreboard



#turtle creation
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

#objects creation
my_snake= Snake()
food = Food()
score =scoreboard()


#key listeners function calls
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.right,"Right")
screen.onkey(my_snake.left,"Left")


#function definations
game_is_on = True
def update():

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        my_snake.move_snake()
        detect_collision()
        detect_collision_with_wall()
        detect_collision_with_self()

def detect_collision():
    if( my_snake.head.distance(food)< 15 ):
       food.refresh()
       score.increase_score()
       my_snake.extend()

def detect_collision_with_wall():
    global game_is_on
    if(my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() < -280 or my_snake.head.ycor() > 280  ):
         game_is_on = False
         score.game_over()

def detect_collision_with_self():
    global game_is_on
    for segments in my_snake.segment[1:]:
     if(my_snake.head.distance(segments)<10):
         game_is_on = False
         score.game_over()





update()














#function calls

screen.exitonclick()
