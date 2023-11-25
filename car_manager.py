from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.create_car()


    def create_car(self):
        for car in range(30):
            random_x = random.randint(-100, 500)
            random_y = random.randint(-250, 280)
            self.add_Car(random_x,random_y)


    def add_Car(self,x,y):
        car=Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.shape("square")
        car.penup()
        car.goto(x,y)
        car.setheading(180)
        self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                car.goto(300,car.ycor())

    def car_next_level(self):
        self.clear_cars()  # Sadece araçları temizle
        self.create_car()
        self.speed += MOVE_INCREMENT
        #new_speed = self.speed() + MOVE_INCREMENT
        #for car in self.cars:
        #    car.speed(new_speed)

    def clear_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()








