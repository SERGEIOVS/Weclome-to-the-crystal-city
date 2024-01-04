import pygame as pg
from PIL import Image
import os
from Settings import *
import math

buildings_list = []
buildings_file_name ='txt/Objects/Buildings.txt'
buildings_file_mode = 'r'
buildings_file = open (buildings_file_name , buildings_file_mode)
buildings_file1 = buildings_file.readlines()
Buildings_images_list = []
buildings_types = []
Buildings_categories = []
Buildings_images_list = []

class Buildings:
    def __init__( self , x , y , image , category , rooms) :
        self.x = x
        self.y = y    
        self.image = image
        self.category = category
        self.rooms = rooms

for i in range( len ( buildings_file1 ) ) :
    Buildings_images_list.append(pg.image.load('Objects/Buildings/abandoned/0/0.png'))
    i = Buildings(buildings_file1[i].split(',')[0] , buildings_file1[i].split(',')[1] , Buildings_images_list[i] , 'house' , 1)
    buildings_list.append( i )