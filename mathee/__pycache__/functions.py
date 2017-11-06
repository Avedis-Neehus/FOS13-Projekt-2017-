from utility import *
import random
import numpy as np


@maindeco
def main_menue():
    
    
    message_display('Hauptmenü', display_width*0.5, display_width*0.15, 58 )
    
    button( display_width*0.34375, display_height*0.4, display_width*0.3125,display_height/6,'Training', second_menue)
    button( display_width*0.34375, display_height*0.6, display_width*0.3125,display_height/6,'Training', second_menue)



@maindeco
def second_menue():
                   
    button( display_width*0.1, display_height*0.3, display_width*0.3125,display_height/6,'+', add.display_task, size = 60)
    button( display_width*0.55, display_height*0.3, display_width*0.3125,display_height/6,'-',  main_menue, size = 100)
    button( display_width*0.1, display_height*0.5, display_width*0.3125,display_height/6,'*', main_menue, size = 60)
    button( display_width*0.55, display_height*0.5, display_width*0.3125,display_height/6,'/', main_menue , size = 60)

class base_task(object):
    
    size = 50
    Input = label(display_width*0.7, display_height*0.5, size = 40)
    
    def __init__(self,operations, task_num = 10, mixed = False ):
        
        
        self.task_num = task_num
        self.mixed = mixed
        #a list containing operator dict keys
        self.operations = operations
        self.input = label(display_width*0.7, display_height*0.5, size = 40)
        self.record = []
        self.current_task = 0
        
        
    
    def generate_numbers(self, start = 0, stop = 20):
        
        self.nums = []
        
        kardinal = len(self.operations) +1
        
        for i in range(kardinal):
            self.nums.append(random.randint(start,stop))
            
        return self.nums
    
    def operation_to_string(self):
                
        self.term = ''.join(str(a) + self.operations[i] for i,a in enumerate(self.nums[:-1])) + str(self.nums[-1])
        self.equation =  self.term + ' ='
        return self.equation  
        
         
    @maindeco
    def display_task(self):
        
        message_display(self.operation_to_string(),display_width/2,display_height/2, fix_right = 1)
        self.input.fill_values()
        self.input.display()
        button(display_width*0.55, display_height*0.9, display_width*0.3125,display_height/6
               ,'Eingabe', self.enter, size = 50)
   
    def get_result(self):
        
            return eval(self.term)
                    
                         
    
    def verify(self):
       
       if self.Input.number == self.get_result():

           return 1
       else:
           return 0
       
    def enter(self):
        
        self.record.append(self.verify())
        
        if self.current_task < self.task_num:
            self.Input.delete()
            self.generate_numbers()
            self.current_task += 1           
            self.operation_to_string
        else:
            main_menue()
            
    def init(self):
        
        self.generate_numbers()
        self.operation_to_string()
        
        
add = base_task(['+'])
add.init()        
        
class brüche(base_task):
    
    input2 = label(display_width*0.7, display_height*0.7, size = 40)  
    
    def __init__(self,operations, task_num = 10, mixed = False):
        
        super().__init__(operations, task_num , mixed )
        
        assert (len(self.operations)==1), 'brüche takes only one operator'
        
        self.operations.insert(0,'/')
        self.operations.append('/')
        
        self.init()
        
    def generate_numbers(self, start = 0, stop = 20):
        super().generate_numbers(start, stop )
        
        self.Nenner1= self.nums[1]
        self.Zahler1= self.nums[0]
        self.Nenner2= self.nums[3]        
        self.Zahler2= self.nums[2]
        
        self.NeuerZahler1 = self.Zahler1 * self.Nenner2
        self.NeuerZahler2 = self.Zahler2 * self.Nenner1
        self.NeuerNenner1 = self.Nenner1 * self.Nenner2
        
    def get_result(self):    
        
        if self.operations[1] == '+':
             
             z3=self.NeuerZahler1+self.NeuerZahler2
             n3=self.NeuerNenner1
         
        elif self.operations[1] == "-":
              
              z3=self.NeuerZahler1-self.NeuerZahler2
              n3=self.NeuerNenner1 
          
        elif self.operations[1] == "*":
              
              z3=self.Zahler1*self.Zahler2
              n3=self.Nenner1*self.Nenner2
          
        if z3 == 0:
                z3 = 0
                n3 = 1
      
        else:
            for x in range(400,1,-1):
                if (z3 % x == 0) and (n3 % x == 0):
                    z3 = z3/x
                    n3 = n3/x
                    break
                
        return z3,n3
    
    def verify(self):
        
        if self.Input.number == self.get_result()[0] and self.input2.number == self.get_result()[1]:
           return 1
        else:
           return 0
        
        
    @maindeco
    def display_task(self):
        
        message_display(str(self.Zahler1), 180, 300, 40 )
        message_display('-----------', 180, 325, 25 )
        message_display(str(self.Nenner1), 180, 350, 40 )
        
        message_display(self.operations[1], 305, 325 , 40 )
        
        message_display(str(self.Zahler2),430 , 300, 40 )
        message_display('-----------',430, 325, 25 )
        message_display(str(self.Nenner2), 430, 350, 40 )        
        message_display('=', 550, 325, 40 )
        
        
        self.input.display() 
        message_display('-----------',620, 325, 25 )
        self.input2.display()
        
        button(display_width*0.55, display_height*0.9, display_width*0.3125,display_height/6
               ,'Eingabe', self.enter, size = 50)        
        
        
        
        
bruch = brüche(['+'])  
    
add = base_task(['+'])        
        
        
        
        
        
        
        
        
        
