#!/usr/bin/env python

from getscreen import *
from globals import *
from pygame.locals import *
pygame.mixer.init()
import random
from sys import exit
from math import *
from random import randint
from stage import *
from game_clock import *
import obj_images
from numpy import uint8
import camera
import mousepointer
import menu
import universe



#Create lists

action = [None, 'stay']
clock = pygame.time.Clock()
dir = None
count = 0
universe = universe.Universe(os_screen.current_w,os_screen.current_h)


level = 'menu'
gamemenu = menu.MenuScreen((360,200))
mainmenu = menu.Menu(gamemenu,level)
mainmenu.instantiate_stuff()

screen_surface = pygame.display.set_mode((os_screen.current_w,os_screen.current_h),FULLSCREEN,32)

while True:

    ######## New Game Menu #######
    while level == 'menu':
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_i:
                    level = 'choose'
                elif event.key == K_e:
                    level = 'choose'
                elif event.key == K_a:
                    level = 'choose'

        gamemenu.update_all(screen_surface)


        if gamemenu.ready:
            pygame.display.update((0,0),(900,900))
        else:
            pygame.display.flip()
            once = True

    ####### Select your Princess Menu #######
    while level == 'choose':
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_i:
                    level = 'bathhouse_st'
                elif event.key == K_e:
                    level = 'dress_st'
                elif event.key == K_a:
                    level = 'accessory_st'
        gamemenu.update_choose(screen_surface)
        try:
            if once:
                pygame.display.update()
        except:
            pygame.display.flip()
            once = True

    if level == 'bathhouse_st':
        actual_level = BathhouseSt(1,6000,universe,'bathhouse_st/')
    if level == 'dress_st':
        actual_level = DressSt(1,6000,universe,'dress_st/')
    if level == 'accessory_st':
        actual_level = AccessorySt(1,6000,universe,'accessory_st/')

    game_clock = GameClock(actual_level)
    clock_pointer = ClockPointer(actual_level)


    actual_level.instantiate_stuff(clock_pointer)

    mouse_pos  = pygame.mouse.get_pos()
    game_mouse = mousepointer.MousePointer(mouse_pos,actual_level)
    gamecamera = camera.GameCamera(actual_level)

    run_level = True


    pygame.mouse.set_visible(0)

    while run_level:
        for i in actual_level.gates:
            if i.change_level:
                level = i.level
                mainmenu.level = i.level
                run_level = False
                i.change_level = False
                break
        for event in pygame.event.get():
            if event.type == QUIT:
                actual_level.princess.save()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    actual_level.princess.save()
                    exit()
                if event.key == K_LEFT:
                    dir = 'left'
                    action[1] = 'walk'
                if event.key == K_RIGHT:
                    dir = 'right'
                    action[1] = 'walk'
                if event.key == K_LCTRL:
                    action[0] = 'kiss'
                if event.key == K_SPACE:
                    action[0] = 'jump'
                if event.key == K_UP:
                    if actual_level.princess.jump == 0:
                        action[0] ='open_door'
                if event.key == K_y:
                    action[0]='celebrate'
                if event.key == K_c:
                    action[0] = 'change'
                if event.key == K_i:
                    action[0] = 'changedress'
                if event.key == K_h:
                    action[0] = 'changehair'
                if event.key == K_x:
                    action[0] = 'changehair2'
                if event.key == K_s:
                    action[0] = 'changeshoes'
                if event.key == K_p:
                    action[0] = 'changeskin'
            elif event.type == KEYUP:
                action[0]=None
                actual_level.princess.doonce = False
                if (dir == 'left' and event.key == K_LEFT) or (dir == 'right' and event.key == K_RIGHT):
                    action[1] = 'stay'

        game_mouse.update()

        time_passed = clock.tick(30)

        screen_surface.fill([255,255,255])

        actual_level.update_all(screen_surface,action,dir,universe,clock_pointer)

        clock_pointer.update_image()
        pygame.display.flip()


    screen_surface.fill([0,0,0])
    pygame.display.flip()
    run_level = True

    for attr,value in level.__dict__.iteritems():
        exec('level.'+attr+'= None')

    del level
    level = 'menu'
