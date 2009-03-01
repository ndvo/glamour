from globals import *


class Scenario():
    """It is necessary to extend this class in order to separete several classes of Scenario. Trees, Clouds, Posts and Buildings have different atributes and different functions."""
    def __init__(self,pos,dir,level,index = 1,type = None, parts=None):
        self.images = ObjectImages(dir)
        self.image_number = -1
        self.speed = 1
        self.image_list = self.images.left
        self.image = self.image_list[self.image_number]
        self.size = self.image.get_size()
        self.distance_from_center = pos[0]
        self.type = type
        self.parts = parts

        for i in level:
            i.scenarios.insert(index,self)
        self.pos = (universe.center_x+(self.distance_from_center),Level_01.floor-(self.size[1]-15))
    def update_pos(self):
        self.image_number += 1
        if self.image_number > len(self.image_list)-1:
            self.image_number = 0
        self.image = self.image_list[self.image_number]

        self.pos = (universe.center_x+(self.distance_from_center),Level_01.floor-(self.size[1]-15))




class Building():
    def __init__(directory,pos):
        self.images = ObjectImages_OneSided(directory)
        self.image_number = 0
        self.image_list = self.images.list
        self.image = self.image_list[self.image_number]
        self.size = self.image.get_size()
        self.distance_from_center = pos[0] 
    def create_parts(self):
        for i in self.parts:
            i = BuildingPart(i[name],i[pos],i[directory])

class Background():
    def __init__(self,pos,level,index,dir):
        self.index = index
        self.images = ObjectImages_OneSided(dir)
        self.image_number = 0
        self.image = self.images.list[self.image_number]
        self.size = self.image.get_size()
        self.pos = pos
        for i in level:
            i.background.insert(index,self)
    def update_image(self):
        self.image_number += 1
        if self.image_number > len(self.images.list)-1:
            self.image_number = -1
        self.image = self.images.list[self.image_number]

            
