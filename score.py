from turtle import Turtle

with open("high_score.txt") as HIGH_SCORE_FILE:
    high_score_data = HIGH_SCORE_FILE.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = int(high_score_data)
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center",
                   font=("Aerial", 24, "normal"))

    def score_counter(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center",
                   font=("Aerial", 24, "normal"))

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Aerial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", align="center",
                   font=("Aerial", 24, "normal"))
