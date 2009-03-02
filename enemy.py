
from globals import *

class Enemy():
    """This class defines an enemy with no movement and no update to position or image. It is used to be extended by other classes of enemies that should define the functions for movements"""
    def __init__(self,speed,directory, pos, level,walk_margin=[10,10,10,10],stay_margin=[10,10,10,10],kissed_margin=[10,10,10,10],dirty=False):
        self.distance_from_center = pos
        try:        self.walk = ObjectImages(directory+'/walk/',walk_margin)
        except:     pass 
        try:        self.stay = ObjectImages(directory+'/stay/',stay_margin)
        except:     pass
        try:        self.kissed = ObjectImages(directory+'/kissed/',kissed_margin)
        except:     pass
        try:        self.image = self.walk.left[0]
        except:     self.image = self.stay.left[0]

        self.size = (self.image.get_width()/2, self.image.get_height())
        self.alive = True
        self.level = level
        self.speed = speed
        self.floor = universe.floor-self.level[0].what_is_my_height(self)
        self.margin = walk_margin
        self.pos = (universe.center_x+self.distance_from_center,self.floor+self.margin[2]-(self.size[1]))

        self.decide = False
        self.count = 0
        self.move = True
        self.direction = 'left'
        self.lookside = 0
        enemies.append(self)
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),(level[0].floor-self.pos[1])),(self.size))
        self.gotkissed = False
        self.image_number = 0
        self.dirty = dirty

        for i in level:
            i.enemies.append(self)

class Schnauzer(Enemy):
    bow = pygame.mixer.Sound('data/sounds/enemies/dog1.ogg')
    def barf(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.bow.play()
    def movement(self,princess):
        self.look_around(princess)
        self.set_pos()
        self.set_image()
    def look_around(self,princess):
        self.count +=1
        if self.count > 130:
            self.move = False
        if self.move == False:
            if princess.pos[0] > self.pos[0]:
                self.direction='right'
            else:
                self.direction = 'left'
            if self.count % 2 == 1:
                self.lookside += 1
            if self.lookside == 6:
                self.move = True
                self.lookside = 0
                self.count = 0
        #self.gotkissed = True
    def got_kissed(self):
        self.gotkissed == True
    def set_pos(self):
        self.floor = universe.floor-self.level[0].what_is_my_height(self)
        self.pos = (universe.center_x + self.distance_from_center, self.floor+self.margin[2]-(self.size[1]))

        if self.move == True:
            if self.direction == 'right' :
                self.distance_from_center += self.speed
            else:
                self.distance_from_center -= self.speed
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),self.pos[1]),(self.size))
    def set_image(self):
        #choose list
        if self.move == True:
            if self.direction == 'right':
                actual_list = self.walk.right
            else:
                actual_list = self.walk.left
        else:
            if self.lookside % 2 ==0:
                actual_list = self.walk.right[0:1]
            else:
                actual_list = self.walk.left[0:1]
        if self.gotkissed == True:
            self.move =False
            if self.direction == 'right':
                actual_list = self.kissed.right
            else:
                actual_list = self.kissed.left        
        number_of_files = len(actual_list)-2
        if self.image_number <= number_of_files:
            self.image_number +=1
        else:
            self.image_number = 0
        
        self.image = actual_list[self.image_number]
class Carriage(Enemy):
    def movement(self,princess):
        self.set_pos()
        self.set_image()
    def set_pos(self):
        self.floor = universe.floor-self.level[0].what_is_my_height(self)
        self.pos = (universe.center_x + self.distance_from_center, self.floor+self.margin[2]-(self.size[1]))

        if self.move == True:
            if self.direction == 'right' :
                self.distance_from_center += self.speed
            else:
                self.distance_from_center -= self.speed
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),(self.level[0].floor-self.size[1])),(self.size))
    def set_image(self):
#choose list
        if self.move == True:
            if self.direction == 'right':
                actual_list = self.walk.right
            else:
                actual_list = self.walk.left
        else:
            if self.direction == 'right':
                actual_list = self.stay.right
            else:
                actual_list = self.stay.left  
  

        number_of_files = len(actual_list)-2
        if self.image_number <= number_of_files:
            self.image_number +=1
        else:
            self.image_number = 0
        self.image = actual_list[self.image_number]
class Butterfly(Enemy):
    height = 100
    up_direction = 'going_down'
    def movement(self,princess):
        self.set_pos()
        self.set_image()
    def set_pos(self):
        
        if self.pos[1] < 300:
            self.up_direction = 'going_down'
        elif self.pos[1] > 500:
            self.up_direction = 'going_up'


        if self.up_direction == 'going_down':
            self.height += 5
        if self.up_direction == 'going_up':
            self.height -= 5 
        self.pos = (universe.center_x + self.distance_from_center, self.height)
        if self.move == True:
            if self.direction == 'right' :
                self.distance_from_center += self.speed
            else:
                self.distance_from_center -= self.speed
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),self.height),(self.size))
    def set_image(self):
#choose list
        self.count+=1
        if self.move == True:
            if self.direction == 'right':
                actual_list = self.walk.right
            else:
                actual_list = self.walk.left
        else:
            if self.direction == 'right':
                actual_list = self.stay.right
            else:
                actual_list = self.stay.left    
    
        number_of_files = len(actual_list)-2
        #if self.count%2==0:
        if self.image_number <= number_of_files:
            self.image_number +=1
        else:
            self.image_number = 0
        self.image = actual_list[self.image_number]
class OldLady(Enemy):
    def __init__(self,speed,directory, pos, level,walk_margin=[10,10,10,10],stay_margin=[10,10,10,10],kissed_margin=[10,10,10,10],dirty=False):
        self.distance_from_center = pos
        self.walk = ObjectImages(directory+'/walk/',walk_margin)
        self.hover = ObjectImages(directory+'/hover/',stay_margin)
        self.hover_inv_left = list(reversed(self.hover.left))
        self.hover_inv_right = list(reversed(self.hover.right))
        self.hover.left +=  self.hover_inv_left
        self.hover.right += self.hover_inv_right
        self.image = self.walk.left[0]
        self.mouseovercount = 0
        self.size = (self.image.get_width()/2, self.image.get_height())
        self.alive = True
        self.level = level
        self.speed = speed
        self.floor = universe.floor-self.level[0].what_is_my_height(self)
        self.margin = walk_margin
        self.pos = (universe.center_x+self.distance_from_center,self.floor+self.margin[2]-(self.size[1]))
        self.decide = False
        self.count = 0
        self.move = True
        self.direction = 'left'
        self.lookside = 0
        enemies.append(self)
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),(level[0].floor-self.pos[1])),(self.size))
        self.gotkissed = False
        self.image_number = 0
        self.dirty = dirty

        for i in level:
            i.enemies.append(self)


    def movement(self,princess):
        self.set_pos()
        self.set_image()
#        if self.rect.collidepoint(mouse_pos):


#        else:
#            self.set_pos()
#            self.set_image()
##            mouse_pos = pygame.mouse.get_pos()
#        if self.rect.collidepoint(mouse_pos):
#            self.bow.play()

    def set_pos(self):
        if self.mouseovercount == 0:
            self.move = True
        else:
            self.move = False
            if self.mouseovercount > 17:
                self.mouseovercount = 0

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.mouseovercount += 1
        else:
            self.mouseovercount = 0

        self.floor = universe.floor-self.level[0].what_is_my_height(self)
        self.pos = (universe.center_x + self.distance_from_center, self.floor+self.margin[2]-(self.size[1]))
        if self.move == True:
            if self.direction == 'right' :
                self.distance_from_center += self.speed
            else:
                self.distance_from_center -= self.speed
        self.rect = Rect(((self.pos[0]+(self.size[0]/2)),(self.level[0].floor-self.size[1])),(self.size))
    def set_image(self):
#choose list
        if self.move == True:
            if self.direction == 'right':
                actual_list = self.walk.right
            else:
                actual_list = self.walk.left
        else:
            if self.direction == 'right':
                actual_list = self.hover.right
            else:
                actual_list = self.hover.left  
  

        number_of_files = len(actual_list)-2
        if self.image_number <= number_of_files:
            self.image_number +=1
        else:
            self.image_number = 0
        self.image = actual_list[self.image_number]
