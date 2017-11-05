from initialise import *
from random import *

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text,pos_x,pos_y,size):
    largeText = pig.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((pos_x),(pos_y))
    gameDisplay.blit(TextSurf, TextRect)  



class event_queue():

    events =  pig.event.get() 
    
    @classmethod       
    def events_update(cls):
        cls.events = pig.event.get()
        
class label(event_queue):
    
    keys = { pig.K_1 : 1, pig.K_2 : 2, pig.K_3 : 3 , pig.K_4 : 4 , pig.K_5 :5 , pig.K_6 : 6, pig.K_7 : 7
            , pig.K_8 : 8 ,pig.K_9 : 9, pig.K_0 : 0}
    
    values = []
    
    def __init__(self, x,y, size = 50):
        
        self.x = x
        self.y = y
        self.size = size
      
        
    def fill_values(self):
        
        for event in event_queue.events:
            
            if event.type == pig.KEYDOWN:
                
                for taste in self.keys:
                    
                    if event.key == taste:
                        
                        self.values.append(self.keys[taste])
                        
                if event.key == pig.K_BACKSPACE:
                    try:
                        del self.values[-1]
                    except:
                        #index out of bounds
                        pass
                    
    def display(self):
        num = ''.join(str(i) for i in self.values)
        message_display(num, self.x,self.y, self.size)
        
    def delete(self):
        self.values[:] = []
       
  
def button(x,y,w,h, text, func = lambda : None, size = 30):
    #wenn innerhalb button
    mouse = pig.mouse.get_pos()
    
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pig.draw.rect(gameDisplay, black,(x,y,w,h))
        
        #wenn gedruckt
        
        for event in event_queue.events:
            if event.type == pig.MOUSEBUTTONDOWN:
                
                func()
   
    else:
        #zeig den button
        pig.draw.rect(gameDisplay, red,(x,y,w,h))
        message_display(text,x+(w/2),y+(h/2),size)        


    
                      

def maindeco(func):
 
    
    def structure():
        while 1:
            
            event_queue.events_update()
            for event in event_queue.events:        
    
                if event.type == pig.QUIT:
                    
                    pig.quit()
                    quit()
            
            gameDisplay.fill(white)
            func()

            pig.display.update()      
            
            clock.tick(30)
    return structure


def spiel_bruch():
    
    r = randint(1, 3)

    Nenner1=randint(1, 20)
    Zahler1=randint(1, 20)
    Nenner2=randint(1, 20)

    Zahler2=randint(1, 20)
    NeuerZahler1 = Zahler1 * Nenner2
    NeuerZahler2 = Zahler2 * Nenner1
    NeuerNenner1 = Nenner1 * Nenner2

    if r == 1:
      op = "+"
      z3=NeuerZahler1+NeuerZahler2
      n3=NeuerNenner1
     
    elif r == 2:
      op = "-"
      z3=NeuerZahler1-NeuerZahler2
      n3=NeuerNenner1 
      
    elif r == 3:
      op = "*"
      z3=Zahler1*Zahler2
      n3=Nenner1*Nenner2
      
    if z3 == 0:
        z3 = 0
        n3 = 1
  
    else:
      for x in range(400,1,-1):
        if (z3 % x == 0) and (n3 % x == 0):
          z3 = z3/x
          n3 = n3/x
          break

    message_display(str(Zahler1), 180, 300, 40 )
    message_display('-----------', 180, 325, 25 )
    message_display(str(Nenner1), 180, 350, 40 )
    
    message_display(str(op), 305, 325 , 40 )
    
    message_display(str(Zahler2),430 , 300, 40 )
    message_display('-----------',430, 325, 25 )
    message_display(str(Nenner2), 430, 350, 40 )
    
    message_display('=', 550, 325, 40 )
    
    message_display(str(z3), 620, 300, 40 )
    message_display('-----------',620, 325, 25 )
    message_display(str(n3), 620, 350, 40 )
    








