from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # Turtle kütüphanesini miras aldık
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_X = random.randint(-200, 200)
        random_Y = random.randint(-200, 200)
        self.goto(random_X, random_Y)