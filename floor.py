import random
import pygame
from globals import *
from pygame.locals import *
from obj_images import *

class Floor():
    images = None


    def __init__(self,index,dir,level,height={'all':186},type='standard'):

        self.pieces = []
        count = 0
        while count < 41:
            self.pieces.append(count)
            count += 1
        self.floor_heights = {}

        if height['all']!= None:
            for i in self.pieces:
                self.floor_heights[i] = height['all']
        else:
            for i in height:
                if i != None:
                    self.floor_heights[i] = height[i]
        if self.images == None:
            self.images = ObjectImages_OneSided(dir)
        self.image_number = 0
        self.image_list = self.images.list
        self.image = self.image_list[self.image_number]
        self.size = self.image.get_size()
        self.distance_from_center = (self.size[0]*(index))
        self.type = type
        for i in level:
            i.floor_image.insert(index,self)
        self.pos = (universe.center_x+(self.distance_from_center),universe.floor-self.size[1])
    def update_pos(self):
        self.image_number += 1
        if self.image_number > len(self.image_list)-1:
            self.image_number = 0
        self.image = self.image_list[self.image_number]
        self.pos = (universe.center_x+(self.distance_from_center),universe.floor-self.size[1])
class Bridge():

    def __init__(self,directory,index,level,main=True):

        if main == True:    self.images = ObjectImages_OneSided(directory+'bridge/')
        else:               self.images = ObjectImages_OneSided(directory) 

        if main == True:
            self.left_bank = Bridge(str(directory)+'left_bank/',index-1,level,main = False)
            self.right_bank= Bridge(str(directory)+'right_bank/',index+1,level,main = False)

        self.image_number = 0
        self.image = self.images.list[0]
        self.size = self.image.get_size()

        if main == True:    self.distance_from_center = (400*(index))-400
        else:               self.distance_from_center = (400*(index))

        self.pos = (universe.center_x+(self.distance_from_center),universe.floor-self.size[1])
        if main == True:
            for i in level:
                del i.floor_image[index]
                i.floor_image.insert(0,self)
        else:
            for i in level:
                i.floor_image[index]= self

    def update_pos(self):
        self.image_number += 1
        if self.image_number > len(self.images.list)-1:
            self.image_number = 0
        self.image = self.images.list[self.image_number]
        
        self.pos = (universe.center_x+(self.distance_from_center),universe.floor-self.size[1])
        print 'updating bridge at ' + str(self.pos) +' '+ str(self.image_number)