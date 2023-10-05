import pygame as pg , os

items_file_name = 'txt/Objects/items.txt' ; items_file_mode = 'r' ; items_file = open (items_file_name , items_file_mode) ; items_file1 = items_file.readlines()

items_list = []
items_images_list = []
items_categories = os.listdir('Objects/Items/')
item_states = []

class Items:
    def __init__( self , x , y , image , pickedup ) :
        self.x     = x
        self.y     = y
        self.image = image
        self.pickedup = pickedup

for i in range( len ( items_file1 ) ) :
    items_images_list.append(pg.image.load('Objects/Items/' + str(items_categories[i]) + '/0/0.png'))
    item_states.append(0)
    i = Items( items_file1[i].split(',')[0] , items_file1[i].split(',')[1] , items_images_list[i] , item_states[i])
    items_list.append( i )