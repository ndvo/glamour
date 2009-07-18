import obj_images
import os
import random
import enemy
import pygame
from pygame.locals import *

class Princess():
    """Creates the princess. Princess is a rather complex class in comparison with the enemies, for princess has many atributes called 'Princess Parts'. That's because princess instance is not build with a single group of images, but a bunch of groups of images that may or not be blitted to the screen.
Princess Parts are her dress, her hair, her eyes, arms and everything that may move or change.
This class uses obj_images module for retrieving images from directories.
It is one of the first classes written, which means that it is somewhat old and may contain som old and useless code that was not well cleaned. This will be corrected soon, I hope.
You need only a 'self' as a parameter for this class. The other atributes are default.
Problems to be fixed in this class are:
Princess controls are not good enough, probably because of the clock tick;
Princess movement determines the camera, and this may not continue for Princess needs to move in the camera more freely;
Princess shoes are moving weirdly while she jumps.
The code is not yet well commented
"""
    directory = 'data/images/princess/'
    def __init__(self,level,save = None, INSIDE = False):
        self.level = level
        try:
            self.file = save.readlines()
        except:
            self.file = open(save).readlines()
        self.size       = (80,180)
        for line in self.file:
            linha = line.split()
            if linha[0] == 'name':
                self.name = linha[1]
            if linha[0] == 'center_distance':
                self.center_distance = int(linha[1])
            if linha[0] == 'dirt':
                self.dirt = int(linha[1])
        self.pos        = [self.level.universe.center_x+self.center_distance,
                           self.level.universe.floor - 186 -self.size[1]]
        for act in ['walk','stay','kiss','fall','jump','ouch','celebrate']:
            exec('self.'+act+'_img = obj_images.MultiPart(self.ordered_directory_list("'+act+'"))')
        self.dirties = [  Dirt(level,'data/images/princess/dirt1',self.pos),
                          Dirt(level,'data/images/princess/dirt2',self.pos),
                          Dirt(level,'data/images/princess/dirt3',self.pos)]
        self.images = None
        self.open_door_img = self.stay_img
        self.lips       = obj_images.TwoSided('data/images/effects/kiss/')
        self.dirt_cloud = obj_images.TwoSided('data/images/effects/dirt/')
        self.glamour_points = 0
        self.gforce     = 0
        self.g_acceleration = 3
        self.speed      = 10
        self.effects    = []
        self.rect       = Rect(self.pos,self.size)
        self.move       = False
        self.direction  = 'left'
        self.got_hitten = 0
        self.jump       = 0
        self.kiss       = 0
        self.kiss_direction = 'left'
        self.kiss_rect = ((0,0),(0,0))
        self.floor = self.level.universe.floor - 186
        self.action = [None,'stay']
        self.image = self.stay_img.left[self.stay_img.itnumber.next()]
        self.image_size = self.image.get_size()
        self.inside = INSIDE

    def ordered_directory_list(self, action):
        odl = []
        for part in ["hairback","skin","face","hair","shoes","dress","arm","armdress","accessory"]:
            for line in self.file:
                if part in line:
                    l = line.split()
                    if l[0] == part and l[1] != 'None':
                        odl.extend([str(self.directory+l[1]+"/"+action+"/")])
        return odl

    def update_all(self):
        if not self.inside:
            self.direction  = self.level.universe.dir
            self.action     = self.level.universe.action
            self.effects = []
            self.update_pos(self.action)
            self.jumping(self.action)
            self.hurting(self.action)
            self.kissing()
            if self.got_hitten>5:
                if self.got_hitten%2 == 0:
                    self.update_image(self.action,self.direction)
                else:
                    self.image = None
            else:
                self.update_image(self.action,self.direction)
        else:
            self.update_image(self.action,self.direction)

    def dirt_cloud_funciton(self):
        if 0 < self.got_hitten < 24:
            if self.got_hitten > len(self.dirt_cloud.left):
                dirt_cloud_image = (self.dirt_cloud.left[self.got_hitten-1-len(self.dirt_cloud.left)])
            else:
                dirt_cloud_image = (self.dirt_cloud.left[self.got_hitten-1])
            self.effects.append((dirt_cloud_image,(self.pos)))

    def jumping(self,action):
        feet_position = self.pos[1]+self.size[1]
        if action[0]!= 'jump' and action[0]!= 'jump2':
            self.jump = 0
        if feet_position == self.floor and not self.jump:
            if action[0]== 'jump':
                self.jump = 1
                os.popen4('ogg123 ~/Bazaar/Glamour/glamour/data/sounds/princess/pulo.ogg')
                self.images.number = 0
        if self.jump > 0 and self.jump <20:
            self.pos[1] -= 30
            if self.jump > 5:
                if self.images.lenght-1 > self.images.number:
                    self.images.number += 1
            if self.jump > 10:
                self.images.number = 0
                action[0]= 'fall'
            self.jump +=1
        if action[0]=='fall':
            if feet_position == self.floor:
                action[0]=None
                os.popen4('ogg123 ~/Bazaar/Glamour/glamour/data/sounds/princess/fall/spike_heel/street/'+str(random.randint(0,0))+'.ogg')
        if feet_position < self.floor and not self.jump:
            action[0]='fall'

    def hurting(self,action):
        if not self.inside:
            if not self.got_hitten:
                for e in self.level.enemies:
                    if e.__class__ == enemy.Schnauzer:
                        if self.rect.colliderect(e.rect):
                            if self.dirt <= 2:
                                self.got_hitten += 1
                                self.dirt += 1
                                self.level.princesses[1] = self.dirties[self.dirt -1]
            else:
                self.got_hitten +=1
                if self.got_hitten == 30   :#75 at 25 frames per second
                    self.got_hitten = 0
            if self.got_hitten and self.got_hitten <6:
                action[0]='ouch'
            if self.got_hitten >=6:
                action[0]= None

    def kissing(self):
        if self.action[0] == 'kiss' or self.kiss > 0:
            self.kiss +=1
            if self.kiss == 1:
                self.images.number = 0
        if self.kiss > 0:
            if self.kiss< 4:
                self.action[0] = 'kiss'
            else:
                self.action[0] = None
            if self.kiss <9:
                self.throwkiss()
            else:
                self.kiss = 0
                self.kiss_rect = Rect ((0,0),(0,0))

    def update_pos(self,action):
        feet_position   = self.pos[1]+self.size[1]
        self.floor = self.level.universe.floor- self.level.what_is_my_height(self)
        self.pos[0] = self.level.universe.center_x+self.center_distance

        #fall
        if feet_position < self.floor:
            self.pos[1] += self.gforce
            self.gforce += self.g_acceleration
        #do not fall beyond the floor
        if feet_position >= self.floor:
            self.pos[1]= self.floor-self.size[1]
        if feet_position == self.floor:
            self.gforce = 0


        if action[1]=='walk' and action[0] != 'celebrate':
           if self.direction == 'right':
               self.center_distance += self.speed
           else:
               self.center_distance -= self.speed

    def soundeffects(self,action):
        if action[1]=='walk' or action[0] == 'celebrate':
            if self.images.number == 3:
                os.popen4('ogg123 ~/Bazaar/Glamour/glamour/data/sounds/princess/steps/spike_heel/street/'+str(random.randint(0,1))+'.ogg')
            if self.images.number == 6:
                os.popen4('ogg123 ~/Bazaar/Glamour/glamour/data/sounds/princess/steps/spike_heel/street/'+str(random.randint(2,3))+'.ogg')

    def throwkiss(self):
        if self.kiss == 1:
            self.kiss_direction = self.direction
        if self.kiss_direction == 'right':
            kissimage = self.lips.left[self.kiss-1]
            self.effects.append((kissimage,(self.pos[0],self.pos[1])))
            self.kiss_rect = Rect((self.pos[0],self.pos[1]),((self.kiss)*44,self.size[1]))
        else:
            kissimage = self.lips.right[self.kiss-1]
            self.effects.append((kissimage,(self.pos[0]-200,self.pos[1])))
            self.kiss_rect = Rect((self.pos[0]-((self.kiss)*44),self.pos[1]),((self.kiss)*44,self.size[1]))



    def update_image(self,action,direction):
        #Correct rect position when turned left
        if self.direction == 'right':
            self.rect   = Rect(self.pos,self.size)
        else:
            self.rect = Rect((self.pos[0]+100,self.pos[1]),self.size)
        chosen = action[0] or action[1]
        if direction == 'left':
            exec('self.images = self.'+chosen+'_img \n'+
                'actual_images = self.'+chosen+'_img.right')
        else:
            exec('self.images = self.'+chosen+'_img \n'+
                'actual_images = self.'+chosen+'_img.left')
        self.image = actual_images[self.images.number]
        if not self.jump:
            self.images.update_number()

    def save(self):
        pass

    def change_clothes(self,part,dir):
        self.parts.pop(part.index)
        part = PrincessPart(self,'data/images/princess/'+str(dir),part.index)


class Dirt():
    image_number = 0
    def __init__(self, level, directory,pos):
        self.level = level
        self.directory = directory
        for act in ['walk','stay','kiss','fall','jump','ouch','celebrate']:
            exec('self.'+act+' = obj_images.TwoSided(str(directory)+"/'+act+'/")')
        self.open_door = self.walk
        self.list = self.stay
        self.actual_list = self.list.left
        self.pos = pos
        self.image = self.actual_list[self.image_number]
        self.past_choice = None

    def update_all(self):
        self.pos = self.level.princesses[0].pos
        chosen = self.level.princesses[0].action[0] or self.level.princesses[0].action[1]
        if self.level.princesses[0].direction == 'left':
            exec('self.images = self.'+chosen+' \n'+
                 'actual_images = self.'+chosen+'.right')
        else:
            exec('self.images = self.'+chosen+' \n'+
                'actual_images = self.'+chosen+'.left')
        if chosen != self.past_choice:
            self.images.number = 0
        self.past_choice = chosen
        self.image = actual_images[self.images.number]
        if not self.level.princesses[0].jump:
            self.images.update_number()
