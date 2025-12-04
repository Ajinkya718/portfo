import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
tim = Player()
screen.listen()
screen.onkey(tim.move_forward, "Up")
screen.onkey(tim.move_back, "Down")
car = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    #Detecting successful crossing
    if tim.ycor() == 290:
        tim.goto(0, -280)
        scoreboard.update_level()
        car.level_up()
    #Detect collision with cars
    for _ in car.all_cars:
        if tim.distance(_) < 20:
            tim.goto(0,0)
            tim.write("Crashed! Game Over!", align="center", font=("Arial", 20, "normal"))
            game_is_on = False

screen.exitonclick()






