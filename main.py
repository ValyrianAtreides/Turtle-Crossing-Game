import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car = CarManager()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(player.up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car_move()

    if player.ycor() >300:
        print("next level")
        scoreboard.next_level()
        player.player_reset()
        car.car_next_level()

    for each_car in car.cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()




