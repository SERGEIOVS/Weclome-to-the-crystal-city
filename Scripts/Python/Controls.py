import sys
mods_dir_path = 'mods'
if mods_dir_path not in sys.path :print('no mods') ; sys.path.append(mods_dir_path);print(sys.path)
import os
import pygame as pg ; from Settings import * ; from PIL import Image ; from Units import * ; import logging ; from Vihicles import * ; import pyautogui ;
from Background import * ; import math
import time ; from Funcs import * ; from Settings import * ; from Items import *
import pprint

print(sys.path)
if mods_dir_path in sys.path : print() ; print() ; print('mods folder added ! ') ; print(os.listdir(mods_dir_path)) ; print() ; print()
pg.init()

pressed = pg.mouse.get_pressed() ; pos = pg.mouse.get_pos() ; clock = pg.time.Clock() ; FPS = 60 ; clock.tick(FPS)
hide_nicknames = 0 ; ground = 1 ; floor = 0 ; keys = pg.key.get_pressed()
fuel_bar_width = 100
minimapfontsize = int( 30 / map_scale)
mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 

custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint' , False , small_font_color ) 

interface_images = []

game_modes  = ['Survival' , 'God mode' , 'Hardcore'] ; game_modes1 = [] ; game_mode_num = 0 ; game_mode = game_modes[game_mode_num]
for i in range(len(game_modes)) : i = big_font.render(game_modes[i].split(',')[0].strip() , False , small_font_color ) ; game_modes1.append(i)     

menu_titles = ['Backpack' , 'Crafting' , 'Quests'] ; menu_titles1 = [] ; menu_title_num = 0 ; menu_title = menu_titles[menu_title_num]
for i in range(len(menu_titles)) : i = small_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)     

difficulties = ['Peaceful' , 'Easy' , 'Normal' , 'Hard'] ; difficulties1   = [] ; difficulty_num  = 0 ; difficulty = difficulties[difficulty_num]
for i in range(len(difficulties)) : i = big_font.render(difficulties[i].split(',')[0].strip() , False , small_font_color ) ; difficulties1.append(i)     

necessary_craft_items = [] ; prices_list  = [] ; prices_list1 = []

for i in range(len(prices_file1)) : prices_list.append(prices_file1[i])
for i in range(len(prices_list))  : i = big_font.render('Price : ' + prices_file1[i].strip() , False , small_font_color ) ; prices_list1.append(i)     

interface_surf_x   = 0   ; interface_surf_y    = int(screen_height ) - inteface_surf.get_width() 
minimap_grid_width = 100 ; minimap_grid_height = 100 ; min_map_size = 3 ; max_map_size = 1.2 ; mini_map_grid_cell_size = meter * map_scale

cursor_types = ['Default' , 'Custom']
cursor_num = 0
cursor_type = cursor_types[cursor_num]

hero_inventory_types = ['Grid' , 'Circle']
hero_inventory_num = 0
hero_inventory_type = hero_inventory_types[hero_inventory_num]

hero_marker_color = (255 , 100 , 0)

def cutscene() : pass

def draw_mini_map():
    if show_map == 1:
        for i in range( len ( islands_file1 ) ) :
            for y in range( len ( islands_file1 ) ) :
                pg.draw.rect(mini_map_surf  , (100 , 50 , 0) , (minimap_border_offset + Sea_width / (100 * map_scale) + int(islands_file1[i].split(',')[0]) / (100 * map_scale) + i * int(islands_file1[i].split(',')[2])  / (100 * map_scale) , minimap_border_offset + Sea_width / (100 * map_scale) + int(islands_file1[i].split(',')[1]) / (100 * map_scale) + y * int(islands_file1[i].split(',')[2])  / (100 * map_scale) ,  5 / map_scale ,  5 / map_scale ))
        
        for i in range( len ( buildings_file1 ) ) :
             if show_buildings == 1 : pg.draw.rect(mini_map_surf , colors[4]  , ( int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1,  10 / map_scale, 10 / map_scale  ))
        
        for i in range( len ( vihicles_file1 ) ) : pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(vihicles_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(vihicles_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1 , 5 / map_scale , 3 / map_scale ))
        
        for i in range( len ( items_file1 ) ) :
             if show_items == 1 : pg.draw.rect(mini_map_surf , (0 , 255 , 0)  , (int(items_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(items_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1, 1 / map_scale , 1 / map_scale ))
        
        hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 )        , ( minimap_border_offset + camera.rect[0] / (100 * map_scale) + minimap_border_offset * minimap_object_offset ,  camera.rect[1] / (100 * map_scale) + minimap_border_offset * minimap_object_offset1  ) , 1 / map_scale )        
        
        for i in range(len(custom_checkpoints_list_x)) : pg.draw.circle(mini_map_surf , (255 , 0 , 0) , ( int(custom_checkpoints_list_x[i]) / (100 * map_scale ) , int(custom_checkpoints_list_y[i]) / (100 * map_scale)) , int(1 / map_scale)  , int(1 / map_scale) )

        screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
        
        pg.draw.rect(screen , (minimap_border_color) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
        
        if map_grid == 1:
            for x in range(grid_size1):
                for y in range(grid_size2):
                        pg.draw.rect(mini_map_surf , ( cell_color) , ( cell_size * x / map_scale * minimap_object_offset , cell_size * y / map_scale * minimap_object_offset1 , mini_map_grid_cell_size / map_scale , mini_map_grid_cell_size / map_scale) , 1 ) #drawing a inventory cells

def Animations():
        global Companion_image , player_image , Companion_animation,animation,hero_animations_dir,hero_image,hero_image1,Enemy_image,Enemy_animation
        for i in range(len(Companions_file1)) :    #Companion animation
            if camera.rect[0] + int(screen_width) - fov >= int(Companions_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(Companions_file1[i].split(',')[1]):
                if  Companion_animation  <= len(os.listdir(                        'Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/')) - 1:
                    Companion_image = pg.image.load(                               'Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/' + str(Companion_animation) + '.png')
                    Companion_animation += 1 ; Companion_image  = pg.image.load(   'Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/' + str(Companion_animation) + '.png')
                if  Companion_animation >= len(os.listdir(                         'Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/')) - 1 : 
                        Companion_animation =  0 ; Companion_image = pg.image.load('Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/' + str(Companion_animation) + '.png')
                        Companion_animation += 1 ; Companion_image = pg.image.load('Objects/Characters/Companions/' + str(Companion_types[i]) + '/' + str(i) + '/' + str(Companion_state) + '/' + str(Companion_turn) + '/' + str(Companion_animation) + '.png')
        
        if multiplayer == 1 : 
            for i in range(len(players_file1)) :    #Player animation
                if int(players_file1[i].split(',')[0]) >= camera.rect[0] + fov and  int(players_file1[i].split(',')[0]) <= camera.rect[0] + int(screen_width) - fov \
                    and int(players_file1[i].split(',')[1]) >= camera.rect[1] + fov and  int(players_file1[i].split(',')[1]) <= camera.rect[1] + int(screen_height) - fov :
                    if  player_animation <= len(os.listdir(                      'Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/' + str(player_turn)  + '/')) - 1 :
                        player_image = pg.image.load(                            'Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/' + str(player_turn)  + '/' + str(player_animation) + '.png') 
                        player_animation += 1 ; player_image  = pg.image.load(   'Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/' + str(player_turn)  + '/' + str(player_animation) + '.png')
                    if player_animation  >= len(os.listdir(                      'Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/' + str(player_turn)  + '/')) - 1 : 
                            player_animation = 0  ; player_image = pg.image.load('Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/'  + str(player_turn) + '/' + str(player_animation) + '.png')
                            player_animation += 1 ; player_image = pg.image.load('Objects/Characters/Players/' + str(player_types[i]) + '/' + str(player_state) + '/'  + str(player_turn) + '/' + str(player_animation) + '.png')
            
        #Enemy animation
        if game_mode != 'Peaceful':
            for i in range(len(Enemies_file1)) :
                if int(Enemies_file1[i].split(',')[0]) >= camera.rect[0] + fov and  int(Enemies_file1[i].split(',')[0]) <= camera.rect[0] + int(screen_width) - fov \
                    and int(Enemies_file1[i].split(',')[1]) >= camera.rect[1] + fov and  int(Enemies_file1[i].split(',')[1]) <= camera.rect[1] + int(screen_height) - fov and Enemy_image not in killed_units :
                    if  Enemy_animation <= len(os.listdir(                     'Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/')) - 1:
                        Enemy_image = pg.image.load(                           'Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/' + str(Enemy_animation) + '.png')
                        Enemy_animation += 1 ; Enemy_image  = pg.image.load(   'Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/' + str(Enemy_animation) + '.png')
                    if  Enemy_animation >= len(os.listdir(                     'Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/')) - 1: 
                            Enemy_animation =  0 ; Enemy_image = pg.image.load('Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/' + str(Enemy_animation) + '.png')
                            Enemy_animation += 1 ; Enemy_image = pg.image.load('Objects/Characters/Enemies/' + str(enemy_types[i]) + '/' + str(i) + '/' + str(enemy_state) + '/' + str(enemy_turn) + '/' + str(Enemy_animation) + '.png')

        #Hero animation
        if vihicle_sit == 0:
            if game_state == 'Play' and camera.rect[0] >= 0 and camera.rect[1] >= 0:
                    hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                    if animation <= len(hero_animations_dir) - 1:
                        clock.tick(FPS / fps_1)
                        animation += 1
                        hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                        hero       =                'Objects/Characters/Hero/' + str(name)      + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                        hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name)      + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                        heroimage  = Image.open(    'Objects/Characters/Hero/' + str(name)      + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                        hero_x , hero_y = int(screen_width) / 2  - heroimage.width /2 , int(screen_height)  /2 - heroimage.height /2

                    if animation >= len(hero_animations_dir) - 1:
                        animation = 0
                        hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                        hero_speed = 4
                        clock.tick(FPS / fps_1)
                        animation  += 1
                        hero       =                'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                        hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                        heroimage  = Image.open(    'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                        hero_x , hero_y = int(screen_width) / 2  - heroimage.width /2 , int(screen_height)  /2 - heroimage.height / 2

def mini_map_keyboard_controls():
    keys = pg.key.get_pressed()
    global map_scale , minimap_x , minimap_y , map_size , minimap_horizontal_offset , minimap_vertical_offset , cancel_icon , cancel_icon_x , cancel_icon_y , mini_map_surf
    global minimap_object_offset , minimap_object_offset1

    if show_map == 1 and game_state == 'Play' :
        if keys [pg.K_LEFT ] : minimap_object_offset  -= 1 ; #draw_mini_map()
        if keys [pg.K_RIGHT] : minimap_object_offset  += 1 ; #draw_mini_map()
        if keys [pg.K_UP   ] : minimap_object_offset1 -= 1 ; #draw_mini_map()
        if keys [pg.K_DOWN ] : minimap_object_offset1 += 1 ; #draw_mini_map()

        if keys [pg.K_KP_1] : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_2] : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_3] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_4] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = int(screen_height) - int(screen_height) / map_size

        if keys [pg.K_KP_5] : map_size = max_map_size ; mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
        if map_size == max_map_size : screen.blit( cancel_icon , ( cancel_icon_x , cancel_icon_y))

        if keys [pg.K_KP_0] : map_size = min_map_size ; mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))

        if keys [pg.K_KP_6] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = 0     
        if keys [pg.K_KP_7] : minimap_x = 0 ; minimap_y = 0
        if keys [pg.K_KP_8] : minimap_x = 0 ; minimap_y = 0
        if keys [pg.K_KP_9] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = 0

        if keys [pg.K_KP_PLUS ] : mini_map_surf.fill((minimapBGcolor)) ; map_scale -= 0.01 ; draw_mini_map()
        if keys [pg.K_KP_MINUS] : mini_map_surf.fill((minimapBGcolor)) ; map_scale += 0.01 ; draw_mini_map()

def mini_map_mouse_controls():
    global cancel_icon
    if game_state == 'Play' : 
        if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and \
            pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and map_size == max_map_size : map_size = min_map_size

        if event.button == 3 and map_size == max_map_size : 
            spawn_sound.play() ; custom_checkpoints_list_x.append(camera.rect[0] + pos[0]) ; custom_checkpoints_list_y.append(camera.rect[1] + pos[1])
            
def toggle_settings():
    if game_state == 'Settings':
        draw_menu()
        for i in range(len(settings_file1)):
            pg.draw.rect(screen , (Button_color) , ( int(screen_width) / 2 - button_width  , int(screen_height) /2 - int(screen_height) /4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ), 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , (Button_frame_color)  , ( int(screen_width) / 2 - button_width , int(screen_height) /2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )            
            screen.blit(settings[i] , ( int(screen_width) / 2 - bigfont * 10 / 2                 , int(screen_height) /2 - int(screen_height) / 4 - bigfont + i             * 40 + bigfont / 2 , button_width , bigfont + 5 ))
            
            if active_button == 0:
                for i in range(len(resolutions_file1)):
                    Button = pg.draw.rect(screen , (Button_color ) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    pg.draw.rect(screen , (Button_frame_color)     , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                    screen.blit(resolutions_list[i] , ( int(screen_width) / 2 + bigfont                , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2))

            if active_button == 1 or active_button == 2:
                pg.draw.line(screen   , (0   , 0  , 0 ) , [ int(screen_width) / 2 + bigfont        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont ] , [ int(screen_width) / 2 + bigfont + 100 , int(screen_height) /2 - int(screen_height) /4 - bigfont + 0 * 40 + bigfont ] , 1 )
                pg.draw.circle(screen , (255 , 0  , 0 ) , ( int(screen_width) / 2 + bigfont        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2)  , 1)
                pg.draw.circle(screen , (255 , 0  , 0 ) , ( int(screen_width) / 2 + bigfont  + 100 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2)  , 1)
                
                pg.draw.rect(screen   , (Button_frame_color ) , ( int(screen_width) / 2 + bigfont  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                screen.blit(ok          , ( int(screen_width) / 2 - bigfont * 10 / 2  + 300        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont ))
                screen.blit(add         , ( int(screen_width) / 2 + 500     / 4  + 10              , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , 100 , bigfont ))
                screen.blit(remove      , ( int(screen_width) / 2 + 5                              , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , 100 , bigfont ))
            
            if active_button == 3:
                for i in range(len(langs_file1)):
                    Button = pg.draw.rect(screen , (Button_color)        , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont), 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    pg.draw.rect(screen          , (Button_frame_color)  , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont),2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    screen.blit(langs_list[i]                            , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2))

def character_select():
    if game_state == 'character select menu':
        draw_menu()
        for i in range(len(Hero_types)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(Hero_types_list[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)  ,  ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(hero_image1 , ( int(screen_width) / 2 + int(screen_width) / 4 - hero_image1.get_width() /2 , hero_image1.get_height() ))

def game_mode_select():
    if game_state == 'game mode select':
        draw_menu()
        for i in range(len(game_modes1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(game_modes1[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))

def Difficulty_select():
    if game_state == 'Select a difficulty':
        draw_menu()
        for i in range(len(difficulties1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(difficulties1[i]                  , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))

def Open_backpack():
    if game_state == 'Backpack':
        draw_menu()
        for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , cell_size) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , ( Button_frame_color  ) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * active_button , button_width , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(menu_titles1[i]                   , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , bigfont ))

            if show_interface == 1 and active_button == 0 :
                for x in range(items_max):
                    for y in range(items_max):
                        pg.draw.rect(screen      , ( cell_color)           , ( int(screen_width) / 2 + cell_size * x , int(screen_height) / 4 + cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                        pg.draw.rect(screen      , ( Button_frame_color  ) , ( int(screen_width) / 2 + cell_size * 0 , int(screen_height) / 4 + cell_size * active_button1 , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
                screen.blit(hero_inventory[item] , (int(screen_width ) / 2 , int(screen_height) - cell_size * 2  )) #drawing a title of the item in inventory            
            
            if show_interface == 1 and active_button == 1 :                
                for i in range(len(crafts_file1) //crafts_on_page):
                        Button = pg.draw.rect(screen  , (Button_color)       , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + i             * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                        pg.draw.rect(screen           , (Button_frame_color) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                        screen.blit(new_craft         , ( int(screen_width) / 2 + bigfont + button_width - cell_size , int(screen_height) / 10 + i * 40 , 100 , bigfont ))

def Open_unit_inventory():
    if vihicle_sit == 1:
        for x in range(items_max):
            for y in range(items_max):
                pg.draw.rect(screen          , ( cell_color)           , ( int(screen_width)  / 4 + cell_size * x , int(screen_height) / 4 + cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                pg.draw.rect(screen          , ( Button_frame_color  ) , ( int(screen_width)  / 4 + cell_size * 0 , int(screen_height) / 4 + cell_size * active_button1 , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(hero_inventory[item] , (int(screen_width ) / 2 ,   int(screen_height) - cell_size     * 2  )) #drawing a title of the item in inventory            
                
def Trade_menu():
    if game_state      == 'Trade menu':
        menu_titles    = ['Ammo' , 'Tools' , 'Clothes' , 'Weapons']
        menu_titles1   = []
        menu_title_num = 0
        menu_title     = menu_titles[menu_title_num]

        for i in range(len(menu_titles)) : i = big_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)   
        
        draw_menu()

        for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , cell_size) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , ( Button_frame_color  ) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * active_button , button_width , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(menu_titles1[i]             ,       (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , bigfont ))

            for i in range(len(crafts_file1) //crafts_on_page):
                        Button = pg.draw.rect(screen  , (Button_color)       , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                        pg.draw.rect(screen           , (Button_frame_color) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                        screen.blit(new_craft         ,                        ( int(screen_width) / 2 + bigfont , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
            for i in range(len(prices_list1)) : screen.blit(prices_list1[i] ,  ( int(screen_width) / 2 + bigfont + button_width / 2   , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))

def toggle_main_menu():
    if game_state == 'Main menu':
        draw_menu()
        for i in range(len(main_menu_file1)):
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(main_menu[i]                      , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)    , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)

def text_updating():
    global new_craft,new_quest,checkpoints_list,achievements_list,hero_inventory_nums,show_game_state,ok,apply,cancel,action_counter,checkpoints_file1,dialoge_started,achievements_file1,checkpoint_size,dialoge_num,action,checkpoint_num

    lang_num = active_button1 ; language = languages[lang_num]
    crafts_list = [] ; crafts_file_name   = 'txt/langs/' + str(language) + '/Crafts.txt' ; crafts_file_mode = 'r' ; crafts_file = open (crafts_file_name , crafts_file_mode , encoding = "utf-8") ; crafts_file1 = crafts_file.readlines()
    langs_file_name = 'txt/Languages.txt' ; langs_file_mode = 'r' ; langs_file = open (langs_file_name  , langs_file_mode , encoding= "utf-8") ; langs_file1 = langs_file.readlines() ; langs_list = []
    dialoges_list = [] ; dialoges_file_name = 'txt/Dialoges.txt' ; dialoges_file_mode = 'r' ; dialoges_file = open (dialoges_file_name , dialoges_file_mode , encoding= "utf-8") ; dialoges_file1 = dialoges_file.readlines() ; dialoge_num = 0 ; dialoge_started = 0
    checkpoints_list  = [] ; checkpoints_file_name  = 'txt/Checkpoints.txt' ; checkpoints_file_mode = 'r' ; checkpoints_file = open (checkpoints_file_name , checkpoints_file_mode) ; checkpoints_file1 = checkpoints_file.readlines() ; checkpoint_size = 100 ; checkpoint_num = 0
    achievements_list = [] ; achievements_file_name = 'txt/Achievements.txt' ; achievements_file_mode = 'r' ; achievements_file = open (achievements_file_name , achievements_file_mode , encoding = "utf-8") ; achievements_file1 = achievements_file.readlines()
    actions_list = [] ; actions_file_name = 'txt/Actions.txt' ; actions_file_mode = 'r' ; actions_file = open (actions_file_name , actions_file_mode) ; actions_file1 = actions_file.readlines() ; actions_list.append(i) ; action_num = 0 ; action_counter = 0 ; action = actions_list[action_num]
    quests_list = [] ; quests_states_list = [] ; quests_file_name = 'txt/langs/' + str(language) + '/Quests.txt' ; quests_file_mode = 'r' ; quests_file = open (quests_file_name , quests_file_mode , encoding = "utf-8") ; quests_file1 = quests_file.readlines()
    main_menu = [] ; main_menu_file_name = 'txt/langs/' + str(language) + '/Main menu.txt' ; main_menu_file_mode = 'r' ; main_menu_file = open (main_menu_file_name , main_menu_file_mode , encoding = "utf-8") ; main_menu_file1 = main_menu_file.readlines()
    settings = [] ; settings_file_name = 'txt/langs/' + str(language) + '/Settings.txt' ; settings_file_mode = 'r' ; settings_file = open (settings_file_name , settings_file_mode , encoding = "utf-8") ; settings_file1 = settings_file.readlines()
    hero_inventory = [] ; hero_inventory_nums = [] ; hero_inventory_file_name = 'txt/langs/' + str(language) + '/Hero inventory.txt' ; hero_inventory_file_mode = 'r' ; hero_inventory_file = open (hero_inventory_file_name , hero_inventory_file_mode , encoding= "utf-8") ; hero_inventory_file1 = hero_inventory_file.readlines()

    for i in range(len(langs_file1))     : i = big_font.render(langs_file1[i].strip()  , False , small_font_color ) ; langs_list.append(i)
    for i in range(len(dialoges_file1))  : i = small_font.render(dialoges_file1[i].strip() , False , small_font_color ) ; dialoges_list.append(i) 
    for i in range(len(actions_file1))   : i = small_font.render(str(actions_file1[i]).strip()  , False , small_font_color ) ; actions_list.append(i)
    for i in range(len(actions_list))    : i = small_font.render(str(actions_list[i] ).strip()  , False , small_font_color ) ; actions_list.append(i)
    for i in range(len(crafts_file1))    : i = big_font.render(crafts_file1[i].strip()  , False , small_font_color ) ; crafts_list.append(i)
    for i in range(len(quests_file1))    : i = small_font.render(quests_file1[i].split(',')[0].strip()  , False , small_font_color ) ; quests_list.append(i)
    for i in range(len(quests_file1))    : i = small_font.render(quests_file1[i].split(',')[1].strip()  , False , small_font_color ) ; quests_states_list.append(i)
    for i in range(len(main_menu_file1)) : i = big_font.render(main_menu_file1[i].strip()  , False , small_font_color ) ; main_menu.append(i)
    for i in range(len(settings_file1))  : i = big_font.render(settings_file1[i].strip() , False , small_font_color ) ; settings.append(i)
    for i in range(len(hero_inventory_file1)) : i = big_font.render(hero_inventory_file1[i].split(',')[0].strip()          , False , small_font_color ) ; hero_inventory.append(i)     
                    
    new_craft = small_font.render('Uus' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply'  , False , small_font_color) ; cancel = small_font.render('Tagasi'  , False , small_font_color)
    show_game_state = big_font.render('Menüü' , False , small_font_color)

def player_movement():
        global calc_dist,show_distance,hero_checkpoint_offset_x,hero_checkpoint_offset_y,state,hero_x,hero_y,turn,hero_speed
        keys = pg.key.get_pressed()
        if game_state == 'Play':
            if keys[pg.K_a] and camera.rect[0] >= 0 and camera.rect[1] >= 0 : state = 'go' ; turn  = 'left'; hero_speed = 4 ; vector[0] -= hero_speed ; hero_checkpoint_offset_x -= hero_speed;calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ));show_distance    = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )
            if keys[pg.K_d] and camera.rect[0] <= map_width and camera.rect[1] >= 0 : state = 'go' ; turn = 'right' ; hero_speed = 4 ;vector[ 0 ]  += hero_speed ; hero_checkpoint_offset_x += hero_speed ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color ) ; #hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
            if keys[pg.K_w] and camera.rect[0] >= 0 and camera.rect[1] >= 0 :vector[1] -= hero_speed ; hero_checkpoint_offset_y -= hero_speed ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )
            if keys[pg.K_s] and camera.rect[0] >= 0 and camera.rect[1] >= 0 : vector[ 1 ]   += hero_speed ; hero_checkpoint_offset_y += hero_speed; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2 ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2) + ((y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )

            if vector != [ 0 , 0 ] : camera.move(vector) #Если игрок ходил

def start():
    if game_state == 'Saves':
        draw_menu()
        for i in range(len(saves_file1)):
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(saves_list[i]                     , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)

    if game_state == 'Crafting':
        draw_menu()
        for i in range(len(crafts_file1) //crafts_on_page):
                #drawing a buttons for a crafts menu
                Button = pg.draw.rect(screen        , (Button_color)       , ( int(screen_width) / 2 - button_width / 2 , int(screen_height) /10 + i * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                pg.draw.rect(screen        , (Button_frame_color) , ( int(screen_width) / 2 - button_width / 2  , int(screen_height) /10 + active_button * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                screen.blit(crafts_list[i] , ( int(screen_width) / 2 - button_width / 2 + bigfont , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
                screen.blit(new_craft      , ( int(screen_width) / 2 + - button_width / 2 - cell_size * 2 , int(screen_height) / 10 + i * 40 , 100 , bigfont ))

    toggle_settings() ; toggle_main_menu() ; character_select() ; Trade_menu() ; game_mode_select() ; Open_backpack() ; mini_map_keyboard_controls() ; Difficulty_select() 

    if game_state == 'Play':
        mouse_visible = False ; mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        if ground == 1:
            for i in range( len ( islands_file1 ) ) : 
                for y in range( len ( islands_file1 ) ) : 
                    if camera.rect[0] + int(screen_width) - fov >= int(islands_file1[i].split(',')[0]) + y * int(islands_file1[i].split(',')[2])  and camera.rect[1] + int(screen_height) - fov >= int(islands_file1[i].split(',')[1]):
                        screen.blit( islands_images[ i ] , ( -camera.rect[ 0 ] +  Sea_width + int(islands_file1[i].split(',')[0]) + i * int(islands_file1[i].split(',')[2]) ,  -camera.rect[ 1 ] +  Sea_width + int(islands_file1[i].split(',')[1]) + y * int(islands_file1[i].split(',')[2])    ) )
            
            world_border = pg.draw.rect(screen , (Button_frame_color) , ( -camera.rect[ 0 ] + 0 ,-camera.rect[ 1 ] + 0 , map_width , map_width) , 100 , 0  )

            for i in range( len ( roads_file1 ) ) :
                 if camera.rect[0] + int(screen_width) - fov >= int(roads_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(roads_file1[i].split(',')[1]):
                    pg.draw.line(screen , (0 , 0  , 0 ) , [  -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1])] , [ -camera.rect[ 0 ] + int(roads_file1[i].split(',')[2]) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[3])], 300 )
            
            for i in range( len ( vihicles_file1 ) ) : 
                 if camera.rect[0] + int(screen_width) - fov >= int(vihicles_file1[i].split(',')[0])  and camera.rect[1] + int(screen_height) - fov >= int(vihicles_file1[i].split(',')[1]) and hero_image != vihicles_images_list[i]:
                    screen.blit( vihicles_images_list[i] , ( -camera.rect[ 0 ] + int(vihicles_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(vihicles_file1[i].split(',')[1]) ) ) 
        
            for i in range( len( buildings_file1 )) : 
                 if camera.rect[0] + int(screen_width) - fov >= int(buildings_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(buildings_file1[i].split(',')[1]):
                    screen.blit( Buildings_images_list[i] , ( -camera.rect[ 0 ] + int(buildings_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(buildings_file1[ i ].split(',')[1] ) ))
        
        for i in range(len(checkpoints_file1)) : pg.draw.circle(screen , (255 , 0 , 0 ) , (-camera.rect[0] + int(checkpoints_file1[i].split(',')[0]) + 50 , -camera.rect[1] + int(checkpoints_file1[i].split(',')[1]) + 180) , 50 , 1 )
        
        for i in range(len(custom_checkpoints_list_x)) :
            pg.draw.circle(screen , (255 , 0 , 0)      , ( -camera.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera.rect[ 1 ] + int(custom_checkpoints_list_y[i])      ) , 20  , 5 )
            screen.blit(custom_checkpoint_title        , ( -camera.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera.rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))
            mini_map_surf.blit(custom_checkpoint_title , ( -camera.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera.rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))

        for i in range(len(Companions_file1)) : 
             if camera.rect[0] + int(screen_width) - fov >= int(Companions_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(Companions_file1[i].split(',')[1]):
                screen.blit( Companions_images_list[i]  , ( -camera.rect[ 0 ] + int(Companions_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Companions_file1[i].split(',')[1])  ) )
        
        if multiplayer == 1 : 
            for i in range(len(players_file1)):
                if hide_nicknames == 0 and camera.rect[0] + int(screen_width) - fov >= int(players_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(players_file1[i].split(',')[1]):
                    pg.draw.rect(screen , (45 , 45 , 45) , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) + bigfont , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , len(nicknames_file1[i]) * len(nicknames_file1[i]) - len(nicknames_file1[i]) , smallfont))
                    screen.blit(nicknameslist[i] , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) + bigfont , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , 100 , bigfont ) )
                        
                if int(players_file1[i].split(',')[0]) >= camera.rect[0] + fov and  int(players_file1[i].split(',')[0]) <= camera.rect[0] + int(screen_width) - fov \
                    and int(players_file1[i].split(',')[1]) >= camera.rect[1] + fov and  int(players_file1[i].split(',')[1]) <= camera.rect[1] + int(screen_height) - fov :  screen.blit( Companion_image , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1])  ) )
                
        for i in range(len(units_with_a_quests)) : screen.blit(new_quest , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0])  , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , 100 , bigfont ) )

        #drawing an enemies(images)
        for i in range(len(Enemies_file1)):
            if int(Enemies_file1[i].split(',')[0]) >= camera.rect[0] + fov and  int(Enemies_file1[i].split(',')[0]) <= camera.rect[0] + int(screen_width) - fov \
                and int(Enemies_file1[i].split(',')[1]) >= camera.rect[1] + fov and  int(Enemies_file1[i].split(',')[1]) <= camera.rect[1] + int(screen_height) - fov and Enemy_image not in killed_units and difficulty != 'Peaceful' : screen.blit( Enemy_image , ( -camera.rect[ 0 ] + int(Enemies_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Enemies_file1[i].split(',')[1])  ) )
        
        #drawing a text for a quests menu
        for i in range(len(quests_file1)) : quests_surf.blit(quests_list[i] , (5 , 5 + bigfont / 2 * i * 1.6 ) ) ; #screen.blit(show_quests_num , (int(screen_width ) - int(screen_width) /3  , int(screen_height ) - int(screen_height) /3 - bigfont ) )

        for i in range(len(Furniture_file1)) :
            for y in range(int(Furniture_file1[i].split(',')[2])):
                if camera.rect[0] + int(screen_width) - fov >= int(Furniture_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(Furniture_file1[i].split(',')[1]):
                    screen.blit( Furniture_images_list[ i ] , ( -camera.rect[ 0 ] + int(Furniture_file1[i].split(',')[0]) + int(Furniture_file1[i].split(',')[2]) * y * 10  , -camera.rect[ 1 ] + int(Furniture_file1[i].split(',')[1] ) ) )
        
        for i in range(len(items_file1)) :
                if camera.rect[0] + int(screen_width) - fov >= int(items_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(items_file1[i].split(',')[1]):
                    screen.blit( items_images[ i ] , ( -camera.rect[ 0 ] + int(items_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Furniture_file1[i].split(',')[1] ) ) )
        
        
        for i in range(len(Plants_file1)) :
                if camera.rect[0] + int(screen_width) - fov >= int(Plants_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(Plants_file1[i].split(',')[1]):
                    screen.blit( Plants_file1[ i ] , ( -camera.rect[ 0 ] + int(Plants_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Plants_file1[i].split(',')[1] ) ) )
        

        inteface_surf.set_alpha(50) ; quests_surf.set_colorkey(( 0 , 0 , 0 ))
        screen.blit( hero_image , ( hero_x , hero_y ) )

        fog                  = pg.draw.rect(screen   , (Button_color) , (-camera.rect[ 0 ] + int(screen_width) /  2 - button_width / 2 + 600 , -camera.rect[ 1 ] + int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        acid_cloud           = pg.draw.rect(screen   , (Button_color) , (-camera.rect[ 0 ] + int(screen_width) /  2 - button_width / 2 , -camera.rect[ 1 ] + int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        water_bubbles        = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        burst                = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        new_skill_effect     = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        damage_effect        = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        heal_effect          = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        death_effect         = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        research_effect      = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        loading_effect       = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        dialoge_effect       = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        blood_effect         = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        paranormal_effect    = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        research_complete = 0

        if show_interface == 1:
            for i in range(len(hero_inventory_file1)):
                pg.draw.rect(screen , ( cell_color)           , ( int(screen_width) / 2 - cell_size * i     + cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                pg.draw.rect(screen , ( Button_frame_color  ) , ( int(screen_width) / 2 - cell_size * item  + cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            
            screen.blit(hero_inventory[item] , (int(screen_width ) / 2 , int(screen_height) - cell_size * 2  )) #drawing a title of the item in inventory
    
            dark_surf.fill(dark_surf_color) ; dialoge_surf.fill((0 , 0 , 0 )) ; dark_surf.set_alpha(dark_level)
            screen.blit(dark_surf     , ( 0 , 0 )) 
            screen.blit(inteface_surf , ( interface_surf_x , interface_surf_y ))
            screen.blit(quests_surf   , ( int(screen_width) - 200 , int(screen_height ) - 200 ))
            quests_surf.fill((quest_surf_color))
                
            #drawing a road to the checkpoint
            pg.draw.line(screen   , (0   , 0 , 0 ) ,    [ -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y ] , [ -camera.rect[ 0 ] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[ 1 ] + int(checkpoints_file1[0].split(',')[1])] , 1 )
                
            #segmented road to the checkpoint 
            #for i in range(int(calc_dist) // 10 )  : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) + i * 10 , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1]) - i * 10) , 1)        
                
            #drawing a circle at the hero x and hero y
            if vihicle_sit == 0 : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[1] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y) , checkpoint_size , 1 )
                
            #drawing a circle at the checkpoint x and checkpoint y
            pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
                
            draw_mini_map()

            if map_size == min_map_size  and vihicle_sit == 1 :
                
                pg.draw.line(  screen , (0 , 255 , 0) , (400 , 400) , ( 400 + fuel_bar_width * -math.cos(fuel) , 400 + fuel_bar_width * -math.sin(-fuel)) , 1)
                screen.blit(show_fuel , ( 0 , int(screen_height ) - 250))
                fuel_values = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )

                screen.blit( cancel_icon , ( cancel_icon_x,cancel_icon_y))

            
            screen.blit(show_health     , ( bigfont , int(screen_height ) - bigfont * 6)) , screen.blit(health_icon     , ( 0 , int(screen_height ) - bigfont * 6))
            screen.blit(show_hero_armor , ( bigfont , int(screen_height ) - bigfont * 5)) , screen.blit(armor_icon      , ( 0 , int(screen_height ) - bigfont * 5))
            screen.blit(show_ammo       , ( bigfont , int(screen_height ) - bigfont * 4)) , screen.blit(ammo_icon       , ( 0 , int(screen_height ) - bigfont * 4))
            screen.blit(show_radiation  , ( bigfont , int(screen_height ) - bigfont * 3)) , screen.blit(radiation_icon  , ( 0 , int(screen_height ) - bigfont * 3))
            screen.blit(show_energy     , ( bigfont , int(screen_height ) - bigfont * 2)) , screen.blit(energy_icon     , ( 0 , int(screen_height ) - bigfont * 2))
            screen.blit(show_money      , ( 0       , int(screen_height ) - bigfont))

            if blit_distance == 1 and map_size == min_map_size : screen.blit(show_distance  , ( hero_x , hero_y - bigfont ) )

            for i in range(len(hero_belt_inventory_images)) : screen.blit( hero_belt_inventory_images[i] , ( int(screen_width) / 2 - cell_size * i + 10  + cell_size , int(screen_height) - cell_size / 2 - items_images[i].get_height() / 2 ) )

run = True ; logging.info( msg = 'GAME STARTED!' )
multiplayer = 0
while run :
    if dark_level <= max_dark_level : dark_level += 0.1 ; clock.tick(FPS / fps_1)
    
    Animations()
    vector = [ 0 , 0 ]
    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION : pos = pg.mouse.get_pos()
        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and int(ammo) > 0  and int(ammo) <= max_ammo and game_state == 'Play' and dialoge_started == 0 and map_size == min_map_size :
                ammo -= 1 ; gun_shot = pg.mixer.Sound( 'Audio/sounds/firegun/single/0.mp3' ) ; gun_shot.play()
                show_hero_armor = big_font.render('armor : ' + str(armor).strip() + " / " + str( max_armor).strip() , False , ( 250 , 0 , 0 ) ) ; show_ammo = big_font.render('ammo : ' + str(ammo).strip() + " / " + str(max_ammo * mags).strip() , False , ( 250 , 0 , 0 ) ) ; show_health = big_font.render('health : ' + str(health).strip() + " / " + str(max_health).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation  = big_font.render('radiation : ' + str(radiation).strip() + " / " + str(max_radiation).strip() , False , ( 255 , 0 , 0 ) )
                hero            = 'Objects/Characters/Hero/'     + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png' ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            if event.button     == 1 and int(ammo) <= 1 and game_state == 'Play' and dialoge_started == 0 and map_size == min_map_size :
                show_hero_armor = big_font.render('armor : ' + str(armor).strip() + " / " + str( max_armor).strip() , False , ( 250 , 0, 0  ) ) ; show_ammo = big_font.render('ammo : ' + str(ammo).strip() + " / " + str(max_ammo * mags).strip() , False , ( 250 , 0 , 0 ) ) ; show_health = big_font.render('health : ' + str(health).strip() + " / " + str(max_health).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation  = big_font.render('radiation : ' + str(radiation).strip() + " / " + str(max_radiation).strip() , False , ( 255 , 0 , 0 ) )
                no_ammo         = pg.mixer.Sound( 'Audio/sounds/firegun/no ammo/0.mp3' ) ; no_ammo.play()
        
            if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and game_state == 'Play' and vihicle_sit == 1:
                vihicle_sit =  0

            if event.button == 3 and pos[0] >= hero_x and pos[0] <= hero_x + hero_image.get_width() and pos[1] >=  hero_y and pos[1] <= hero_y + hero_image.get_height() and open_backpack == 0 and game_state == 'Play':                
                game_state = 'Backpack'
            
            for i in range(len(Companions_file1)):
                    if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(Companions_file1[i].split(',')[0]) and pos[0] <=  -camera.rect[0] + int(Companions_file1[i].split(',')[0]) + Companions_images_list[i].get_width() and pos[1] >=  -camera.rect[1] + int(Companions_file1[i].split(',')[1])  and pos[1] <=  -camera.rect[1] + int(Companions_file1[i].split(',')[1]) + Companions_images_list[i].get_height():
                        game_state = 'Trade menu'
                        if welcome_num  >= 0 and welcome_num <= len(welcome_speech_dir) - 1 : welcome_num += 0.5 ; welcome = pg.mixer.Sound('Audio/speech/langs/' + str(language) + '/welcome/' + str(int(welcome_num)) + '.mp3') ; welcome.play()
                        if welcome_num  >= len(welcome_speech_dir) - 1 : welcome_num = 0 ; welcome_num += 0.5 ; welcome = pg.mixer.Sound('Audio/speech/langs/' + str(language) + '/welcome/' + str(int(welcome_num)) + '.mp3') ; welcome.play()

            for i in range(len(Enemies_file1)):
                    if Enemy_image not in killed_units and  event.button == 1 and pos[0] >=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0]) + Enemy_image.get_width() and pos[1] >=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) + Enemy_image.get_height():
                        if enemy_sound_num <= len(enemy_sounds_dir) - 1:enemy_sound.play() ; enemy_sound_num += 0.5 ; enemy_sound = pg.mixer.Sound('Audio/sounds/roar/' + str(int(enemy_sound_num)) + '.mp3')
                        if enemy_sound_num >= len(enemy_sounds_dir) - 1:enemy_sound_num = 0 ; enemy_sound.play() ; enemy_sound_num += 0.5 ; enemy_sound = pg.mixer.Sound('Audio/sounds/roar/' + str(int(enemy_sound_num)) + '.mp3') ; killed_units.append(Enemy_image)

            for i in range(len(vihicles_file1)):
                if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(vihicles_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(vihicles_file1[i].split(',')[0]) + vihicles_images_list[i].get_width() and pos[1] >=  -camera.rect[1] + int(vihicles_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(vihicles_file1[i].split(',')[1]) + vihicles_images_list[i].get_height() and vihicle_sit == 0:
                    vihicle_sit = 1 ; camera.rect[0] = int(vihicles_file1[i].split(',')[0]) - int(screen_width) / 2 ; camera.rect[1] = int(vihicles_file1[i].split(',')[1]) - int(screen_height) / 2 ; hero_image = vihicles_images_list[i]
            

            for i in range(len(items_file1)):
                if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0]) and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images[i].get_width() \
                    and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images[i].get_height():
                    hero_belt_inventory_images.append(items_images[i])

                    if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_belt_inventory_images) - 1 <= items_max:
                        pickup_sound.play() ; pickup_sound_num += 0.5 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')

                    
            #button 4 or 5 = mouse_wheel_scrolling button 1 = left mouse button button 3 = right mouse button 
            if game_state == 'Main menu':   
                if event.button == 1 and active_button == 0 : spawn_sound.play() ; game_state = 'Saves' 
                if event.button == 1 and active_button == 1 : click_sound.play() ; game_state = 'character select menu'
                if event.button == 1 and active_button == 2 : click_sound.play() ; game_state = 'Settings'
                if event.button == 1 and active_button == 3 : click_sound.play() ; pg.quit()

            if game_state == 'Play' :
                if dialoge_started  == 0:
                    if event.button == 2 : game_state = 'Trade menu' ; print('active buton ', active_button) ; click_sound.play()

                    if map_size == min_map_size :  
                        if event.button == 4  and item >= 0: item -= 1 ; click_sound.play()
                        if event.button == 5  and item <= len(hero_inventory_file1) - 3 : item += 1 ; click_sound.play()
                    
                    if map_size == max_map_size :  
                        if event.button == 4 : map_scale -= 0.1 ; draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 

                        if event.button == 5 : map_scale += 0.1 ; draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 
                
                if dialoge_started  == 1:
                    if event.button == 1  and action_counter == 0 : spawn_sound.play()
                    if event.button == 1  and action_counter == 2 : game_state = 'Trade menu' ;dialoge_started = 0 ; spawn_sound.play() 
                    if event.button == 1  and action_counter == 3 : game_state = 'Crafting'   ; dialoge_stated = 0 ; spawn_sound.play() 
                    if event.button == 1  and action_counter == 4 : dialoge_started = 0
                    
                    if event.button == 4  and action_counter >= 1 : action_counter -= 1 ; click_sound.play()
                    if event.button == 5  and action_counter <= len(actions_list) - 2 : action_counter += 1 ; click_sound.play()

            if game_state == 'character select menu':
                if event.button == 0 : game_state = 'Play' ; print('game state : ', game_state ) ; click_sound.play()
                if event.button == 4 and active_button >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button) 
                if event.button == 5  and active_button <= len(Hero_types) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button)

            if game_state == 'Trade menu':
                if event.button == 4 and pos[0]<= int(screen_width) / 2 and active_button >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button) 
                if event.button == 5 and pos[0]<= int(screen_width) / 2 and active_button <= len(menu_titles1) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button) 
            
                if event.button == 4 and pos[0]>= int(screen_width) / 2 and active_button1 >= 1 : active_button1 -= 1 ; click_sound.play() ; print('active buton ', active_button) 
                if event.button == 5 and pos[0]>= int(screen_width) / 2 and active_button1 <= len(menu_titles1) - 2 : active_button1 += 1 ; click_sound.play() ; print('active buton1 ' , active_button1) 
            
            if game_state == 'Saves':
                if event.button == 1 and active_button == 1 : game_state = 'game mode select' ; click_sound.play()
                if event.button == 4 and active_button == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button == 3 and active_button1  <= len(langs_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            
            if game_state == 'game mode select':
                if event.button == 1 and active_button == 0 : game_state = 'Select a difficulty' ; click_sound.play()
                if event.button == 4 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button1  <= len(langs_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            
            if game_state == 'Select a difficulty':
                if event.button == 1 and active_button == 0 : game_state = 'Play' ; click_sound.play()
                if event.button == 4 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button1  <= len(langs_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()

            if game_state == 'Backpack':
                if event.button == 1 and active_button == 1 : game_state = 'Play' ; click_sound.play()
                if event.button == 4 and active_button  >= 1 and pos[0] >= int(screen_width) / 2 : active_button -= 1 ; click_sound.play() 
                if event.button == 5 and active_button  <= len(langs_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button += 1 ; click_sound.play()

            if game_state == 'Settings':
                if event.button == 1 : click_sound.play()
                if event.button == 3 : game_state = 'Main menu' ; click_sound.play() ; active_button = 0
                
                if event.button == 4 and active_button  >= 1 and pos[0] <= int(screen_width) / 2 : active_button -= 1 ; click_sound.play()
                if event.button == 5 and active_button  <= len(settings_file1) -2 and pos[0] <= int(screen_width) / 2 : active_button += 1 ; click_sound.play()
                
                if event.button == 4 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play()
                if event.button == 5 and active_button1  <= len(settings_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()

                if event.button == 4 and active_button == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button == 3 and active_button1  <= len(langs_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()

                if event.button == 1 and pos[0] >= int(screen_width) / 2 : text_updating()

        if event.type == pg.QUIT : run = False

    keys = pg.key.get_pressed()
    
    player_movement()

    if game_state == 'Play':
        if keys[pg.K_e] and vihicle_sit == 1 : Open_unit_inventory()
        if keys [pg.K_ESCAPE]   and open_backpack == 1: open_backpack  = 0
        if keys [reload_btn] and mags >= 1 : reloadsound = pg.mixer.Sound( 'Audio/sounds/firegun/reload.mp3' ) ; reloadsound.play() ; mags -= 1 ; hero_file_name = 'txt/hero.txt' ; hero_file_mode = 'w' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file.write(str(mags)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(mags)) ; hero_file.write(str(mags)) ; hero_file.close() ; ammo = max_ammo ; show_ammo  = big_font.render(str(ammo) + " / "  + str( ammo * mags ) , False , colors[2] ) ; show_armor = big_font.render(str(armor).strip() + " / "  + str( max_armor ).strip() , False , ( 250 , 0, 0 ) ) ; show_health    = big_font.render(str(health).strip()     + " / "  + str( max_health ).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation = big_font.render(str(radiation ).strip() + " / "  + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) ) ; cursor = pg.image.load( 'Interface/icons/refresh_icon.png' ) ; pg.display.update()
        if keys [screenshot_btn ] : make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!') ; print('Screenshot saved ! ')
        if keys [load_game_btn  ] : load_game() #load game
        if keys [save_game_btn  ] : save_game() #save game
        if keys [pg.K_f] : fuel += 1 ; show_fuel = big_font.render('Fuel  : ' + str(fuel)    , False , small_font_color )

    if keys [pg.K_g  ] and keys[pg.K_LCTRL]  : toggle_god_mode() ;  spawn_sound.play() #GOD MODE - no damage , no limit etc
    if keys[back_btn]  : bg_image = bg_images[ random.randint( 0 , len(bg_images) - 1 ) ] ; game_state = 'Main menu'

    mini_map_keyboard_controls()
    
    mini_map_surf.fill((minimapBGcolor))
    screen.fill( (BGcolor) )
    start()
    
    mouse_visible = False ; cursor = pg.image.load( 'Interface/icons/Select/0.png' ) ; screen.blit( cursor , ( pos[ 0 ] - mouse_horizontal_offset , pos[ 1 ]  - mouse_vertical_offset )) ; calc_dist = math.sqrt( (( x_2_list - x_1_list   * hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list * hero_checkpoint_offset_y) ** 2 ) /100) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )
    
    for i in range(len(Companions_file1)) : 
        if game_state == 'Play' and dialoge_started == 1 and pos[0] >=  -camera.rect[0] + int(Companions_file1[i].split(',')[0])  and\
            pos[0] <= -camera.rect[0] + int(Companions_file1[i].split(',')[0]) + Companions_images_list[i].get_width() and\
                  pos[1] >=  -camera.rect[1] + int(Companions_file1[i].split(',')[1])  and pos[1] <=  -camera.rect[1] + int(Companions_file1[i].split(',')[1]) +  Companions_images_list[i].get_height():
            
            for i in range(len(actions_file1)) :
                 dialoge_surf.blit(actions_list[i] , ( 10 , 10 + i * 20  ))
                 frame = pg.draw.rect(dialoge_surf , ( Button_frame_color ) , (10 , 10 + action_counter  * 20 , 90 , 20 ) , 2 , 2 )
                 screen.blit(dialoge_surf , (hero_x , hero_y - 150  ))

    if game_state != 'Play' : show_game_state = big_font.render(str(game_state) , False , small_font_color) ; screen.blit( show_game_state ,  (game_state_x , game_state_y))
    
    for i in range(len(main_menu_file1)):
        if game_state == 'Main menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(crafts_file1)):
        if game_state == 'Crafting'  and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i

    for i in range(len(saves_file1)):
        if game_state == 'Saves'     and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(Hero_types)):
        if game_state == 'character select menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(items_max):    
        if game_state == 'Trade menu' and pos[0] >= int(screen_width) / 2 - button_width and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(game_modes1)):
        if game_state == 'game mode select' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
    
    for x in range(minimap_grid_width):
        for y in range(minimap_grid_height):
            pg.draw.rect(mini_map_surf , (cell_color) , ( cell_size * x , cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
            
    pg.display.update()    

    #for i in range(len(items_file1)):
    #        if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images_list[i].get_width() and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images_list[i].get_height():
    #            action = 'Pickup'
    #            if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) <= items_max:
    #                pickup_sound.play() ; pickup_sound_num += 0.5 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')
    #                hero_inventory_images.append(items_images_list[i])
    #            if pickup_sound_num >= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) - 1: pickup_sound_num = 0
    #            if len(hero_inventory_images) >= items_max : inv_is_full_sound.play()