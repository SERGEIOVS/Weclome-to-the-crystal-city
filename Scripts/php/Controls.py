import pygame as pg ; from Settings import * ; from PIL import Image ; from Units import * ; import logging ; from Vihicles import * ; import pyautogui ; from Buildings import * ; import math
import time ; from Funcs import *

pressed = pg.mouse.get_pressed() ; pos = pg.mouse.get_pos() ; clock = pg.time.Clock() ; FPS = 60 ; clock.tick(FPS)

hide_nicknames = 0

#land level
ground = 1 ; floor = 0

#sounds
welcome_speech_dir = os.listdir('Audio/sounds/welcome/') ; enemy_sounds_dir   = os.listdir('Audio/sounds/roar/') ; pickup_sounds_dir   = os.listdir('Audio/sounds/pickup/')

step_sound   = pg.mixer.Sound('Audio/sounds/knoks/knok_1.mp3')
rifle_sound  = pg.mixer.Sound('Audio/sounds/firegun/auto_firing(3 times)_1.mp3')
spawn_sound  = pg.mixer.Sound('Audio/sounds/spawn/bell.mp3')
scream_sound = pg.mixer.Sound('Audio/sounds/screams/far scream.mp3')
death_sound  = pg.mixer.Sound('Audio/sounds/death/bell.mp3')

pickup_sound_num = 0 ; pickup_sound  = pg.mixer.Sound('Audio/sounds/pickup/' + str(pickup_sound_num) + '.mp3') ; inventory_is_full_sound = pg.mixer.Sound('Audio/sounds/inventory_is_full.mp3')

welcome_num = 0 ; welcome = pg.mixer.Sound('Audio/speech/langs/'+ str(language) +'/welcome/' + str(int(welcome_num)) + '.mp3')

enemy_sound_num = 0 ; enemy_sound = pg.mixer.Sound('Audio/sounds/roar/' + str(welcome_num) + '.mp3')

#music
soundtracks = os.listdir('Audio/enviroment/')
switch_music = 1
music = soundtracks[switch_music]
show_song_name = small_font.render(   str(music) , False , ( 250 , 0 , 0 ) )
pg.mixer.music.load('Audio/enviroment/' + str(music))

minimap_border_offset = 10

bg_images = [

pg.image.load( 'wallpapers/0.png' ) , pg.image.load( 'wallpapers/1.png' ) ,
pg.image.load( 'wallpapers/2.png' ) , pg.image.load( 'wallpapers/3.png' )

]

health_icon    = pg.image.load('Interface/icons/health_icon.png')
ammo_icon      = pg.image.load('Interface/icons/pistol_ammo_icon.png')
armor_icon     = pg.image.load('Interface/icons/armor_icon.png')
radiation_icon = pg.image.load('Interface/icons/radiation_green.png')
energy_icon    = pg.image.load('Interface/icons/energy_icon.png')

god_mode = 0
hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
item_offset = 0

def toggle_god_mode() : global print_god_mode ; print_god_mode = print('GOD MODE ACTIVATED!') ; spawn_sound.play()

def draw_mini_map():
    if show_map == 1:
        for i in range( len ( islands_file1 ) ) : pg.draw.rect(mini_map_surf , (100 , 50 , 0) , (minimap_border_offset + int(islands_file1[ i ].split(',')[0]) / (100 * map_scale)+ minimap_border_offset ,  minimap_border_offset + int(islands_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_border_offset ,  10 / map_scale ,  10 / map_scale ))
        
        for i in range( len ( buildings_file1 ) ) :
             if show_buildings == 1 : pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) + minimap_border_offset , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_border_offset  ,  10 / map_scale, 10 / map_scale  ))
            
        for i in range( len ( vihicles_file1 ) ) : pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(vihicles_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset , int(vihicles_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset , 5 / map_scale , 3 / map_scale ))
        
        for i in range( len ( items_file1 ) ) :
             if show_items == 1 : pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset , int(items_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset , 1 / map_scale , 1 / map_scale ))

        #hero mini map marker
        hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , ( minimap_border_offset   + camera.rect[0] / (100 * map_scale) + minimap_border_offset ,  camera.rect[1] / (100 * map_scale) + minimap_border_offset  ) , 1 / map_scale )        
        
        screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )

        pg.draw.rect(screen , ( 255 , 0 , 0 ) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset  , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)

def toggle_settings():
    if game_state == 'settings':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )
        screen.blit(show_game_title , ( int(screen_width)  /  2 - len(Game_title) * smallfont / 2  , 10) )
        screen.blit( show_update  ,   (  int(screen_width) /  2 - len(update_name) * smallfont / 2 , 50) )
        screen.blit(show_game_version , ( 10 , 575 ) )
        screen.blit( show_author  , (  0 , 10 ))
        screen.blit( show_created_date , (  0 , 35 ))

        for i in range(len(settings_file1)):
            #drawing a rects for each button
            pg.draw.rect(screen   , (45 , 45 , 45) , ( int(screen_width) / 2 - bigfont * 10 / 2 , bigfont + int(screen_height) / bigfont + i * 40 + bigfont , bigfont * 10 / 2 , bigfont ))
            pg.draw.rect(screen   , (45 , 45 , 45) , ( int(screen_width) / 2 + smallfont , bigfont + int(screen_height) / bigfont  + bigfont , 200 , 150))
            pg.draw.line(screen   , (0 , 0 ,   0 ) , [ int(screen_width) / 2 + bigfont , bigfont + int(screen_height) / bigfont + 40] , [ int(screen_width) / 2 + bigfont + 100 , bigfont + int(screen_height) / bigfont + 40] , 1 )
            pg.draw.circle(screen , (255 , 0 , 0 ) , ( int(screen_width) / 2 + bigfont , bigfont + int(screen_height) / bigfont + 40 ) , 1)
            pg.draw.circle(screen , (255 , 0 , 0 ) , ( int(screen_width) / 2 + bigfont + 100 , bigfont + int(screen_height) / bigfont + 40 )  , 1)

            #drawing a text for a main menu
            screen.blit(settings[i] , ( int(screen_width) /  2 - bigfont * 10 / 2 , bigfont + int(screen_height) / bigfont + i * 40 + bigfont , bigfont * len(str(settings[i])) / 4 , bigfont ))

def toggle_main_menu():
    if game_state == 'main_menu':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )
        screen.blit(show_game_title , ( int(screen_width)  /  2 - len(Game_title)  * smallfont / 2 , 10) )
        screen.blit( show_update  ,   (  int(screen_width) /  2 - len(update_name) * smallfont / 2 , 50) )
        screen.blit(show_game_version , ( 10 , 575 ) )
        screen.blit( show_author  , (  0 , 10 ))
        screen.blit( show_created_date , (  0 , 35 ))

        for i in range(len(main_menu_file1)):

            #drawing a rects for each button
            pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  2 - len(main_menu_file1[i]) * smallfont , bigfont + int(screen_height) / bigfont + i * 40 + bigfont , bigfont * len(str(main_menu[i])) / 4 , bigfont + 5 ))
            
            #drawing a frame for an active button 
            pg.draw.rect(screen , (255 , 0 , 0) ,  ( int(screen_width) /  2 - len(main_menu_file1[i]) * smallfont , bigfont + int(screen_height) / bigfont + 0  * 40 + bigfont , bigfont * len(str(main_menu[i])) / 4 , bigfont + 5 ) , 2)

            #drawing a text for a main menu
            screen.blit(main_menu[i] ,             ( int(screen_width) /  2 - len(main_menu_file1[i]) * smallfont + smallfont , bigfont + int(screen_height) / bigfont + i * 40 + bigfont , bigfont * len(str(main_menu[i]) ) / 4 , bigfont ))
            

def start():
    if game_state == 'saving':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )
        
        for i in range(len(saves_file1)):        #drawing a buttons for a saves menu

                pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  2 - 100 , int(screen_height) / 10 + i * 40 , bigfont * len(str(saves_list[i])) / 2 , bigfont )) ; screen.blit(saves_list[i] , ( int(screen_width) /  2 - 70 , int(screen_height) / 10 + i * 40 , 100 , bigfont ) )
    
    if game_state == 'crafting':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )

        for i in range(len(crafts_file1)):
                
                #drawing a buttons for a crafts menu
                pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  2 - len(crafts_file1[i]) * len(crafts_file1[i]) / 10 , int(screen_height) / 10 + i * 40 , len(crafts_file1[i]) * len(crafts_file1[i]) / 1.8 - bigfont , bigfont))
                
                pg.draw.rect(screen , (255 , 0 , 0 ) , ( int(screen_width) /  2 - len(crafts_file1[i]) * len(crafts_file1[i]) / 10 , int(screen_height) / 10 + 0 * 40 , len(crafts_file1[i]) * len(crafts_file1[i]) / 1.8 - bigfont , bigfont) , 2 )

                screen.blit(crafts_list[i] , ( int(screen_width) /  2 - 70 , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
    
    toggle_settings() ; toggle_main_menu()

    if game_state == 'play':        
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
    
        if ground == 1:
            for i in range( len ( islands_file1 ) ) : 
                 if camera.rect[0] + int(screen_width) - 200 >= int(islands_file1[i].split(',')[0]):
                    screen.blit( islands_images[ i ] , ( -camera.rect[ 0 ] + int(islands_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(islands_file1[i].split(',')[1] ) ) )
            
            for i in range( len ( vihicles_file1 ) ) : 
                 if camera.rect[0] + int(screen_width) - 200 >= int(vihicles_file1[i].split(',')[0]):
                    screen.blit( vihicles_images_list[i] , ( -camera.rect[ 0 ] + int(vihicles_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(vihicles_file1[i].split(',')[1]) ) ) 
        
            for i in range( len(buildings_file1 )) : 
                 if camera.rect[0] + int(screen_width) - 200 >= int(buildings_file1[i].split(',')[0]):
                    screen.blit( Buildings_images_list[i] , ( -camera.rect[ 0 ] + int(buildings_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(buildings_file1[ i ].split(',')[1] ) ))

        for i in range(len(checkpoints_file1)) : pg.draw.circle(screen , (255 , 0 , 0 ) , (-camera.rect[0] + int(checkpoints_file1[i].split(',')[0]) + 50 , -camera.rect[1] + int(checkpoints_file1[i].split(',')[1]) + 180) , 50 , 1 )

        for i in range(len(Companions_file1)) : 
             if camera.rect[0] + int(screen_width) - 200 >= int(Companions_file1[i].split(',')[0]):
                screen.blit( Companions_images_list[i]  , ( -camera.rect[ 0 ] + int(Companions_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Companions_file1[i].split(',')[1])  ) )
        
        for i in range(len(players_file1)):
                if hide_nicknames == 0:

                    #drawing anicknames(text)
                    pg.draw.rect(screen , (45 , 45 , 45) , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) + bigfont , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , len(nicknames_file1[i]) * len(nicknames_file1[i]) - len(nicknames_file1[i]) , smallfont))
                    
                    screen.blit(nicknameslist[i] , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) + bigfont , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , 100 , bigfont ) )
                    
                    screen.blit(new_quest , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0])  , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1]) - 20 , 100 , bigfont ) )
        
        #drawing a players(images)        
        for i in range(len(players_file1)) : 
             if camera.rect[0] + int(screen_width) - 100 >= int(players_file1[i].split(',')[0]):
                screen.blit( unit_image , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1])  ) )
        
        for i in range(len(Enemies_file1)):
            if Enemies_images_list[i] not in killed_units:
                if camera.rect[0] + int(screen_width) - 200 >= int(Enemies_file1[i].split(',')[0]):
                    #drawing a players(images)
                    screen.blit( Enemies_images_list[i] , ( -camera.rect[ 0 ] + int(Enemies_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Enemies_file1[i].split(',')[1])  ) )
        
        #drawing a text for a quests menu
        for i in range(len(quests_file1)) : quests_surf.blit(quests_list[i] , (5 , 5 + bigfont / 2 * i * 1.6 ) )

        #for i in range(len(items_file1)) :
        #            for y in range(len(items_file1)) :
        #                if items_images_list[i] not in hero_inventory_images : screen.blit( items_images_list[ i ] , ( -camera.rect[ 0 ] + int(items_file1[i].split(',')[0]) + item_offset + y * 100, -camera.rect[ 1 ] + int(items_file1[i].split(',')[1] ) ) )
        
        for i in range(len(items_file1)) :
            for y in range(int(items_file1[i].split(',')[0])):
                if camera.rect[0] + int(screen_width) - 200 >= int(items_file1[i].split(',')[0]):
                    if items_images_list[i] not in hero_inventory_images : screen.blit( items_images_list[ i ] , ( -camera.rect[ 0 ] + int(items_file1[i].split(',')[0]) + int(items_file1[i].split(',')[2]) * y * 10  , -camera.rect[ 1 ] + int(items_file1[i].split(',')[1] ) ) )
    

        inteface_surf.set_alpha(50) ; quests_surf.set_colorkey(( 0 , 0 , 0 )) ; dialoge_surf.set_alpha(150)

        for i in range(len(hero_inventory_file1)):
            pg.draw.rect(screen , ( 45 , 45 , 45 ) , ( int(screen_width) / 2 - cell_size * i + 5  + cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 2 ) #drawing a inventory cells
            pg.draw.rect(screen , ( 255 , 0 , 0 ) , ( int(screen_width) / 2 - cell_size * len(hero_inventory) / 2 + 5 - cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 2 ) #drawing a inventory cell_frame for a selected item in inventory
        screen.blit(hero_inventory[item] , (int(screen_width ) / 2 - cell_size * len(hero_inventory) / 2 , int(screen_height) - cell_size * 2  )) #drawing a title of the item in inventory

        if saving_type == 'default' : screen.blit( hero_image , ( hero_x , hero_y ) )

        dark_surf.fill(dark_surf_color) ; dialoge_surf.fill((0 , 0 , 0 )) ; dark_surf.set_alpha(dark_level)

        screen.blit(dark_surf , ( 0 , 0 )) 
        screen.blit(inteface_surf , ( 0 , int(screen_height ) - 200 ))
        screen.blit(quests_surf , ( int(screen_width) - 200 , int(screen_height ) - 200 ))
        quests_surf.fill((quest_surf_color))

        #drawing a road to the checkpoint
        pg.draw.line(screen   , (0   , 0 , 0 ) ,    [ -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y ] , [ -camera.rect[ 0 ] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[ 1 ] + int(checkpoints_file1[0].split(',')[1])] , 1 )
        
        #segmented road to the checkpoint 
        for i in range(int(calc_dist) // 10 ) : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) + i * 10 , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1]) - i * 10) , 5)
                          
        #drawing a circle at the hero x and hero y
        pg.draw.circle(screen , (255 , 0 , 0) ,     ( -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[1] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y) , checkpoint_size , 1 )
        
        #drawing a circle at the checkpoint x and checkpoint y
        pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        
        draw_mini_map()

        screen.blit(show_hero_armor , ( bigfont , bigfont / 2 + 400 )) , screen.blit(armor_icon      , ( 0 , bigfont / 2 + 430 ))
        screen.blit(show_health     , ( bigfont , bigfont / 2 + 430 )) , screen.blit(health_icon     , ( 0 , bigfont / 2 + 400 ))
        screen.blit(show_ammo       , ( bigfont , bigfont / 2 + 460 )) , screen.blit(ammo_icon       , ( 0 , bigfont / 2 + 460 ))
        screen.blit(show_radiation  , ( bigfont , bigfont / 2 + 490 )) , screen.blit(radiation_icon  , ( 0 , bigfont / 2 + 490 ))
        screen.blit(show_energy     , ( bigfont , bigfont / 2 + 520 )) , screen.blit(energy_icon     , ( 0 , bigfont / 2 + 520 ))

        screen.blit(show_money      , ( 0 , bigfont / 2 + 550 ))

        if blit_distance == 1 : screen.blit(show_distance  , ( hero_x , hero_y - bigfont ) )

        for i in range(len(hero_inventory_images)) : screen.blit( hero_inventory_images[i] , ( int(screen_width) / 2 - cell_size * i + 10  + cell_size   , int(screen_height) - cell_size / 2 - items_images_list[i].get_height() / 2 ) )

herojump , herojumpcounter = False , 10 ; jump_height = 6 # you can not jump , jump height

fps_1 = 4

run = True

mouse_horizontal_offset   = 5 ; mouse_vertical_offset   = 5 ; minimap_horizontal_offset = 0 ; minimap_vertical_offset = 0

logging.info( msg = 'GAME STARTED!' )

while run :
    for i in range(len(players_file1)) :
        if camera.rect[0] + int(screen_width) - 100 >= int(players_file1[i].split(',')[0]):
            if unit_animation  >= 0 and unit_animation <= len(os.listdir('Objects/Characters/Players/2/idle/left/')) - 1 :
                pg.image.load('Objects/Characters/Players/' + '2' + '/' + str(state) + '/left/' + str(unit_animation) + '.png')
                unit_animation += 1 ; unit_image  = pg.image.load('Objects/Characters/Players/' + '2' + '/' + str(state) + '/left/' + str(unit_animation) + '.png')
                
                #drawing a players(images)
                for i in range(len(players_file1)) : screen.blit( unit_image , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1])  ) )
                
                if unit_animation  >= len(os.listdir('Objects/Characters/Players/2/idle/left/')) - 1 : 
                    unit_animation = 0  ; unit_image = pg.image.load('Objects/Characters/Players/' +'2' + '/' + str(state) + '/left/' + str(unit_animation) + '.png')
                    unit_animation += 1 ; unit_image = pg.image.load('Objects/Characters/Players/' +'2' + '/' + str(state) + '/left/' + str(unit_animation) + '.png')
                    
                    #drawing a players(images)
                    for i in range(len(players_file1)) : screen.blit(unit_image , ( -camera.rect[ 0 ] + int(players_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(players_file1[i].split(',')[1])  ) )


    if dark_level <= max_dark_level : dark_level += 0.1 ; clock.tick(FPS / fps_1) ; unit_speed += 0.1

    if game_state == 'play' and camera.rect[0] >= 0:
            hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
            if animation <= len(hero_animations_dir) - 1:
                clock.tick(FPS / fps_1)
                animation += 1
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero = 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )
            
            if animation >= len(hero_animations_dir) - 1 :
                animation = 0
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero_speed = 4
                clock.tick(FPS / fps_1)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )
                
    vector = [ 0 , 0 ]
    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION : pos = pg.mouse.get_pos()
        
        if game_state == 'main_menu' : cursor = pg.image.load( 'Interface/icons/cursor/select.png' ) ; mouse_visible = True
        if pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images_list[i].get_width() \
        and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images_list[i].get_height():
            action = 'Pickup'
            print('pickup')

        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and int(ammo) > 0 and game_state == 'play':
                ammo -= 1
                gun_shot = pg.mixer.Sound( 'Audio/sounds/firegun/single_1.mp3' ) ; gun_shot.play()
                show_hero_armor = big_font.render('armor : ' + str( armor ).strip() + " / " +  str( max_armor ).strip() , False    , ( 250 , 0, 0 ) )
                show_ammo       = big_font.render('ammo : ' + str(ammo ).strip() + " / " + str( max_ammo * mags ).strip() , False  , ( 250 , 0 , 0 ) )
                show_health     = big_font.render('health : ' + str( health ).strip() + " / " + str( max_health ).strip() , False  , ( 255 , 0 , 0 ) )
                show_radiation  = big_font.render('radiation : ' + str( radiation ).strip() + " / " + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) )
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            if event.button == 1 and int(ammo) <= 1 and game_state == 'play':
                show_hero_armor = big_font.render('armor : '     + str(armor ).strip() + " / " +  str( max_armor ).strip() , False , ( 250 , 0, 0 ) )
                show_ammo       = big_font.render('ammo : '      + str(ammo ).strip() + " / " + str( max_ammo * mags ).strip() , False , ( 250 , 0 , 0 ) )
                show_health     = big_font.render('health : '    + str(health ).strip() + " / " + str( max_health ).strip() , False , ( 255 , 0 , 0 ) )
                show_radiation  = big_font.render('radiation : ' + str(radiation ).strip() + " / " + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) )
                no_ammo = pg.mixer.Sound('Audio/sounds/firegun/no_ammo.wav' )
                no_ammo.play()
                
            for i in range(len(Companions_file1)):
                    if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(Companions_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(Companions_file1[i].split(',')[0]) + Companions_images_list[i].get_width() \
                    and pos[1] >=  -camera.rect[1] + int(Companions_file1[i].split(',')[1])  and pos[1] <=  -camera.rect[1] + int(Companions_file1[i].split(',')[1]) + Companions_images_list[i].get_height():
                        action = 'Talk'
                        if welcome_num >= 0 and welcome_num <= len(welcome_speech_dir) - 1:
                            welcome.play()
                            welcome_num += 0.5
                            welcome = pg.mixer.Sound('Audio/speech/langs/' + str(language) +'/welcome/' + str(int(welcome_num)) + '.mp3')
                        if welcome_num >= len(welcome_speech_dir) - 1:
                            welcome_num = 0
                            welcome.play()
                            welcome_num += 0.5
                            welcome = pg.mixer.Sound('Audio/speech/langs/' + str(language) + '/welcome/' + str(int(welcome_num)) + '.mp3')

            for i in range(len(Enemies_file1)):
                    if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0]) + Enemies_images_list[i].get_width() \
                        and pos[1] >=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) + Enemies_images_list[i].get_height():
                        action = 'Talk'
                        if welcome_num >= 0 and enemy_sound_num <= len(enemy_sounds_dir) - 1:
                            enemy_sound.play()
                            enemy_sound_num += 0.5
                            enemy_sound = pg.mixer.Sound('Audio/sounds/roar/' + str(int(enemy_sound_num)) + '.mp3')
                        if enemy_sound_num >= len(enemy_sounds_dir) - 1:
                            enemy_sound_num = 0
                            enemy_sound.play()
                            enemy_sound_num += 0.5
                            enemy_sound = pg.mixer.Sound('Audio/sounds/roar/' + str(int(enemy_sound_num)) + '.mp3')
                    
                    if event.button == 1 and  pos[0] >=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(Enemies_file1[i].split(',')[0]) + Enemies_images_list[i].get_width() \
                        and pos[1] >=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(Enemies_file1[i].split(',')[1]) + Enemies_images_list[i].get_height():
                            enemy_sound.play()
                            killed_units.append(Enemies_images_list[i])
            
            for i in range(len(items_file1)):
                    if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images_list[i].get_width() \
                    and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images_list[i].get_height():
                        
                        action = 'Pickup'
                        if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) <= items_max:
                            pickup_sound.play()
                            pickup_sound_num += 0.5
                            pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')
                            hero_inventory_images.append(items_images_list[i])

                        if pickup_sound_num >= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) - 1 >= items_max : pickup_sound_num = 0

                        if len(hero_inventory_images) >= items_max : inventory_is_full_sound.play()

        if event.type == pg.QUIT : run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_a] and game_state == 'play' and camera.rect[0] >= 0:
            state = 'go'
            turn = 'left'
            hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
            hero_speed = 4
            vector[ 0 ] -= hero_speed
            hero_checkpoint_offset_x -= hero_speed
            calc_dist = math.sqrt( (( x_2_list - x_1_list -hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ))
            show_distance = small_font.render('Distance : ' + str(int(calc_dist) // 100) + ' m' , False , small_font_color )
            #print('Distance : ' , int(calc_dist) // 100 , 'hero offset x : ' , hero_checkpoint_offset_x , 'hero offset y : ' , hero_checkpoint_offset_y)
            blit_action = 0
            mini_map_surf.fill((minimapBGcolor))
            
            if animation <= len(hero_animations_dir) - 1:
                clock.tick(FPS / fps_1)
                animation += 1
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero            = 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image      = pg.image.load('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage       = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

            if animation >= len(hero_animations_dir) - 1 :
                animation = 0 ; state = 'go' ; turn = 'left'
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero_speed = 4
                clock.tick(FPS / fps_1)
                animation += 1
                hero       ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage  = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )
    
    if keys[pg.K_s]  and keys[pg.K_LSHIFT]  and game_state == 'main_menu' : game_state = 'saving'
    
    if keys[pg.K_s] and game_state == 'main_menu':game_state = 'settings' ; toggle_settings()

    if keys[pg.K_e] and game_state == 'play' and camera.rect[1] >= 0 : unit_moving = 0

    if keys[pg.K_q] and game_state == 'play' : game_state = 'quests_menu'

    if keys[pg.K_d] and game_state == 'play' and camera.rect[0] <= map_width:state = 'go' ; turn = 'right';hero_speed = 4 ;vector[ 0 ] += hero_speed ; hero_checkpoint_offset_x += hero_speed
            
    mini_map_surf.fill((minimapBGcolor))
    calc_dist = math.sqrt( (( x_2_list - x_1_list + hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list + hero_checkpoint_offset_y) ** 2 ))
    show_distance = small_font.render('Distance : ' + str(int(calc_dist) // 100) + ' m' , False , small_font_color )
    #print('Distance : ' , int(calc_dist) // 100 , 'hero offset x : ' , hero_checkpoint_offset_x , 'hero offset y : ' , hero_checkpoint_offset_y)
    hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if not( herojump ) :
        if keys[pg.K_w] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] -= hero_speed ; hero_checkpoint_offset_y -= hero_speed
            calc_dist = math.sqrt( (( x_2_list - x_1_list   + hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list + hero_checkpoint_offset_y) ** 2 ))
            show_distance = small_font.render('Distance : ' + str(int(calc_dist) // 100) + ' m' , False , small_font_color )
            #print('Distance : ' , int(calc_dist) // 100 , 'hero offset x : ' , hero_checkpoint_offset_x , 'hero offset y : ' , hero_checkpoint_offset_y)
            hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
  
        if keys[pg.K_s] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] += hero_speed ; hero_checkpoint_offset_y += hero_speed
            calc_dist = math.sqrt( (( x_2_list - x_1_list   + hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list + hero_checkpoint_offset_y) ** 2 ))
            show_distance = small_font.render('Distance : ' + str(int(calc_dist) // 100) + ' m' , False , small_font_color )
            #print('Distance : ' , int(calc_dist) // 100 , 'hero offset x : ' , hero_checkpoint_offset_x , 'hero offset y : ' , hero_checkpoint_offset_y)
            mini_map_surf.fill((minimapBGcolor))
            hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

        if keys[pg.K_SPACE] and game_state == 'play': herojump = True #можно прыгать
        if vector != [ 0 , 0 ] and game_state == 'play' : camera.move(vector) ##  Если игрок ходил
    else:
        if herojumpcounter >= -jump_height :
            if herojumpcounter < 0 : hero_y += ( herojumpcounter ** 2 ) / 2 ; clock.tick(FPS / 2)
            else : hero_y -= ( herojumpcounter ** 2 ) / 2 ; herojumpcounter -= 1 ; clock.tick(FPS / 2)
        else : herojump = False ; herojumpcounter = jump_height

    if keys [pg.K_r] and game_state == 'play' : 
        hero_status = 'reload'
        if hero_status =='reload' and mags >= 1:
            reloadsound = pg.mixer.Sound( 'Audio/sounds/firegun/reload.mp3' ) ; 
            reloadsound.play()
            mags -= 1
            hero_file_name = 'txt/hero.txt' ; hero_file_mode = 'w' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file.write(str(mags)) ; hero_file.close()
            ammo = max_ammo  ; 
            show_ammo      = big_font.render(str(ammo) + '/' + str( ammo * mags ) , False , colors[2] )
            show_armor     = big_font.render(str(armor).strip() + " / " +  str( max_armor ).strip() , False , ( 250 , 0, 0 ) )
            show_ammo      = big_font.render(str(ammo).strip() + " / " + str( max_ammo * mags ).strip() , False , ( 250 , 0 , 0 ) )
            show_health    = big_font.render(str(health).strip() + " / " + str( max_health ).strip() , False , ( 255 , 0 , 0 ) )
            show_radiation = big_font.render(str(radiation ).strip() + " / " + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) )

            pg.display.update()
            
    if keys [pg.K_F3] : make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!') ; print('screenshot !')
    
    if keys [pg.K_F12] : save_game_and_quit()#save game and quit game

    if keys [pg.K_F9] : load_game() #load game

    if keys [pg.K_F5] :save_game() #save game 

    if keys [pg.K_p] : game_state = 'play'
    
    if keys [pg.K_s] and game_state == 'main_menu' : game_state = 'saving'
    
    if keys [pg.K_c] and game_state == 'main_menu' : game_state = 'crafting'

    if keys [pg.K_b] : open_backpack = 1

    if keys [pg.K_b]  and keys[pg.K_LSHIFT] : open_backpack = 0
     
    if keys [pg.K_g]  and keys[pg.K_LCTRL] : toggle_god_mode() #GOD MODE-no damage,no limit etc

    if keys [pg.K_ESCAPE] : bg_images[ random.randint( 0 , len(bg_images) - 1 ) ] ; game_state = 'main_menu'

    if keys [pg.K_UP] : show_map = 1
    if keys [pg.K_DOWN] : show_map = 0

    if keys [pg.K_KP_5] : map_size = 1

    if  keys [pg.K_KP_7]:minimap_location = 'left_up'
    if minimap_location == 'left_up' : minimap_x = 0 ; minimap_y = 0

    if keys [pg.K_KP_8] : minimap_location = 'left_up'
    if minimap_location == 'left_up' : minimap_x = 0 ; minimap_y = 0

    if keys [pg.K_KP_9] : minimap_location = 'right_up'
    if minimap_location == 'right_up' : minimap_x = int(screen_width) - int(screen_width) / 3 ; minimap_y = 0

    if keys [pg.K_KP_4] : minimap_location = 'right_down'
    if minimap_location == 'right_down': minimap_x = int(screen_width)  - int(screen_width) / 3 ; minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_6] : minimap_location = 'right_up'
    if minimap_location == 'right_up' : minimap_x = int(screen_width) - int(screen_width) / 3 ; minimap_y = 0     
    
    if keys [pg.K_KP_3] :minimap_location = 'right_down'
    if minimap_location == 'right_down' : minimap_x = int(screen_width)  - int(screen_width) / 3 ; minimap_y = int(screen_height) - int(screen_height) / 3
    
    if keys [pg.K_KP_1] : minimap_location = 'left_down'
    if minimap_location == 'left_down' : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_2] : minimap_location = 'left_down'
    if minimap_location == 'left_down' : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_PLUS]:mini_map_surf.fill((minimapBGcolor)) ; map_scale -= 0.1 ; draw_mini_map()
    if keys [pg.K_KP_MINUS] : mini_map_surf.fill((minimapBGcolor)) ; map_scale += 0.1 ; draw_mini_map()

    if keys [pg.K_ESCAPE]  and open_backpack == 1: open_backpack  = 0
    
    screen.fill( (BGcolor) )
    start()

    mouse_visible = False ; cursor = pg.image.load( 'Interface/icons/cursor/crosshair.png' ) ; screen.blit( cursor , ( pos[ 0 ] - mouse_horizontal_offset , pos[ 1 ]  - mouse_vertical_offset ))

    pg.display.update()