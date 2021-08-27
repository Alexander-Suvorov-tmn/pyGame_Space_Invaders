import pygame
import random
import os
import sqlite3
from easygui import *
from variables import *

 
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'image')
player_img = pygame.image.load(os.path.join(img_folder, 'razorinv.png')).convert()
mob_img = pygame.image.load(os.path.join(img_folder, 'invaderinv.png')).convert()
bullet_img = pygame.image.load(os.path.join(img_folder, 'bullet.png')).convert()

font_name = pygame.font.match_font('comic sans ms', 14)