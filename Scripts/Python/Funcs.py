import pygame as pg
from Settings import *
import pyautogui
from time import *
import logging
pg.init()

dark_level = 0 ; max_dark_level  = 100 ; volume_levels = 10 ; settings_values = 5

bigfont = 30 ; smallfont = 15 ; font_name = 'arial' ; big_font_color = ( 250 , 0 , 0 ) ; small_font_color  = ( 250 , 0 , 0 ) ; change_font_color = ( 0 , 250 , 0 ) ; big_font = pg.font.SysFont(font_name , bigfont) ; small_font = pg.font.SysFont(font_name , smallfont)

languages = os.listdir('txt/langs/') ; lang_num = 2 ; language = languages[lang_num]

bg_num    = 1 ; wallpapers_dir = os.listdir('Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/') ; wallpaper  = wallpapers_dir[bg_num]

#sounds
welcome_speech_dir = os.listdir('Audio/sounds/welcome/') ; enemy_sounds_dir = os.listdir('Audio/sounds/roar/') ; pickup_sounds_dir = os.listdir('Audio/sounds/pickup/')

sounds_dir = os.listdir('Audio/sounds/')

#music
soundtracks = os.listdir('Audio/enviroment/') ; switch_music = 1 ; music = soundtracks[switch_music] ; show_song_name = small_font.render(str(music) , False , ( 250 , 0 , 0 ) ) ; pg.mixer.music.load('Audio/enviroment/' + str(music)) ; minimap_border_offset = 10 ; minimap_object_offset = 0 ; minimap_object_offset1 = 0

step_sound_num     = 1 ; step_sound   = pg.mixer.Sound('Audio/sounds/steps/grass/'       + str(step_sound_num)   + '.mp3')
rifle_sound_num    = 0 ; rifle_sound  = pg.mixer.Sound('Audio/sounds/firegun/automatic/' + str(rifle_sound_num)  + '.mp3')
spawn_sound_num    = 0 ; spawn_sound  = pg.mixer.Sound('Audio/sounds/spawn/'             + str(spawn_sound_num)  + '.mp3')
scream_sound_num   = 0 ; scream_sound = pg.mixer.Sound('Audio/sounds/screams/far/'       + str(scream_sound_num) + '.mp3')
death_sound_num    = 0 ; death_sound  = pg.mixer.Sound('Audio/sounds/death/'             + str(death_sound_num)  + '.mp3')
pickup_sound_num   = 0 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/'            + str(pickup_sound_num) + '.mp3')
enemy_sound_num    = 0 ; enemy_sound  = pg.mixer.Sound('Audio/sounds/roar/'              + str(enemy_sound_num)  + '.mp3')
click_sound_num    = 0 ; click_sound  = pg.mixer.Sound('Audio/sounds/clicks/'            + str(click_sound_num)  + '.mp3')
welcome_num        = 0 ; welcome           = pg.mixer.Sound('Audio/speech/langs/'                   + str(language)           + '/welcome/' + str(int(welcome_num)) + '.mp3')
inv_full_sound_num = 0 ; inv_is_full_sound = pg.mixer.Sound('Audio/sounds/massages/Full inventory/' + str(inv_full_sound_num) +'.mp3')

bg_images   = []
for i in range(len(wallpapers_dir)) :
     if i not in bg_images : bg_images.append(pg.image.load( 'Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/' + str(i) + '.png'))

Icons_dir = os.listdir('Interface/Icons/')

for i in range(len(Icons_dir)) : pass

#icons
health_icon_num    = 0 ; health_icon    = pg.image.load('Interface/Icons/Health/'          + str(health_icon_num)    + '.png')
ammo_icon_num      = 0 ; ammo_icon      = pg.image.load('Interface/Icons/Ammo/'            + str(ammo_icon_num)      + '.png') 
armor_icon_num     = 0 ; armor_icon     = pg.image.load('Interface/Icons/Armor/'           + str(armor_icon_num)     + '.png')
radiation_icon_num = 0 ; radiation_icon = pg.image.load('Interface/Icons/Radiation/'       + str(radiation_icon_num) + '.png')
energy_icon_num    = 0 ; energy_icon    = pg.image.load('Interface/Icons/Energy/'          + str(radiation_icon_num) + '.png')
sound_icon_num     = 0 ; sound_icon     = pg.image.load('Interface/Icons/Music/'           + str(sound_icon_num)     + '.png')
cancel_icon_num    = 0 ; cancel_icon    = pg.image.load('Interface/buttons/cancel/'        + str(cancel_icon_num)    + '.png')

cancel_icon_x , cancel_icon_y = int(screen_width) - 50 , 50

hero_x , hero_y = int(screen_width) / 2 - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

item_offset = 0 ; active_button = 0 ; active_button1 = 0 ; crafts_on_page = 10 ; characters_on_page = 10 ; players_on_page = 10 ; button_width = 250 ; button_height = bigfont ; button_border_radius = 5

hero_image1 = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png') ; heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')

mouse_horizontal_offset = 5 ; mouse_vertical_offset = 5 ; minimap_horizontal_offset = 0 ; minimap_vertical_offset = 0 ; fov = 100 ; minimap_opacity = 0 ; interface_opacity = 0 

Button_color = (45 , 45 , 45) ; minimap_border_color = (45 , 45 , 45) ; Button_frame_color = (255 , 0 , 0) ; cell_color = ( 45  , 45 , 45 )

game_state_x   = int(screen_width) / 2 - int(len(game_state) * bigfont / 3) ; game_state_y = 100
game_title_x   = 100      ; game_title_y        = 100
Game_version_x = 10       ; Game_version_y      = int(screen_height) - bigfont
Game_Author_x  = 10       ; Game_Author_y       = int(screen_height) - bigfont 
Game_created_date_x  = 10 ; Game_created_date_y = 10 
Game_update_x  = 10       ; Game_update_y       = 10 

back_btn = pg.K_ESCAPE ; save_game_btn = pg.K_F5 ; backpack_btn1 = pg.K_b ; backpack_btn2 = pg.K_b ; load_game_btn = pg.K_F3

change_settings_value = 0 ; fps_1 = 4 ; 
herojump , herojumpcounter = False , 10 ; jump_height = 6 # you can not jump , jump height

def make_screenshot() :
    screenshots = 1 ; screenshot = pyautogui.screenshot() 
    for i in range(screenshots)  : screenshot.save( 'screenshots/' + str(d1.year) + ' - ' + str(d1.month) + ' - ' + str(d1.day) + ' - ' + str(d1.hour) + ' - ' +  str(d1.minute) + ' - ' + str(d1.second) + '.png' )

def save_game_and_quit() :saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])) ; saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )
def toggle_god_mode()    : global print_god_mode , god_mode ; god_mode = 0 ; print_god_mode = print('GOD MODE ACTIVATED!')

def load_game() : saves_file_mode = 'r' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.close() ; logging.info(msg = 'GAME LOADED!' ) ; print('Game loaded!')
def save_game() : saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  );saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; print('GAME SAVED!')

def draw_menu():
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0   , 0  ))
        screen.blit(show_game_title    , ( int(screen_width)  /  2 - len(Game_title)  * smallfont / 2  , 10))
        screen.blit( show_update       , ( int(screen_width)  /  2 - len(update_name) * smallfont / 2  , 50))    
        screen.blit(show_game_version  , (  10 , int(screen_height) - bigfont))
        screen.blit( show_author       , (  0  , 10 ))
        screen.blit( show_created_date , (  0  , 35 ))
        screen.blit( cancel_icon , ( cancel_icon_x,cancel_icon_y))
        game_state_x = int(screen_width) / 2 - int(len(game_state) * bigfont / 3) ; game_state_y = 100

vihicle_sit = 0