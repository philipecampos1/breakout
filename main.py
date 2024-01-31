import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from score import Score
import time

score = Score()
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Breakout")
block_colors = ['purple', 'gold', 'tomato', 'skyblue', '#3c79b8', '#419f6a']
positions_y = 300
positions_x = -330
screen.tracer(0)
screen.listen()
player = Paddle((0, -250))
ball = Ball()
blocks = []

for row in range(3):
    for _ in range(8):
        block = Blocks(position_x=positions_x, position_y=positions_y, color=random.choice(block_colors))
        blocks.append(block)
        positions_x += 90
    positions_x = -330
    positions_y -= 40

screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 390 or ball.distance(player) < 25:
        ball.bounce_y()

    if ball.ycor() < -330:
        ball.reset_ball()
        score.decrease_lives()

    if score.lives == 0:
        game_is_on = False
        score.game_over()

    if score.score == 24:
        score.win()
        game_is_on = False

    for block in blocks:
        if ball.distance(block) < 40:
            block.destroy()
            blocks.remove(block)
            ball.bounce_y()
            score.increase_score()

screen.exitonclick()
