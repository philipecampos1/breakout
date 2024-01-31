from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.lives = 3
        self.penup()
        self.goto(x=260, y=350)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} Lives:{self.lives}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def win(self):
        self.goto(x=0, y=0)
        self.write("You win", align="center", font=("Arial", 24, "normal"))

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()
