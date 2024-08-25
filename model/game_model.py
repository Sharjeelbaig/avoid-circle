# model/game_model.py

import random

class GameModel:
    def __init__(self, width, height, box_width, box_height, circle_radius):
        self.width = width
        self.height = height
        self.box_width = box_width
        self.box_height = box_height
        self.box_x = width // 2 - box_width // 2
        self.box_y = height - box_height - 10
        self.box_speed = 10
        self.circle_radius = circle_radius
        self.circle_speed = 7
        self.circles = []
        self.score = 0

    def move_box(self, direction):
        if direction == "left" and self.box_x > 0:
            self.box_x -= self.box_speed
        if direction == "right" and self.box_x < self.width - self.box_width:
            self.box_x += self.box_speed

    def add_circle(self):
        if random.randint(1, 20) == 1:
            self.circles.append([random.randint(0, self.width - self.circle_radius), 0])

    def move_circles(self):
        for circle in self.circles:
            circle[1] += self.circle_speed
            if circle[1] > self.height: # If the circle is out of the screen
                self.circles.remove(circle) # Remove the circle
                self.score += 1 # Increment the score

    def check_collision(self): 
        for circle in self.circles:
            if self.is_collision(self.box_x, self.box_y, self.box_width, self.box_height, circle[0], circle[1]):
                return True
        return False

    def is_collision(self, box_x, box_y, box_width, box_height, circle_x, circle_y):
        if (circle_x + self.circle_radius > box_x) and (circle_x - self.circle_radius < box_x + box_width):
            if (circle_y + self.circle_radius > box_y) and (circle_y - self.circle_radius < box_y + box_height):
                return True
        return False
