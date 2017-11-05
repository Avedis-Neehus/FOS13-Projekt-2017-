import pygame as pig

pig.init()


display_width = 800
display_height = 600

gameDisplay = pig.display.set_mode((display_width,display_height))
pig.display.set_caption('matheeee')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


clock = pig.time.Clock()
