from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("White")
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))

    def increase_score(self):
        self.score += 1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))



