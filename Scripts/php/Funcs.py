import pygame as pg
from Settings import *
import pyautogui
from time import *
import logging

def make_screenshot() :
    screenshots = 1 ; screenshot = pyautogui.screenshot() 
    for i in range(screenshots) : screenshot.save( 'screenshots/' + str(d1.year) + ' - ' + str(d1.month) + ' - ' + str(d1.day) + ' - ' + str(d1.hour) + ' - ' +  str(d1.minute) + ' - ' + str(d1.second) + '.png' )

def save_game_and_quit():
            saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  ) ; saves_file.close()
            logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )

def load_game():
        saves_file_mode = 'r' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.close() ; logging.info(msg = 'GAME LOADED!' ) ; print('Game loaded!')

def save_game():
        saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  )
        saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; print('GAME SAVED!')