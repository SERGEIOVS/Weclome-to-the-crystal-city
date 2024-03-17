import pygame as pg , os
from Settings import *
saving_type = 'Default' ; game_state = 'Main menu'

items_list = []
items_file_name = 'txt/Objects/' + str(saving_type) + '/Items.txt'
items_file_mode = 'r'
items_file = open (items_file_name , items_file_mode)
items_file1 = items_file.readlines()
items_images = []
items_categories = os.listdir('Objects/Items/')

class Items:
    def __init__( self , x , y , image) :
        self.x     = x
        self.y     = y
        self.image = image

for i in range( len ( items_file1 ) ) :
    items_images.append(pg.image.load('Objects/Items/' + str(items_categories[i]) + '/0/0.png'))
    i = Items( items_file1[i].split(',')[0] , items_file1[i].split(',')[1] , items_images[i])
    items_list.append( i )