import pygame as pg
from PIL import Image
import os
from Settings import *
import math

class Background:
    def __init__(self , x , y , image) :
        self.x = x
        self.y = y
        self.image = image

for i in range(len(islands_file1)) : islands_images.append(pg.image.load('Objects/Background/islands/0/0.png'))
i = Background( islands_file1[i].split(',')[0] , islands_file1[i].split(',')[1] , islands_images[0] )
islands_list.append( i )

BGcolor   = colors[0] ; minimapBGcolor = colors[0]
screen.fill((BGcolor))

buildings_list = []
buildings_file_name ='txt/Objects/'+ str(saving_type) + '/Buildings.txt'
buildings_file_mode = 'r'
buildings_file  = open (buildings_file_name , buildings_file_mode)
buildings_file1 = buildings_file.readlines()

Buildings_images_list = []
buildings_types = os.listdir('Objects/Background/Buildings/')
Buildings_categories  = []

Sea_width = 300

class Buildings:
    def __init__( self , x , y , image , category , rooms) :
        self.x = x
        self.y = y    
        self.image = image
        self.category = category
        self.rooms = rooms

for i in range( len ( buildings_file1 ) ) :
    Buildings_images_list.append(pg.image.load('Objects/Background/Buildings/' + str(buildings_types[i]) + '/0/0.png'))
    i = Buildings(buildings_file1[i].split(',')[0] , buildings_file1[i].split(',')[1] , Buildings_images_list[i] , buildings_types[i] , 1)
    buildings_list.append(i)

Plants_list = []
Plants_file_name ='txt/Objects/'+ str(saving_type) + '/Buildings.txt'
Plants_file_mode = 'r'
Plants_file  = open (buildings_file_name , buildings_file_mode)
Plants_file1 = buildings_file.readlines()

Plants_images_list = []
Plants_types = os.listdir('Objects/Background/Buildings/')
Plants_categories  = []

class Plants:
    def __init__( self , x , y , image , category) :
        self.x = x
        self.y = y    
        self.image = image
        self.category = category

for i in range( len ( Plants_file1 ) ) :
    Plants_images_list.append(pg.image.load('Objects/Background/Plants/' + str(Plants_types[i]) + '/0/0.png'))
    i = Plants(Plants_file1[i].split(',')[0] , Plants_file1[i].split(',')[1] , Plants_images_list[i] , Plants_types[i])
    Plants_list.append(i)

    import pygame as pg , os ; from Settings import * ;
from PIL import Image
saving_type = 'Default' ; game_state = 'Main menu'

Furniture_types = os.listdir('Objects/Background/Furniture/')

Furniture_file_name = 'txt/Objects/' + str(saving_type) + '/Furniture.txt'
Furniture_file_mode = 'r'
Furniture_file  = open (Furniture_file_name , Furniture_file_mode)
Furniture_file1 = Furniture_file.readlines()
Furniture_list  = []
Furniture_images_list = []

class Furniture:
    def __init__( self , x , y , image , state , damage , inventory , route , loot) :
        self.x         = x
        self.y         = y    
        self.image     = image
        self.state     = state
        self.damage    = damage
        self.inventory = inventory
        self.route     = route
        self.loot      = loot

for i in range( len ( Furniture_file1 ) ) :
    Furniture_images_list.append(pg.image.load('Objects/Background/Furniture/' + str(Furniture_types[i]) + '/0/0.png'))
    i = Furniture(Furniture_file1[i].split(',')[0] , Furniture_file1[i].split(',')[1] , Furniture_images_list[i] , 'idle' , '2' , [] , '2' , 'Companion_loot')
    Furniture_list.append(i)