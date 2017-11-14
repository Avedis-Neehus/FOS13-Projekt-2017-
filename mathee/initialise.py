import pygame as pig
import operator as op


pig.init()


display_width = 800
display_height = 600

gameDisplay = pig.display.set_mode((display_width,display_height))
pig.display.set_caption('matheeee')
schrift = 'freesansbold.ttf'

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

clock = pig.time.Clock()


operation = {
        '+' : op.add,
        '-' : op.sub,
        '*' : op.mul,
        '/' : op.truediv,
        '%' : op.mod}
