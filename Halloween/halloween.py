import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Schools Magic Show BGM.mp3')
pygame.mixer.music.play()
sleep(10)
image = pygame.image.load('hallow.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(1)
pygame.mixer.music.load('screamandchoke.mp3')
pygame.mixer.music.play()
sleep(3)
