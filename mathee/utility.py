from initialise import *



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text,pos_x,pos_y,size = 50, fix_right = 0, fix_left = 0, fixed_point = display_width/2 ):
    
    largeText = pig.font.Font(schrift,size)
    TextSurf, TextRect = text_objects(text, largeText)
    if fix_right == 1: 
            
            length = len(text)*size*0.8
            pos_x = fixed_point - length/2
    TextRect.center = ((pos_x),(pos_y))
    gameDisplay.blit(TextSurf, TextRect)  


    

class event_queue():

    events =  pig.event.get() 
    
    @classmethod       
    def events_update(cls):
        cls.events = pig.event.get()
        
class label(event_queue):
    
    keys = { pig.K_1 : 1, pig.K_2 : 2, pig.K_3 : 3 , pig.K_4 : 4 , pig.K_5 :5 , pig.K_6 : 6, pig.K_7 : 7
            , pig.K_8 : 8 ,pig.K_9 : 9, pig.K_0 : 0, pig.K_MINUS: '-', pig.K_COMMA: ','}
    
    
    
    def __init__(self, x,y, size = 50):
        
        self.x = x
        self.y = y
        self.size = size
        self.values = []
        
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
    @property               
    def number(self):
        
        num = 0
        values = [x for x in self.values]
        sign = 1
        
        
        if values.count('-')> 0:
            sign = -1
            #not using remove for the case of multiple - inputs
            values = [x for x in values if x!= '-']
            
        try:
            ind = values.index(',')
            length = len(values[:ind])
            values = [x for x in values if x!= ',']
            
        except: #no comma
            length = len(values)
            
        for i,lit in enumerate(values):
            num += lit*10**(length -i -1)
        return num*sign     
                            
    def display(self):
        num = ''.join(str(i) for i in self.values)        
        button(self.x, self.y, 100,40, num, no_click_func = self.fill_values, size = self.size)
                     
    def delete(self):
        self.values[:] = []
        
    @staticmethod 
    def delete_all(inst):
        
        [label.delete() for label in inst]

class result(object):
    
    def __init__(self, max_len = 0, results = [], dim = [20, 500,40,20]):
        
        self.results = results
        self.max_len = max_len
        self.dim = dim
        self.gap = 30
        
    def gap_comp(num,L,l,start):
        
        pos = L
        
    def  draw(self, versch = 0):
        
        dim = [a for a in self.dim]
        gap = 50
        switch = 1       
        dim[0]-= gap 
        
        for i,res in enumerate(self.results):            
            
            
            if i*(gap+dim[2]) > (display_width):  
                
                if switch:
                    a = i
                    switch = 0
                    
                dim[1] = self.dim[1] + self.dim[3]+10
                dim[0] = self.dim[0] + gap*(i-a)
                   
            else:    
                dim[0] += gap
               

                
                
            if res:
                pig.draw.rect(gameDisplay, green,dim)
                
            else:
                pig.draw.rect(gameDisplay, red ,dim)
                
    def  update(self, res):
       
        self.results.append(res)      
        
    def clear(self):
        self.results[:] = []
        
def button(x,y,w,h, text = '', func = lambda : None, no_click_func = lambda : None , size = 30):
    #wenn innerhalb button
    mouse = pig.mouse.get_pos()
    
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        
        pig.draw.rect(gameDisplay, light_gray,(x,y,w,h))
        message_display(text,x+(w/2),y+(h/2),size)
        no_click_func()
        
        #wenn gedrückt        
        for event in event_queue.events:
            if event.type == pig.MOUSEBUTTONDOWN:
                
                func()
   
    else:
        #zeig den button
        pig.draw.rect(gameDisplay, gray,(x,y,w,h))
        message_display(text,x+(w/2),y+(h/2),size)        


    
class taskDone(Exception): pass   
                   
def loop_exit():    
    raise taskDone
    
def maindeco(func):
 
    
    def structure(*args):
        try:
            
            while True:
                
                event_queue.events_update()
                for event in event_queue.events:        
        
                    if event.type == pig.QUIT:
                        
                        pig.quit()
                        quit()
                
                gameDisplay.fill(white)
                func(*args)
    
                pig.display.update()      
                
                clock.tick(30)
        except taskDone:
            pass
    return structure

