import obj_images
import os
import random
import enemy
import pygame
import sqlite3
from pygame.locals import *
from settings import *

class Princess():
    """Creates the princess. Princess is a rather complex class in comparison with the enemies, for princess has many atributes called 'Princess Parts'. That's because princess instance is not build with a single group of images, but a bunch of groups of images that may or not be blitted to the screen.
Princess Parts are her dress, her hair, her eyes, arms and everything that may move or change.
This class uses obj_images module for retrieving images from directories.
It is one of the first classes written, which means that it is somewhat old and may contain som old and useless code that was not well cleaned. This will be corrected soon, I hope.
Problems to be fixed in this class are:
Princess shoes are moving weirdly when she jumps.
"""
    directory = 'data/images/princess/'
    def __init__(self,level,INSIDE = False,xpos=None):
        self.first_frame = True
        self.level = level
        self.effects    = []
        self.size       = (2,180*scale)
        #Acess db save file
        self.save_db     = level.universe.db
        self.save_cursor = level.universe.db_cursor
        row     = self.save_cursor.execute("SELECT * FROM save").fetchone()
        print "Connected to the Save Database for princess data\nRetrieved data: "+str(row)
        self.name = row['name']
        self.center_distance = int(int(row['center_distance'])*scale)
        if xpos:
            self.center_distance = int(xpos*scale)
        self.dirt            = int(row['dirt'])
        self.points          = int(row['points'])
        self.pos = [int(self.level.universe.center_x) + self.center_distance,
                           self.level.universe.floor - (186*scale) -self.size[1]]
        for act in ['walk','stay','kiss','fall','jump','ouch','celebrate']:
            exec('self.'+act+'_img = obj_images.MultiPart(self.ordered_directory_list("'+act+'"))')
        self.dirties = [Dirt(level,'data/images/princess/'+d,self.pos) for d in ('dirt1','dirt2','dirt3')]
        self.images = None
        self.open_door_img  = self.stay_img
        self.lips           = obj_images.TwoSided('data/images/effects/kiss/')
        self.dirt_cloud     = obj_images.TwoSided('data/images/effects/dirt/')
        self.gforce         = 0
        self.g_acceleration = 3*scale
        self.speed          = 10*scale
        self.rect           = Rect(self.pos,self.size)
        self.move           = False
        self.direction      = 'left'
        self.situation      = {"hurt":0,"excited":0}
        self.jump           = 0
        self.kiss           = 0
        self.kiss_direction = 'left'
        self.kiss_rect      = ((0,0),(0,0))
        self.floor          = self.level.universe.floor - 186*scale
        self.last_height    = 186*scale
        self.action         = [None,'stay']
        self.image          = self.stay_img.left[self.stay_img.itnumber.next()]
        self.image_size     = self.image.get_size()
        self.inside         = INSIDE
        self.steps = [pygame.mixer.Sound('data/sounds/princess/steps/spike_heel/street/'+str(i)+'.ogg') for i in range(0,5)]
        self.jumpsound      = pygame.mixer.Sound('data/sounds/princess/pulo.ogg')
        self.channel1       = pygame.mixer.Channel(0)
        self.channel2       = pygame.mixer.Channel(1)
        self.channel3       = pygame.mixer.Channel(2)
        self.past_choice    = None

    def ordered_directory_list(self, action):
        odl = []
        cursor = self.level.universe.db_cursor
        row = cursor.execute("SELECT * FROM princess_garment WHERE id=(SELECT MAX(id) FROM princess_garment)").fetchone()
        print row
        for part in ["hair_back","skin","face","hair","shoes","dress","arm","armdress","accessory"]:
            if row[part] != 'None':
                name = part.replace('_','')
                odl.extend([str(self.directory+row[part]+"/"+action+"/")])
        return odl

    def update_all(self):
        if self.first_frame:
            if self.dirt > 0:
                self.level.princesses[1] = self.dirties[self.dirt -1]
        if not self.inside:
#            self.glamour_points += 1
            self.direction  = self.level.universe.dir
            self.action     = self.level.universe.action
            self.effects = []
            self.soundeffects(self.action)
            self.jumping(self.action)
            self.update_pos(self.action)
            self.hurting(self.action)
            self.kissing()
            if self.situation['hurt'] > 5:
                if self.situation['hurt']%2 == 0:
                    self.update_image(self.action,self.direction)
                else:
                    self.image = None
            else:
                self.update_image(self.action,self.direction)
        else:
            self.update_image(self.action,'right')

    def dirt_cloud_funciton(self):
        if 0 < self.situation['hurt'] < 24:
            if self.situation['hurt'] > len(self.dirt_cloud.left):
                dirt_cloud_image = (self.dirt_cloud.left[self.situation['hurt']-1-len(self.dirt_cloud.left)])
            else:
                dirt_cloud_image = (self.dirt_cloud.left[self.situation['hurt']-1])
            self.effects.append(Effect(dirt_cloud_image,(self.pos)))

    def jumping(self,action):
        feet_position = self.pos[1]+self.size[1]
        if action[0]!= 'jump' and action[0]!= 'jump2':
            self.jump = 0
        if feet_position == self.floor and not self.jump:
            if action[0]== 'jump':
                self.jump = 1
                self.channel3.play(self.jumpsound)
                self.images.number = 0
        if self.jump > 0 and self.jump <20:
            self.pos[1] -= 30*scale
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
        if feet_position < self.floor and not self.jump:
            action[0]='fall'

    def hurting(self,action):
        if not self.inside:
            if not self.situation['hurt']:
                for e in self.level.enemies:
                    if (e.__class__ in (enemy.Schnauzer , enemy.FootBall, enemy.Hawk) and self.rect.colliderect(e.rect)):
                        if self.dirt <= 2:
                            self.situation['hurt'] += 1
                            self.dirt += 1
                            self.save_cursor.execute("UPDATE save SET dirt = "+str(self.dirt)+" WHERE name = '"+self.name+"'")
                            print "Oh Dear, you've got all dirty! I need to take a record on that..."
                            self.level.princesses[1] = self.dirties[self.dirt -1]
                    if e.__class__ == enemy.Carriage:
                        if self.rect.colliderect(e.rect):
                            self.speed = 0
                        else:
                            self.speed = 10*scale
                    if e.__class__ == enemy.Butterfly:
                        if self.rect.colliderect(e.rect) and self.situation['excited'] == 0:
                            self.situation['excited']+=1
                if self.level.viking_ship:
                    if self.rect.colliderect(self.level.viking_ship.talk_balloon_rect):
                        if self.dirt <= 2:
                            self.situation['hurt'] += 1
                            self.dirt += 1
                            self.save_cursor.execute("UPDATE save SET dirt = "+str(self.dirt)+" WHERE name = '"+self.name+"'")
                            print "Oh Dear, you've got all dirty! I need to take a record on that..."
                            self.level.princesses[1] = self.dirties[self.dirt -1]

            else:
                self.situation['hurt'] +=1
                if self.situation['hurt'] == 30:
                    self.situation['hurt'] = 0
            if self.situation['excited']:
                self.situation['excited'] +=1
                action[0] = 'celebrate'
                if self.situation['excited'] == 60:
                    self.situation['excited'] = 0
            if self.situation['hurt'] and self.situation['hurt'] <6:
                action[0]='ouch'
                self.situation['excited'] =0
            if self.situation['hurt'] >=6:
                action[0]= None

    def kissing(self):
        if self.action[0] == 'kiss' or self.kiss > 0:
            self.kiss +=1
            if self.kiss == 1:
                self.kiss_img.number = 0
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
        last_height = self.level.what_is_my_height(self)
        self.floor = self.level.universe.floor - last_height
        self.pos[0] = self.level.universe.center_x+self.center_distance
        #fall
        if feet_position < self.floor:
            self.pos[1] += self.gforce
            if self.pos[1]+self.size[1] > self.floor:
                self.pos[1] = self.floor-self.size[1]         #do not fall beyond the floor
            self.gforce += self.g_acceleration
        #do not stay lower than floor
        if feet_position >= self.floor:
            self.pos[1]= self.floor-self.size[1]
        if feet_position == self.floor:
            self.gforce = 0
        if action[1]=='walk' and action[0] != 'celebrate':
            if self.direction == 'right':
                self.center_distance += self.speed
                next_height = self.level.what_is_my_height(self)
                if (self.level.universe.floor - next_height)  <= int(feet_position -(30*scale)):
                    self.center_distance -= self.speed
            else:
                self.center_distance -= self.speed
                next_height = self.level.what_is_my_height(self)
                if (self.level.universe.floor - next_height)  <= int(feet_position -(30*scale)):
                    self.center_distance += self.speed

    def soundeffects(self,action):
        if not self.jump and (self.pos[1]+self.size[1]) == self.floor:
            if action[1]=='walk' or action[0] == 'pos[0]celebrate':
                if self.images.number % 6 == 0:
                    self.channel1.play(self.steps[random.randint(0,1)])
                if (self.images.number + 3)% 6 == 0:
                    self.channel2.play(self.steps[random.randint(2,3)])

    def throwkiss(self):
        if self.kiss == 1:
            self.kiss_direction = self.direction
        if self.kiss_direction == 'right':
            kissimage = self.lips.left[self.kiss-1]
            self.effects.append(Effect(kissimage,(self.pos[0],self.pos[1])))
            self.kiss_rect = Rect((self.pos[0],self.pos[1]),((self.kiss)*44,self.size[1]))
        else:
            kissimage = self.lips.right[self.kiss-1]
            self.effects.append(Effect(kissimage,(self.pos[0]-(200*scale),self.pos[1])))
            self.kiss_rect = Rect((self.pos[0]-((self.kiss)*(44*scale)),self.pos[1]),((self.kiss)*(44*scale),self.size[1]))

    def update_image(self,action,direction):
        self.rect   = Rect(     (self.pos[0]+(self.image_size[0]/2),self.pos[1]-1),
                                self.size)
        chosen = action[0] or action[1]
        if direction == 'left':
            exec('self.images = self.'+chosen+'_img \n'+'actual_images = self.'+chosen+'_img.right')
        else:
            exec('self.images = self.'+chosen+'_img \n'+'actual_images = self.'+chosen+'_img.left')
        self.image = actual_images[self.images.number]
        if chosen != self.past_choice:
            exec('self.'+chosen+'_img.number = 0')
        self.past_choice = chosen
        if not self.jump:
            self.images.update_number()

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
        self.open_door = self.stay
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
            exec('self.'+chosen+'.number = 0')
        self.past_choice = chosen
        self.image = actual_images[self.images.number]
        if not self.level.princesses[0].jump:
            self.images.update_number()

class Effect():
    def __init__(self,image,position):
        self.image      = image
        self.position   = self.pos = position
