import pygame as pg , datetime
from Units import * ; from Items import * ; import os , math , logging

pg.init() ; pg.font.init()

cwd = os.getcwd()

d1 =  datetime.datetime.today() ; d1 += datetime.timedelta( hours = 0 )

pos = pg.mouse.get_pos()

Game_title = os.path.basename(cwd)
screen = pg.display.set_mode( (int( screen_width) , int(screen_height ) )   )
game_icon = pg.display.set_icon(pg.image.load("Interface/icons/Game icons/Game_icon.png"))
pg.display.set_caption(Game_title)
Game_version = d1.date()
update_name = 'Fear in the dark'
author = 'Thunderman98'
subtitles = 0
cursor_x = pos[0] ; cursor_y = pos[1]

bigfont   = 30 ; smallfont = 15 ; font_name = 'arial'
big_font_color    = ( 250 , 0 , 0 )
small_font_color  = ( 250 , 0 , 0 )
change_font_color = ( 0 , 250 , 0 )
big_font   = pg.font.SysFont(font_name , bigfont) ; small_font = pg.font.SysFont(font_name , smallfont)

languages = os.listdir('txt/langs/') ; language = languages[2]

logpaths = ['logs/info_log.txt' , 'logs/debug_log.txt' , 'logs/warning_log.txt' , 'logs/critical_log.txt' , 'logs/error_log.txt']

log_levels  = [ logging.INFO , logging.WARNING , logging.ERROR , logging.CRITICAL , logging.DEBUG ]

log_formats = ['%(asctime)s - %(levelname)s - %(message)s' , '%(levelname)s - %(asctime)s - %(message)s']

logging.basicConfig(filename =  logpaths[0] , level = log_levels[0] , format = log_formats[0])    #отключить протоколирование - logging.disable()

colors = [ ( 0 , 0 , 255 ) , ( 0 , 0 , 0 ) , (250 , 0 , 0)  , (255 , 255 , 255) , (45 , 45 , 45 ) ]

anim_wait = 0
mags = 3

map_scale = 1 ; map_size = 3 ; show_map = 0
show_units = 1
show_buildings = 1
show_items = 1
show_interface = 1
open_backpack = 1

bg_num = 1 ; wallpapers = os.listdir('wallpapers/') ; wallpaper  = wallpapers[bg_num]

dark_level = 0
unit_moving = 1;unit_speed = 0;unit_speed1 = 0 ; max_unit_speed = 4

max_dark_level = 100
show_hero_stats = 1

volume_levels = 10
settings_values = 5

saving_type = 'default' ; game_state = 'main_menu' ; action = 'talk'

Colors_Coords_x_1 = [] ; Colors_Coords_y_1 = []

Colors_Coords_x_2 = [] ; Colors_Coords_y_2 = []

cell_size = 50

for i in range(volume_levels) : i += 1 ; i = Colors_Coords_x_1.append( i * 100) ; i = Colors_Coords_y_1.append(400)

for i in range(settings_values) : i += 1 ; i = Colors_Coords_x_2.append( i * 100) ; i = Colors_Coords_y_2.append(500)

islands_file_name = 'txt/Objects/Islands.txt' ; islands_file_mode = 'r' ; islands_file = open (islands_file_name , islands_file_mode) ; islands_file1 = islands_file.readlines() ; islands_list = [] ; islands_images = []

dialoges_list = [] ; dialoges_file_name = 'txt/dialoges.txt' ; dialoges_file_mode = 'r' ; dialoges_file = open (dialoges_file_name , dialoges_file_mode) ; dialoges_file1 = dialoges_file.readlines() ; dialoge_num = 0 ;dialoge_started    = 0

for i in range(len(dialoges_file1)) : i = small_font.render(dialoges_file1[i].strip() , False , small_font_color ) ; dialoges_list.append(i) 

checkpoints_list = [] ; checkpoints_file_name = 'txt/checkpoints.txt' ; checkpoints_file_mode = 'r' ; checkpoints_file = open (checkpoints_file_name , checkpoints_file_mode) ; checkpoints_file1 = checkpoints_file.readlines() ; checkpoint_size = 100 ; checkpoint_num = 0

achievements_list = [] ; achievements_file_name = 'txt/achievements.txt' ; achievements_file_mode = 'r' ; achievements_file = open (achievements_file_name , achievements_file_mode) ; achievements_file1 = achievements_file.readlines()

saves_list = [] ; saves_file_name = 'txt/saves/2023 - 8 - 10/0.txt' ; saves_file_mode = 'r' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file1 = saves_file.readlines()

for i in saves_file1 : screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]

for i in range(len(saves_file1)) : i = big_font.render(saves_file1[0].split(',')[0] , False , small_font_color ) ; saves_list.append(i)

crafts_list = [] ; crafts_file_name = 'txt/crafts.txt' ; crafts_file_mode = 'r' ; crafts_file = open (crafts_file_name , crafts_file_mode) ; crafts_file1 = crafts_file.readlines()
 
for i in range(len(crafts_file1)) : i = big_font.render(crafts_file1[i].strip() , False , small_font_color ) ; crafts_list.append(i)

quests_list = [] ; quests_states_list = [] ; quests_file_name = 'txt/langs/' + str(language) + '/Quests.txt' ; quests_file_mode = 'r' ; quests_file = open (quests_file_name , quests_file_mode) ; quests_file1 = quests_file.readlines()

for i in range(len(quests_file1)) : i = small_font.render(quests_file1[i].split(',')[0].strip() , False , small_font_color ) ; quests_list.append(i)

for i in range(len(quests_file1)) : i = small_font.render(quests_file1[i].split(',')[1].strip() , False , small_font_color ) ; quests_states_list.append(i)

main_menu = [] ; main_menu_file_name = 'txt/langs/' + str(language) + '/main_menu.txt' ; main_menu_file_mode = 'r' ; main_menu_file = open (main_menu_file_name , main_menu_file_mode) ; main_menu_file1 = main_menu_file.readlines()

for i in range(len(main_menu_file1)) : i = big_font.render(main_menu_file1[i].strip() , False , small_font_color ) ; main_menu.append(i)

settings = [] ; settings_file_name = 'txt/langs/' + str(language) + '/settings.txt' ; settings_file_mode = 'r' ; settings_file = open (settings_file_name , settings_file_mode) ; settings_file1 = settings_file.readlines()

for i in range(len(settings_file1)) : i = big_font.render(settings_file1[i].strip() , False , small_font_color ) ; settings.append(i)

hero_file_name = 'txt/hero.txt' ; hero_file_mode = 'r' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file1 = hero_file.readlines()

hero_inventory = [] ; hero_inventory_nums = [] ; hero_inventory_file_name = 'txt/hero_inventory.txt' ; hero_inventory_file_mode = 'r' ; hero_inventory_file = open (hero_inventory_file_name , hero_inventory_file_mode);hero_inventory_file1 = hero_inventory_file.readlines()

controls = [] ; controls_file_name = 'txt/controls.txt';controls_file_mode = 'r' ; controls_file = open (controls_file_name , controls_file_mode) ; controls_file1 = controls_file.readlines()

bg_num = 1 ; wallpapers_dir = os.listdir('wallpapers/') ; wallpaper = wallpapers_dir[bg_num]

map_grid = 1 ; dark_level = 0 ; show_interface = 1 ; open_backpack = 0 ; show_hero_stats = 1

meter = 100 ; cm = meter / 100 ; km = meter * 1000 ; inch = 2.54 #measure units/ linear measure 

map_width , map_height = meter * km , meter * km ; map_scale = 1 ; map_size = 3 ; show_map = 1 ; show_units = 1 ; show_buildings = 1 ; show_items = 1 ; show_islands = 0 #inch = 25,4 mm (2,54 см) foot = 0,3048 m (или 12 inches)

#surfs
mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
checkpoints_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
quests_surf = pg.Surface(( 200 , 200 ))
dark_surf = pg.Surface(( int(screen_width) , int(screen_height) ))
inteface_surf = pg.Surface(( 200 , 200 ))
dialoge_surf = pg.Surface((int(screen_width) / 3 , int(screen_height ) / 3))

dark_surf_color = ((0 , 0 , 0)) ; quest_surf_color = colors[1]

show_game_title   = big_font.render(      str( Game_title) , False ,big_font_color)
show_game_version = small_font.render(    'Version : ' + str( Game_version) , False ,small_font_color )
show_update       = small_font.render(    str( update_name ) , False , small_font_color)
show_game_state   = big_font.render(      str(game_state) , False , small_font_color )
show_author       = small_font.render(    'Author : ' + str(author) , False , small_font_color )
show_created_date = small_font.render(    'Created : 25 oktober 2019' , False , small_font_color )
show_money        = big_font.render(      'Money : ' + str(hero_money) , False , ( 250 , 0 , 0 ) )

hero_checkpoint_offset_x = 0 ; hero_checkpoint_offset_y = 0

class Background:
    def __init__(self , x , y , image) :
        self.x = x
        self.y = y
        self.image = image

for i in range( len ( islands_file1) )     : islands_images.append(pg.image.load('Objects/islands/0/0.png')) ; i = Background( islands_file1[i].split(',')[0] , islands_file1[i].split(',')[1] , islands_images[0] ) ; islands_list.append( i )

for i in range(len(nicknames_file1))   : i = small_font.render(players_file1[i].split(',')[2].strip() , False , small_font_color ) ; nicknameslist.append(i)

for i in range(len(hero_inventory_file1)) : i = big_font.render(hero_inventory_file1[i].strip() , False , small_font_color ) ; hero_inventory.append(i)     

new_quest = big_font.render('!' , False , small_font_color )

BGcolor = colors[0] ; minimapBGcolor = colors[0]

screen.fill(BGcolor)

minimap_location = 'right_up' ; minimap_x = 15 / 2 ; minimap_y = 15 / 2

if minimap_location == 'left_up': minimap_x = 0 ; minimap_y = 0
minimap_location = 'left_up' ; minimap_x = 15 / 2 ; minimap_y = 15 / 2

if minimap_location == 'left_down': minimap_x = 0 ; minimap_y = 0

class cam :
    def __init__( self , x , y ) : self.rect = pg.Rect( int(camera_x) , int(camera_y) , int(screen_width) , int(screen_height))

    def move( self , vector ) : self.rect[ 0 ] += vector[ 0 ] ; self.rect[ 1 ] += vector[ 1 ]

camera = cam( 0 , 0 ) ; vector = [ 0 , 0 ]

#hero_x and hero_y
x_1_list =  -camera.rect[ 0 ] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x ; y_1_list =  -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y  

x_2_list =  -camera.rect[ 0 ] + int(checkpoints_file1[checkpoint_num ].split(',')[0]) ; y_2_list =  -camera.rect[ 1 ] + int(checkpoints_file1[checkpoint_num ].split(',')[1]) #checkpoint_x andd checkpoint_y

distances = [] ; distance_num = 0
calc_dist = math.sqrt( (( x_2_list - x_1_list   * hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list * hero_checkpoint_offset_y) ** 2 ) // 100)
show_distance = small_font.render('Distance : ' + str(int(calc_dist) // 100) + ' m' , False , small_font_color )
blit_action = 0
blit_distance = 1