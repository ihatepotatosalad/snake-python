from turtle import Turtle


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.write(f'Score: {self.score}')

    def add_to_score(self):

        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}')

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER final score: {self.score}', font=(
            'Arial', 15, 'normal'), align='center')
