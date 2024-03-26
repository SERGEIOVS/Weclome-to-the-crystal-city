import os,pygame as pg

New_items_list = []
New_items_file_name = 'txt/Newitems.txt'
New_items_file_mode = 'r'
New_items_file = open (New_items_file_name , New_items_file_mode)
New_items_file1 = New_items_file.readlines()
New_items_images = []
New_items_categories = os.listdir('Objects/NewItems/')

class New_Items:
    def __init__( self , x , y , image) :
        self.x     = x
        self.y     = y
        self.image = image

for i in range( len ( New_items_file1 ) ) :
    New_items_images.append(pg.image.load('Objects/NewItems/' + str(New_items_categories[i]) + '/0/0.png'))
    i = New_Items( New_items_file1[i].split(',')[0] , New_items_file1[i].split(',')[1] , New_items_images[i])
    New_items_list.append( i )


