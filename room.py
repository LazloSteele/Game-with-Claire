from describe_room import DescribeRoom
from game_object import GameObject
import random
import assets

class Room(GameObject):
    def __init__(self):
        self.name = random.randint(0,100)
        self.focus = None
        self.secret = None
        self.contents = []
        self.exits = ['NORTH', 'SOUTH', 'EAST', 'WEST']

        self.generate_contents()

    def generate_contents(self):
        self.generate_plants()

        self.focus = random.choice(self.contents)
        

    def generate_plants(self):
        
        for plant_type in assets.Plants:
            n = random.randint(1, 6)
            while n > 0:
                self.contents.append(assets.TreeFactory(random.choice(plant_type)))
                n -= 1

    
    
