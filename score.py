from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.initial_high_score()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def initial_high_score(self):
        with open("High_scores.txt","r") as file:
             hs = file.read()
             self.high_score = int(hs)

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_scores.txt","w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!!" , False, align=ALIGNMENT, font=FONT)


