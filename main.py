import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.title("turtle crossing")

score_board = Scoreboard()
carmanager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_left()

    for cars in carmanager.all_car:
        ''' here having same variable name can cause confusion to computer '''
        if cars.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.at_finish_line():
        player.start_line()
        carmanager.level_up()
        score_board.increase_level()
