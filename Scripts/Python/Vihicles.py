import pygame as pg , os
from PIL import Image
saving_type = 'Default' ; game_state = 'Main menu'

Land_vihicles_types = os.listdir('Objects/Vihicles/')
Land_vihicles_file_name = 'txt/Objects/' + str(saving_type) + '/Land_Vihicles.txt'
Land_vihicles_file_mode = 'r'
Land_vihicles_file = open (Land_vihicles_file_name , Land_vihicles_file_mode)
Land_vihicles_file1 = Land_vihicles_file.readlines()
Land_vihicles_list = []
Land_vihicles_images_list = []

class Land_Vihicles:
    def __init__( self , x , y , image,state,damage,inventory,route,loot) :
        self.x         = x
        self.y         = y    
        self.image     = image
        self.state     = state
        self.damage    = damage
        self.inventory = inventory
        self.route     = route
        self.loot      = loot

for i in range( len ( Land_vihicles_file1 ) ) :
    Land_vihicles_images_list.append(pg.image.load('Objects/Vihicles/' + str(Land_vihicles_types[i]) + '/0/0.png'))
    i = Land_Vihicles(Land_vihicles_file1[i].split(',')[0] , Land_vihicles_file1[i].split(',')[1] , Land_vihicles_images_list[i] , 'idle' ,'2', [] , '2' , 'Companion_loot')
    Land_vihicles_list.append(i)

vihicles_types = os.listdir('Objects/Vihicles/')
vihicles_file_name = 'txt/Objects/' + str(saving_type) + '/Vihicles.txt'
vihicles_file_mode = 'r'
vihicles_file = open (vihicles_file_name , vihicles_file_mode)
vihicles_file1 = vihicles_file.readlines()
vihicles_list = []
vihicles_images_list = []

class Air_Vihicles:
    def __init__( self , x , y , image,state,damage,inventory,route,loot) :
        self.x         = x
        self.y         = y    
        self.image     = image
        self.state     = state
        self.damage    = damage
        self.inventory = inventory
        self.route     = route
        self.loot      = loot

for i in range( len ( vihicles_file1 ) ) :
    vihicles_images_list.append(pg.image.load('Objects/Vihicles/' + str(vihicles_types[i]) + '/0/0.png'))
    i = Air_Vihicles(vihicles_file1[i].split(',')[0] , vihicles_file1[i].split(',')[1] , vihicles_images_list[i] , 'idle' ,'2', [] , '2' , 'Companion_loot')
    vihicles_list.append(i)