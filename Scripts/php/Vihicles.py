import pygame as pg , os
from PIL import Image

vihicles_types = os.listdir('Objects/Vihicles')

vihicles_file_name = 'txt/Objects/Vihicles.txt'
vihicles_file_mode = 'r'
vihicles_file = open (vihicles_file_name , vihicles_file_mode)
vihicles_file1 = vihicles_file.readlines()
vihicles_list = []
vihicles_images_list = []

class Vihicles:
    def __init__( self , x , y , image) :
        self.x = x
        self.y = y    
        self.image = image

for i in range( len ( vihicles_file1 ) ) :
    vihicles_images_list.append(pg.image.load('Objects/Vihicles/' + str(vihicles_types[i]) + '/0/0.png'))
    i = Vihicles(vihicles_file1[i].split(',')[0] , vihicles_file1[i].split(',')[1] , vihicles_images_list[i])
    vihicles_list.append(i)