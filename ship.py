import os


class Ship():
    def __init__(self):
        self.SHIP_WIDTH = 55
        self.SHIP_HEIGHT = 40
        self.SHIP_VELOCITY = 5
        self.BULLET_VELOCITY = 7
        self.SHIP_IMAGE_PATH = os.path.join('Assests', 'spaceship_red.png')
        self.MAX_BULLETS = 4