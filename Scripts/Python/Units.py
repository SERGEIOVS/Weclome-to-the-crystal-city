import pygame as pg ; from Items import * ; from PIL import Image ; from Items import * ; import random ; import os ; import sys
from Settings import * ; pg.font.init()
saving_type = 'Default' ; game_state = 'Main menu'

item = 0 ; items = 0 ; items_max = 6 ; items_stack = 100

screen_file_name = 'txt/screen.txt' ; screen_file_mode = 'r' ; screen_file = open (screen_file_name , screen_file_mode) ; screen_file1 = screen_file.readlines()
hero_file_name = 'txt/Objects/' + str(saving_type) + '/Hero.txt'   ; hero_file_mode = 'r' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file1 = hero_file.readlines() ; hero_file.close()
hero_belt_inventory_images = []
hero_backpack_inventory_images = []

for i in screen_file1 : screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]

name = 2 ; state = 'idle' ; turn = 'left' ; animation = 0 ; hero_speed = 3
ammo_used = 0
health , max_health         = int(hero_file1[0].split(',')[0]) , int(hero_file1[0].split(',')[0])
armor  , max_armor          = int(hero_file1[0].split(',')[1]) , int(hero_file1[0].split(',')[1])
radiation , max_radiation   = int(hero_file1[0].split(',')[2]) , int(hero_file1[0].split(',')[2])
energy , max_energy         = int(hero_file1[0].split(',')[3]) , int(hero_file1[0].split(',')[3]) 
hero_damage = 5
pistol_mags , max_pistol_mags = 3 , 3 ; pistol_ammo , pistol_max_ammo  = int(hero_file1[0].split(',')[4]) , int(hero_file1[0].split(',')[4]) ; mags = pistol_mags ; ammo , max_ammo = pistol_ammo , pistol_max_ammo

hero_night_vision   = 0
hero_skills         = [ 'fast run' , 'night vision']
hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
hero                = 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
hero_image          = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png') ; heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
hero_x , hero_y     = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
hero_money_used = 0 
hero_money = 1000 - hero_money_used ; currency = 'Coins'

Hero_types = os.listdir('Objects/Characters/Hero/')
Hero_types_list = []

big_font   = pg.font.Font( None , 30) ; small_font = pg.font.Font( None , 15)
show_hero_armor = big_font.render( str( armor     ).strip() + " / " + str( max_armor       ).strip() , False , ( 250 , 0 , 0 ) ) ; show_ammo    = big_font.render( str( ammo  ).strip()     + " / " + str( max_ammo * mags ).strip() , False , ( 250 , 0 , 0 ) ) ; show_health = big_font.render( str( health ).strip()    + " / " + str( max_health).strip() , False , ( 255 , 0 , 0 ) )
show_radiation  = big_font.render( str( radiation ).strip() + " / " + str( max_radiation   ).strip() , False , ( 255 , 0 , 0 ) ) ; show_energy  = big_font.render( str( energy).strip()     + ' / ' + str( max_energy      ).strip() , False , ( 255 , 0 , 0 ) )
nicknames_file_name = 'txt/nicknames.txt' ; nicknamesfile_mode = 'r' ; nicknames_file = open (nicknames_file_name , nicknamesfile_mode) ; nicknames_file1 = nicknames_file.readlines() ; nicknameslist = []

Companions_class_values = ['x','y','image']

class Companions:
    def __init__(self , x  , y , image ):
        self.x         = x
        self.y         = y    
        self.image     = image

Companions_file_name = 'txt/Objects/' + str(saving_type) + '/Companions.txt' ; 
Companions_file_mode = 'r' ; 
Companions_file = open (Companions_file_name , Companions_file_mode) ; 
Companions_file1 = Companions_file.readlines() ; 
Companion_state = 'idle' ; 
Companion_turn =  'left' ; 
Companion_types = os.listdir('Objects/Characters/Companions/') ; 
Companion_animation = 0 ; 
Companions_images_list   = [] ; 
Companions_routes = [] ; 
Companion__speech = [] ; 
Companions_list = []
Companions_inventory = []

for i in range( len ( Companions_file1 ) ) :
    Companions_images_list.append(pg.image.load('Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/' + str(Companion_animation) + '.png'))
    Companion_image = Companions_images_list[Companion_animation]
    Companions_inventory.append([])
    Companions_inventory[i].append('123')
    i = Companions(Companions_file1[i].split(',')[0] , Companions_file1[i].split(',')[1] , Companions_images_list[Companion_animation])
    Companions_list.append( i )

class Players:
    def __init__( self ,x,y,image) :
        self.x         = x
        self.y         = y    
        self.image     = image

players_file_name    = 'txt/Objects/' + str(saving_type) + '/Players.txt'
players_file_mode    = 'r' ; 
players_file         = open (players_file_name , players_file_mode) ; 
players_file1        = players_file.readlines() ; 
player_state         = 'idle' ; 
player_turn          = 'left' ; 
player_types         = os.listdir('Objects/Characters/Players/') ; 
player_animation     = 0 ; 
players_images_list  = [] ; 
Players_routes       = [] ; 
Players_speech   = [] ; 
players_list         = []
players_inventory    = []

for i in range(len(players_file1 )) :
    players_images_list.append(pg.image.load('Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/' + str(player_turn) + '/' + str(player_animation) + '.png'))
    player_image = players_images_list[player_animation]
    players_inventory.append([])
    players_inventory[i].append('123')
    i = Players( players_file1[i].split(',')[0] , players_file1[i].split(',')[1] , players_images_list[player_animation])
    players_list.append(i)

class Enemies:
    def __init__( self , x , y , image):
        self.x         = x
        self.y         = y    
        self.image     = image

Enemies_file_name  = 'txt/Objects/' + str(saving_type) + '/Enemies.txt'
Enemies_file_mode  = 'r' ; Enemies_file    = open (Enemies_file_name    , Enemies_file_mode)
Enemies_file1      =  Enemies_file.readlines()
enemy_state        = 'idle' ; enemy_turn     = 'left'
enemy_types        = os.listdir('Objects/Characters/Enemies/')
Enemy_animation    = 0  ; Enemies_images_list  = []
Enemies_routes     = [] ; Enemy_speech = []
Enemies_list       = []
Enemies_inventory  = []

for i in range(len(Enemies_file1)) :
    Enemies_images_list.append(pg.image.load('Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/' + str(Enemy_animation) + '.png'))
    Enemy_image = Enemies_images_list[Enemy_animation]
    Enemies_inventory.append([])
    Enemies_inventory[i].append('123')
    i = Enemies(Enemies_file1[i].split(',')[0] , Enemies_file1[i].split(',')[1] , Enemies_images_list[Enemy_animation])
    Enemies_list.append(i)

killed_units        = []
selected_units      = []
unit_with_a_quest   = 0
units_with_a_quests = [Companions_images_list[0]]