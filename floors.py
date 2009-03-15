
import globals
import obj_images


class Floor():
    images = None
    def __init__(self,index,dir,level,height={'all':186},type='standard'):
        if self.images == None:
            self.images = obj_images.OneSided(dir)
        self.image_number = 0
        self.image_list = self.images.list
        self.image = self.image_list[self.image_number]
        self.size = self.image.get_size()
        self.center_distance = (self.size[0]*(index))
        self.type = type
        level.floor_image.insert(index,self)
        self.pos = (globals.universe.center_x+(self.center_distance),globals.universe.floor-self.size[1])
    def update_pos(self):
        self.image_number += 1
        if self.image_number > len(self.image_list)-1:
            self.image_number = 0
        self.image = self.image_list[self.image_number]
        self.pos = (globals.universe.center_x+(self.center_distance),globals.universe.floor-self.size[1])
class Bridge():
    def __init__(self,directory,index,level,main=True):
        if main == True:    self.images = obj_images.OneSided(directory+'bridge/')
        else:               self.images = obj_images.OneSided(directory) 

        if main == True:
            self.left_bank = Bridge(str(directory)+'left_bank/',index-1,level,main = False)
            self.right_bank= Bridge(str(directory)+'right_bank/',index+1,level,main = False)

        self.image_number = 0
        self.image = self.images.list[0]
        self.size = self.image.get_size()

        if main == True:    self.center_distance = (400*(index))-400
        else:               self.center_distance = (400*(index))

        self.pos = (globals.universe.center_x+(self.center_distance),globals.universe.floor-self.size[1])
        if main == True:
            del level.floor_image[index]
            level.floor_image.insert(0,self)
        else:
            level.floor_image[index]= self

    def update_pos(self):
        self.image_number += 1
        if self.image_number > len(self.images.list)-1:
            self.image_number = 0
        self.image = self.images.list[self.image_number]
        
        self.pos = (globals.universe.center_x+(self.center_distance),globals.universe.floor-self.size[1])
