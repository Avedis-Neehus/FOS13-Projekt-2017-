from utility import *

@maindeco
def main_menue():
    
    number = label(display_width*0.7, display_height*0.5, size = 20)
    
    number.fill_values()
    number.display()
    
    message_display('Hauptmenue', display_width*0.5, display_width*0.15)
    
    button( display_width*0.34375, display_height*0.4, display_width*0.3125,display_height/6,'Training', second_menue)
    button( display_width*0.34375, display_height*0.6, display_width*0.3125,display_height/6,'Training', second_menue)



@maindeco
def second_menue():
                   
    button( display_width*0.1, display_height*0.3, display_width*0.3125,display_height/6,'+', main_menue, size = 60)
    button( display_width*0.55, display_height*0.3, display_width*0.3125,display_height/6,'-',  main_menue, size = 100)
    button( display_width*0.1, display_height*0.5, display_width*0.3125,display_height/6,'*', main_menue, size = 60)
    button( display_width*0.55, display_height*0.5, display_width*0.3125,display_height/6,'/', main_menue, size = 60)

from utility import *


@maindeco
def main_menue():
    
    number = label(display_width*0.7, display_height*0.5, size = 20)
    
    number.fill_values()
    number.display()
    
    message_display('Hauptmenue', display_width*0.5, display_width*0.15, 58 )
    
    button( display_width*0.34375, display_height*0.4, display_width*0.3125,display_height/6,'Training', second_menue)
    button( display_width*0.34375, display_height*0.6, display_width*0.3125,display_height/6,'Training', second_menue)



@maindeco
def second_menue():
                   
    button( display_width*0.1, display_height*0.3, display_width*0.3125,display_height/6,'+', main_menue, size = 60)
    button( display_width*0.55, display_height*0.3, display_width*0.3125,display_height/6,'-',  main_menue, size = 100)
    button( display_width*0.1, display_height*0.5, display_width*0.3125,display_height/6,'*', main_menue, size = 60)
    button( display_width*0.55, display_height*0.5, display_width*0.3125,display_height/6,'/', bruch_menue, size = 60)

@maindeco
def bruch_menue():
    
    number = label(display_width*0.7, display_height*0.5, size = 20)
    
    number.fill_values()
    number.display()
    
    message_display('Brueche', display_width*0.5, display_width*0.15, 58 )
    
    button( display_width*0.34375, display_height*0.4, display_width*0.3125,display_height/6,'Start', bruchgame_menue)
    button( display_width*0.34375, display_height*0.6, display_width*0.3125,display_height/6,'Zurueck', second_menue)

    
@maindeco
def bruchgame_menue():
    
    number = label(display_width*0.7, display_height*0.5, size = 20)
    
    number.fill_values()
    number.display()
    
    message_display('Training - Brueche', display_width*0.5, display_width*0.15, 58 )
    
    spiel_bruch() 
