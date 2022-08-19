import os


class Settings():
    # A class to store all the settings of the alien invasion game

    def __init__(self):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.BACKGROUND_IMAGE_PATH = os.path.join('Assests', 'space.png')