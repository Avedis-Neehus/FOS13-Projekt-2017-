
from utility import *
import random
from copy import deepcopy


@maindeco
def main_menue():
    
    
    message_display('Hauptmenü', display_width*0.5, display_width*0.15, 58 )
    
    button( display_width*0.34375, display_height*0.35, display_width*0.3125,display_height/6,'Test', basic_test)
    button( display_width*0.34375, display_height*0.55, display_width*0.3125,display_height/6,'Training', second_menue)
    button( display_width*0.34375, display_height*0.75, display_width*0.3125,display_height/6,'Time Attack', second_menue)



@maindeco
def second_menue():
    
    message_display('Training',display_width*0.5, display_width*0.085, 60 )
    
    button( display_width*0.175, display_height*0.2, display_width*0.3125,display_height/6,'+', add_difficulty_menue , size = 60)
    button( display_width*0.5125, display_height*0.2, display_width*0.3125,display_height/6,'-', sub_difficulty_menue , size = 60)
    button( display_width*0.175, display_height*0.4, display_width*0.3125,display_height/6,'*',  mult_difficulty_menue , size = 60)
    button( display_width*0.5125, display_height*0.4, display_width*0.3125,display_height/6,'/', div_difficulty_menue, size = 60)
               
    button( display_width*0.175, display_height*0.6, display_width*0.3125,display_height/6,'Terme und Gleichungen', gleichungs_menue , size = 20)
    button( display_width*0.5125, display_height*0.6, display_width*0.3125,display_height/6,'Brüche', bruch_menue , size = 20)
    button(display_width*0.33, display_height*0.8, display_width*0.3125,display_height/6,'Mix', mix_difficulty_menue , size = 35)
    back_button(y=0.9)
    
@maindeco
def difficulty_menue(op):
    
    message_display(op, display_width*0.48, display_width*0.125, 100 )
    
    button( display_width*0.3275, display_height*0.3, display_width*0.3125,display_height/6,'Einfach', einfach[op].display_task , size = 50)
    button( display_width*0.3275, display_height*0.5, display_width*0.3125,display_height/6,'Mittel',  mittel[op].display_task, size = 50)
    button( display_width*0.3275, display_height*0.7, display_width*0.3125,display_height/6,'Schwer', schwer[op].display_task, size = 50) 
    
    back_button()

@maindeco    
def bruch_menue():
    
    button( display_width*0.175, display_height*0.2, display_width*0.3125,display_height/6,'+', bruch['+'].display_task , size = 60)
    button( display_width*0.5125, display_height*0.2, display_width*0.3125,display_height/6,'-', bruch['-'].display_task , size = 60)
    button( display_width*0.175, display_height*0.4, display_width*0.3125,display_height/6,'*',  bruch['*'].display_task , size = 60)
    back_button()
    
@maindeco    
def gleichungs_menue():
    
    button( display_width*0.175, display_height*0.2, display_width*0.3125,display_height/6,'leichte Gleichung', leichte_Gleichung.display_task , size = 20)
    button( display_width*0.5125, display_height*0.2, display_width*0.3125,display_height/6,'schwere Gleichung', schwere_Gleichung.display_task , size = 20)
    button( display_width*0.175, display_height*0.4, display_width*0.3125,display_height/6,'leichte Terme', leichter_Term.display_task , size = 20)
    button( display_width*0.5125, display_height*0.4, display_width*0.3125,display_height/6,'schwere Terme', schwerer_Term.display_task , size = 20)
    message_display("Terme und Gleichungen", 440, 50, 45 )
    
    
    back_button()
    
    
def add_difficulty_menue():
    difficulty_menue('+')        

def sub_difficulty_menue():   
    
    difficulty_menue('-')
    
def mult_difficulty_menue():
    
    difficulty_menue('*')
    
def div_difficulty_menue():
    
    difficulty_menue('/')
    
def mix_difficulty_menue():
    difficulty_menue('mix')    
    
def back_button(x= 0,y = 0, exit_func = loop_exit):
    button(display_width*x, display_height*y, display_width*0.2,display_height/10,'zurück',exit_func, size = 30)
    
class base_task(object):
    
    size = 50
    
    
    def __init__(self,operations, task_num = 10, mixed = False, reals = 0, start = 1, stop = 20):
        
        
        self.task_num = task_num
        self.mixed = mixed
        self.start = start
        self.stop = stop
        self.reals = reals       
        #a list containing operator dict keys
        self.operations = operations
        self.inputs = [label(display_width*0.7, display_height*0.625, size = 40)]
        self.record = result(task_num)
        
        self.del_record = 1
        self.back_button = 1
        self.current_task = 0
        
        
        
        
    def num_type(self):
        
        n = random.randint(self.start, self.stop)
        
        if self.reals:
            
            liste = [random.randint(self.start, self.stop), random.randint(0,9), random.randint(1,9)]
            ergebnis = 0
            
            for i in range(len(liste)):
                ergebnis+= liste[i] *10**-i
    
            return float(format(ergebnis, '.2f'))
        
        return n
        
    def mix_op(self):
        
        if self.mixed:
            random.shuffle(self.operations)
        else: 
            pass
        
    def generate_numbers(self):
        
        self.nums = []
        
        kardinal = len(self.operations) +1
        
        for i in range(kardinal):
            self.nums.append(self.num_type())
            
        return self.nums
    
    def operation_to_string(self):
                
        self.term = ''.join(str(a) + self.operations[i] for i,a in enumerate(self.nums[:-1])) + str(self.nums[-1])
        self.equation =  self.term + ' ='
        return self.equation  
        
         
    @maindeco
    def display_task(self):
        
        message_display(self.operation_to_string(),display_width/2.3 + len(self.operation_to_string()),display_height/2, fix_right = 0)
        #message_display(self.operations[0], display_width*0.48, display_width*0.125, 100)
        [user_num.display() for user_num in self.inputs]
        
        self.record.draw()
        
        button(display_width*0.65, display_height*0.8, display_width*0.3125,display_height/6
               ,'Eingabe', self.enter, size = 50)
        
        if self.back_button:
            back_button(exit_func = self.__exit__)
        
        
        
    def get_result(self):
        
            return [eval(self.term)]
                                             
    
    def verify(self):
       
       if all( abs(user.number-correct_num) < 0.05 for user, correct_num in zip(self.inputs, self.get_result()) ) :           
           return 1
       else:
           return 0
       
    def __exit__(self):
        
        if self.del_record:
            self.record.clear()
        self.current_task = 0 
        loop_exit()
        
    def enter(self):
        
        self.record.update(self.verify())
        
        if self.current_task < self.task_num:
            label.delete_all(self.inputs)
            self.mix_op()
            self.generate_numbers()
            self.current_task += 1           
                        
        else:
            self.__exit__()
            
    def init(self):
        
        self.generate_numbers()
        self.operation_to_string()
        
        


        
class brüche(base_task):
    
     
    
    def __init__(self,operations, task_num = 10, mixed = False, reals = 0, start = 0, stop = 20 ):
        
        super().__init__(operations, task_num , mixed, reals, start, stop )
        
        assert (len(self.operations)==1), 'brüche takes only one operator'
        
        self.operations.insert(0,'/')
        self.operations.append('/')
        self.inputs = [label(display_width*0.725, display_height*0.475, size = 40),
                       label(display_width*0.725, display_height*0.55, size = 40)]
        
        self.init()
        
    def generate_numbers(self):
        super().generate_numbers()
        
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
        
        
        [user_num.display() for user_num in self.inputs]
        message_display('-----------',620, 325, 25 )
        
        self.record.draw()
        
        button(display_width*0.55, display_height*0.9, display_width*0.3125,display_height/6
               ,'Eingabe', self.enter, size = 50)        

        if self.back_button:
            back_button(exit_func = self.__exit__)
        

class Aufgabe_Gleichungen(base_task):

    
    def __init__(self, einfache_Gleichung_bool, schwere_Gleichung_bool, task_num = 10, mixed = False, ):
        
        self.task_num = task_num
        self.mixed = mixed
        self.inputs = [label(display_width*0.7, display_height*0.5, size = 40)]
        self.record = result(task_num)
        self.current_task = 0
        self.einfache_Gleichung_bool = einfache_Gleichung_bool
        self.schwere_Gleichung_bool = schwere_Gleichung_bool
        self.back_button = 1
        self.del_record = 1
        
        
        self.init()
        
    def generate_numbers(self, start, stop, anzahl):

        
        self.nums = []
        
        for i in range(anzahl):
            number = random.randint(start, stop)
            if number == 0:
                number = 4
            self.nums.append(number)
        


    def einfache_Gleichung(self):
        
        self.a = self.nums[0]
        self.b = self.nums[1]

        # a + x = b  

        self.Aufgabe = str(self.a) + " + x = " + str(self.b)

        self.ergebnis = self.b - self.a

        # a + x = b|-a
        #     x = b - a


        # Einrücken alle Gleichzeichen untereinander:
        self.Loesungsweg = self.Aufgabe + "|" + str(-self.a) + "\n" + len(str(-self.a) + " + ") * " " + "x = " + str(self.ergebnis)

        if self.a < 0:
            self.Loesungsweg = self.Aufgabe + "|" + "+" + str(-self.a) + "\n" + len(str(self.a) + " + ") * " " + "x = " + str(self.ergebnis)





    def schwere_Gleichung(self):


        def Pluszeichen(ein_string):
            n = 0
            k = 0
            string = ein_string
            string_2 = ein_string 
            zahlenstring = "0123456789"
            for i in string:
                if i in zahlenstring and string[k-1] not in zahlenstring and k != 0 and string[k-1] != "+" and string[k-1] != "-" and string[k-1] != ".":
            
                    string_2 = string_2[0:k+n] + "+" + string_2[k+n:]

                    n += 1
            
                k += 1
            if string_2[0] in zahlenstring:
        
                string_2 = "+" + string_2

            return string_2

        self.a = self.nums[0]
        self.b = self.nums[1]
        self.c = self.nums[2]
        self.d = self.nums[3]

        self.f = self.a * self.b

        # Aufgabe (b-d)x + (-c) = (-d)x + (f-c)


        self.Aufgabe = str(self.b-self.d) + "x " + str(-self.c) + " = " + str(-self.d) + "x " + str(self.f-self.c)

        self.Aufgabe = Pluszeichen(self.Aufgabe)
        
        # Einrücken alle Gleichzeichen untereinander:
        Zeile1_loesung_laengeBisGleichzeichen = len(Pluszeichen(str(str(self.b-self.d) + "x " + str(-self.c))))

        Zeile2_loesung_laengeBisGleichzeichen = len(Pluszeichen(str(str(self.b) + "x " + str(-self.c)))) 

        differenz_Zeile1_und_2_loesung_laengeBisGleichzeichen = 0

        differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen = 0

        differenz_Zeile1_und_3_loesung_laengeBisGleichzeichen = Zeile1_loesung_laengeBisGleichzeichen - len(str(str(self.b) + "x"))

        differenz_Zeile1_und_4_loesung_laengeBisGleichzeichen = Zeile1_loesung_laengeBisGleichzeichen - 1

        if Zeile1_loesung_laengeBisGleichzeichen > Zeile2_loesung_laengeBisGleichzeichen:
            differenz_Zeile1_und_2_loesung_laengeBisGleichzeichen = Zeile1_loesung_laengeBisGleichzeichen - Zeile2_loesung_laengeBisGleichzeichen

        else:
            differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen = Zeile2_loesung_laengeBisGleichzeichen - Zeile1_loesung_laengeBisGleichzeichen
        
        self.zwischen_Loesungsweg = " " * differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen + self.Aufgabe + "|" + str(self.d) + "x" + "\n" + " " * differenz_Zeile1_und_2_loesung_laengeBisGleichzeichen +  str(self.b) + "x " + str(-self.c) + " = " + str(self.f-self.c) + "|" + str(self.c)

        self.zwischen_Loesungsweg = Pluszeichen(self.zwischen_Loesungsweg)

        if self.b < 0:
            self.Loesungsweg = self.zwischen_Loesungsweg + "\n" + " " * (differenz_Zeile1_und_3_loesung_laengeBisGleichzeichen+differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen) + str(self.b) + "x" + " = " + str(self.f) + "|: " + "(" + str(self.b) + ")" + "\n" + " " * (differenz_Zeile1_und_4_loesung_laengeBisGleichzeichen+differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen) + "x" + " = " + str(self.a)

        else:
            self.Loesungsweg = self.zwischen_Loesungsweg + "\n" + " " * (differenz_Zeile1_und_3_loesung_laengeBisGleichzeichen+differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen) + str(self.b) + "x" + " = " + str(self.f) + "|: " + str(self.b) + "\n" + " " * (differenz_Zeile1_und_4_loesung_laengeBisGleichzeichen+differenz_Zeile2_und_1_loesung_laengeBisGleichzeichen) + "x" + " = " + str(self.a)
        
        
        self.ergebnis = self.a


        # (b-d)x + (-c) = (-d)x + (f-c)|+d
        #   (b)x + (-c) = (f-c)|+c
        #          (b)x = f|: (b)|f = a*b
        #             x = a
        


    @maindeco
    def display_task(self):
        

        
        if self.einfache_Gleichung_bool:
            message_display("leichte Gleichungen", 440, 50, 50 )
            
        elif self.schwere_Gleichung_bool:
            message_display("schwere Gleichungen", 440, 50, 50 )
        
        message_display(self.Aufgabe, 200, 200, 40 )
        message_display("x =", display_width*0.6, display_height*0.53, 40 )

        
        self.record.draw()
        button(display_width*0.65, display_height*0.8, display_width*0.3125,display_height/6
           ,'Eingabe', self.display_show_task_solution, size = 50)
        
        [user_num.display() for user_num in self.inputs]
        
        if self.back_button:

            back_button(exit_func = self.__exit__)
    
    @maindeco
    def display_show_task_solution(self):
        
        if self.einfache_Gleichung_bool:
            message_display("leichte Gleichungen", 440, 50, 50 )
            
        elif self.schwere_Gleichung_bool:
            message_display("schwere Gleichungen", 440, 50, 50 )
        
        message_display("Loesung:", 180, 350, 30 )
        
        if self.verify():
            message_display("Richtig!", 180, 200, 30 )
            
        else:
            message_display("Leider Falsch!", 180, 200, 30 )
        
        # Zeilenumbrueche
        
        line = ""
        height = 400
        
        for element in self.Loesungsweg:
            
            if element == "\n":
                message_display(line, 180, height, 30 )
                line = ""
                height += 35
                continue
            
            line = str(line + element)
            
        message_display(line, 180, height, 30 )
        
        
        button(display_width*0.65, display_height*0.8, display_width*0.3125,display_height/6
           ,'Weiter', self.enter, size = 50)
        

        
    def verify(self):
        
        if all( abs(user.number-correct_num) < 0.05 for user, correct_num in zip(self.inputs, [self.ergebnis]) ) :
            
            return 1
        else:
        
            return 0
        
        
    def __exit__(self):
        
        if self.del_record:
            self.record.clear()
        self.current_task = 0 
        main_menue()
        
       
    def enter(self):
        
        
        
        self.record.update(self.verify())
        if self.current_task < self.task_num:
            label.delete_all(self.inputs)
            self.current_task += 1
            if self.einfache_Gleichung_bool:
                self.generate_numbers(-50,50,2)
                self.einfache_Gleichung()
                self.display_task()
            
            elif self.schwere_Gleichung_bool:
                self.generate_numbers(-20,20,4)
                self.schwere_Gleichung()
                self.display_task()
                


        else:
            self.record.clear()
            self.current_task = 0
            main_menue()



    def init(self):
        
        
        if self.einfache_Gleichung_bool:
            
            self.generate_numbers(-50,50,2)
            self.einfache_Gleichung()

        elif self.schwere_Gleichung_bool:
            
            self.generate_numbers(-20,20,4)
            self.schwere_Gleichung()
        



class Terme(Aufgabe_Gleichungen):
    
    def __init__(self, einfach_bool, schwer_bool, task_num = 10, mixed = False, ):
        
        self.einfach_bool = einfach_bool
        self.schwer_bool = schwer_bool
        self.task_num = task_num
        self.mixed = mixed
        self.inputs = [label(display_width*0.7, display_height*0.5, size = 40)]
        self.record = result(task_num)
        self.current_task = 0
        self.back_button = 1
        self.del_record = 1
        
        
        self.init()


    def einfache_Terme(self):
        
        self.d = self.nums[0]
        self.e = self.nums[1]
        
        self.Zufallszahl = random.randint(1,4)
        
        if str(self.Zufallszahl) in "123":
            
            if self.Zufallszahl == 1:
                o = "+ "
                v = "x "
                
            elif self.Zufallszahl == 2:
                o = "- "
                v = "x "
                
            else:
                o = "* "
                v = ""
            
            self.Aufgabe = str(self.d) + v + o + str(self.e) + "x"
            
            self.ergebnis = eval(str(str(self.d) + o + str(self.e)))
            
            
        else:
            
            self.Aufgabe = str(self.d*self.e) + "y" + "/" + str(self.e)
            
            self.ergebnis = self.d
            
            
            
    def schwere_Terme(self):
        
        self.d = self.nums[0]
        self.e = self.nums[1]
        self.q = self.nums[2]
        self.p = self.nums[3]

        while self.q-self.p == 0 or self.d*self.e/(self.q-self.p) != self.d*self.e//(self.q-self.p):
            self.generate_numbers(1,20,4)
            self.d = self.nums[0]
            self.e = self.nums[1]
            self.q = self.nums[2]
            self.p = self.nums[3]
            
        self.Aufgabe = str(self.d) + "x" + " * " + str(self.e) + "y" + " : " + "(" + str(self.q) + "-" + str(self.p) + ")"
            
        self.ergebnis = self.d*self.e//(self.q-self.p)



    
    @maindeco
    def display_task(self):
        
        if self.einfach_bool:
    
            message_display("leichte Terme", 440, 50, 50 )
            message_display("x", 675, 327, 40 )
            message_display("Gib hier deine Antwort ein:", 400, 327, 20 )
            message_display("Vereinfache den Term:", 200, 140, 25 )
            
        elif self.schwer_bool:
            
            message_display("schwere Terme", 440, 50, 50 )
            message_display("xy", 690, 327, 40 )
            message_display("Gib hier deine Antwort ein:", 400, 327, 20 )
            message_display("Vereinfache den Term:", 200, 140, 25 )
            
        [user_num.display() for user_num in self.inputs]
        
        self.record.draw()
        
        message_display(self.Aufgabe, 200, 200, 40 )
        
        button(display_width*0.65, display_height*0.8, display_width*0.3125,display_height/6
           ,'Eingabe', self.enter, size = 50)
        
        if self.back_button:

            back_button(exit_func = self.__exit__)
            
            
     
        
    def enter(self):
        
        
        
        self.record.update(self.verify())
        if self.current_task < self.task_num:
            label.delete_all(self.inputs)
            self.current_task += 1
            if self.einfach_bool:
                self.generate_numbers(1,20,2)
                self.einfache_Terme()
                self.display_task()
            
            elif self.schwer_bool:
                self.generate_numbers(1,20,4)
                self.schwere_Terme()
                self.display_task()
                


        else:
            self.record.clear()
            self.current_task = 0
            main_menue()

        

    def init(self):
        
        
        if self.einfach_bool:
            
            self.generate_numbers(1,20,2)
            self.einfache_Terme()

        elif self.schwer_bool:
            
            self.generate_numbers(1,20,4)
            self.schwere_Terme()




def test(tasks, task_num =15): 
    
    tasks = deepcopy([val for dic in tasks for val in dic.values()])
    
    record = result(task_num)
    
    
    for task in tasks:
        task.task_num = int(task_num/len(tasks))
        task.record = record
        task.del_record = False
        task.back_button = False
        task.display_task()
        #task.record.results[-3:].save()
    for task in tasks:
        task.record.clear()
            
class closed_div(base_task):
    
    
    def generate_numbers(self):
        
        assert (len(self.operations)==1), 'brüche takes only one operator' 
        self.nums = []
        
        a= random.randint(self.start, self.stop)
        b= random.randint(self.start, self.stop)
        c = a*b
        self.nums.append(c)
        self.nums.append(b)
        return self.nums




task = ['+', '-', '*']

einfach = dict((key, base_task([key])) for key in task)  
mittel  =  dict((key, base_task([key,key,key], start =-10, stop = 40 )) for key in task) 
schwer  =  dict((key, base_task([key,key,key,key], reals = 1, start =-10, stop = 40 )) for key in task)
bruch   = dict((key, brüche([key], start = 1)) for key in task)  

einfach.update({'/' : closed_div(['/'], stop = 11)})
einfach.update({'mix' : base_task(['+','*','-'], mixed = 1)})
mittel.update({'/' : base_task(['/'])})
mittel.update({'mix' : base_task(['+','*','-','/','+'], mixed = 1)})
schwer.update({'/' : base_task(['/', '/'])})
schwer.update({'mix' : base_task(['+','*','/','+','*'], mixed = 1)})

basic_tasks = [einfach, mittel]

def basic_test():
    test(basic_tasks)
           
def initz(dics):
    for dic in dics:
        for a in dic:
            dic[a].init()
            
            
initz([einfach, mittel, schwer])                   
leichte_Gleichung = Aufgabe_Gleichungen(True, False)
leichte_Gleichung.init()
        
schwere_Gleichung = Aufgabe_Gleichungen(False, True)
schwere_Gleichung.init()  

leichter_Term = Terme(True, False)
schwerer_Term = Terme(False,True)








