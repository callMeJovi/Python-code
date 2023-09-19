import pygame
import time
# initiate - load music mixer
pygame.mixer.init()
# load music
pygame.mixer.music.load('C:/Users/jeggy/OneDrive/Documents/Python_code/mysql_code/music_demo/music/van-ness-wu-summertime-love-official-music-video.mp3')
pygame.mixer.music.play()

time.sleep(120)