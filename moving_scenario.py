from globals import *
from obj_images import *
from princess import *
from getscreen import os_screen

class MovingScenario():
    def __init__(self,index,level,dir):
        self.pos = (0,200)
        self.images = ObjectImages(dir)
        self.image_list= self.images.left
        self.image_number = 0
        self.move = False
        self.dir = 'left'
        self.distance_from_center = 0
        self.speed = 8
        self.pos = (self.distance_from_center, 200)
        self.count = 0
        self.image = self.image_list[self.image_number]
        self.size = self.image.get_size()
        for i in level:
            i.moving_scenario.insert(index,self)
    def set_pos(self,act,dir):
        self.pos = (universe.center_x + self.distance_from_center, universe.floor - ((self.size[1])-100))
        if act[1] == 'move':
            if dir == 'right' :
                self.distance_from_center += self.speed
            else:
                self.distance_from_center -= self.speed
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),(universe.floor-self.size[1])),(self.size))
   
