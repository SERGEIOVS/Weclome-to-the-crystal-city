import pygame as pg
from Settings import *
from Items import *
from PIL import Image
from Items import *
import random
import os   

pg.font.init()
killed_units   = []
selected_units = []
item  = 3
items = 0

screen_file_name = 'txt/screen.txt' ; screen_file_mode = 'r' ; screen_file = open (screen_file_name , screen_file_mode) ; screen_file1 = screen_file.readlines()

items_max = 5
hero_file_name = 'txt/hero.txt';hero_file_mode = 'r' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file1 = hero_file.readlines() ; hero_file.close()

items_stack = 100
hero_inventory_images = []

for i in screen_file1:
    screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]

max_inentory_size = 10

pistol_mags     = int(hero_file1[0])
max_pistol_mags = int(hero_file1[0])
pistol_ammo     = int(hero_file1[0])
pistol_max_ammo = int(hero_file1[0])

mags     = pistol_mags
ammo     =  pistol_ammo
max_ammo =  pistol_max_ammo

energy =  int(hero_file1[4])
name   = 2
state  = 'idle'
turn   = 'left'
animation  = 0
hero_speed = 3
health , max_health = hero_file1[1] , hero_file1[1]
armor  , max_armor = hero_file1[1] , hero_file1[2]
radiation     = hero_file1[3]
max_radiation = hero_file1[4]
hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
hero_night_vision   = 0
hero_skills = [ 'fast run' , 'night_vision']

hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
hero_money = 1000
currency = 'coins'

big_font   = pg.font.Font( None , 30)
small_font = pg.font.Font( None , 15)

unit_state    = 'idle'
unit_types    = os.listdir('Objects/Characters/')
unit_category = 'Citizens'
player_types  = os.listdir('Objects/Characters/Players/')

show_hero_armor = big_font.render(str( armor ).strip() + " / " +  str( max_armor ).strip() , False , ( 250 , 0 , 0 ) )
show_ammo       = big_font.render(str(ammo ).strip() + " / " + str( max_ammo * mags ).strip() , False , ( 250 , 0 , 0 ) )
show_health     = big_font.render( str( health ).strip() + " / " + str( max_health ).strip() , False , ( 255 , 0 , 0 ) )
show_radiation  = big_font.render( str( radiation ).strip() + " / " + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) )
show_energy     = big_font.render( str( energy).strip() + ' / ' + str(energy).strip() , False , ( 255 , 0 , 0 ) )

Companions_file_name = 'txt/Objects/Companions.txt' ; Companions_file_mode = 'r' ; Companions_file = open (Companions_file_name , Companions_file_mode) ; Companions_file1 = Companions_file.readlines() ; Companions_list = [] ; Companions_images_list = []

players_file_name = 'txt/Objects/Players.txt' ; players_file_mode = 'r' ; players_file = open (players_file_name , players_file_mode) ; players_file1 = players_file.readlines() ; players_list = [] ; players_images_list = []

Enemies_file_name = 'txt/Objects/Enemies.txt' ; Enemies_file_mode = 'r' ; Enemies_file = open (Enemies_file_name , Enemies_file_mode) ; Enemies_file1 = Enemies_file.readlines() ; Enemies_list = [] ; Enemies_images_list = []

nicknames_file_name = 'txt/nicknames.txt' ; nicknamesfile_mode = 'r' ;nicknames_file = open (nicknames_file_name , nicknamesfile_mode) ; nicknames_file1 = nicknames_file.readlines() ; nicknameslist = []

unit_animation = 0
unit_image = pg.image.load('Objects/Characters/Players/' + '2' + '/' + str(state) + '/left/' + str(unit_animation) + '.png')
Companions_routes = []
Companion_welcome_speech = []
Enemies_routes = []

class Companions:
    def __init__( self , x , y , image , state , damage , inventory , route , loot ):
        self.x = x
        self.y = y    
        self.image = image
        self.state = state
        self.damage = damage
        self.inventory = inventory
        self.route = route
        self.loot = loot

for i in range( len ( Companions_file1 ) ) :
    Companions_images_list.append(pg.image.load('Objects/Characters/' + str(unit_types[0]) + '/' +str(unit_category) + '/0/left/' + str(animation) + '.png'))
    Companions_routes.append(1_000)
    i = Companions(Companions_file1[i].split(',')[0] , Companions_file1[i].split(',')[1] , Companions_images_list[i] , 'idle' ,'2', [] , '2' , 'Companion_loot')
    i.inventory.append(items_categories[0])
    i.loot = i.inventory[0]
    Companions_list.append( i )

class Players:
    def __init__( self , x , y , image ,state , damage , inventory , loot) :
        self.x = x
        self.y = y    
        self.image = image
        self.state = state
        self.damage = damage
        self.inventory = inventory
        self.loot = loot

for i in range( len ( players_file1 ) ) :
    i = Players( players_file1[i].split(',')[0] , players_file1[i].split(',')[1] , unit_image , 'idle' , 2 , [] , 'player_loot')
    i.inventory.append('pistol')
    i.inventory.append('medkit')
    i.inventory.append('flashlight')
    i.loot = i.inventory[0]
    players_list.append( i )


class Enemies:
    def __init__( self , x , y , image , state , damage , inventory , route , loot ):
        self.x = x
        self.y = y    
        self.image = image
        self.state = state
        self.damage = damage
        self.inventory = inventory
        self.route = route
        self.loot = loot

for i in range( len ( Enemies_file1 ) ) :
    Enemies_images_list.append(pg.image.load('Objects/Characters/Enemies/Mutants/0/left/0.png'))
    Enemies_routes.append(1_000)
    i = Enemies(Enemies_file1[i].split(',')[0] , Enemies_file1[i].split(',')[1] , Enemies_images_list[i] , 'idle' , '2' , [] , '2' , 'Enemies_loot')
    i.inventory.append(items_categories[0])
    i.loot = i.inventory[0]
    Enemies_list.append( i )