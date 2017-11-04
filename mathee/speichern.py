#Sandro, Jonathan

import os

def erstellen(vorname,nachname):            #Beispiel: erstellen("franz","geißler")
#EINSTELLUNG
   #Path zum Speicherort Eingeben (String):
   speicherort = "C:/Users/sandro.fleischer/Desktop/ordner/"
#EINSTELLUNG


   if os.path.isfile(speicherort+str(vorname)+str(nachname)+".txt") == True:
       return "Für diesen Namen existiert schon ein Konto"
   else:
       f = open(str(vorname)+str(nachname)+".txt","w")
       f.write("0\n0\n0\n0")
       f.close
       
erstellen("franz","geißler")                # VOR DEM EINFUEGEN ENTFERNEN!!!

def verändern(wer,was,änderung):            #Beispiel: verändern("franzgeißler",1,2)
   lesen = open(str(wer)+".txt")
   a = lesen.readline()
   a = int(a)
   
   b = lesen.readline(2) 
   b = int(b)

   c = lesen.readline(3)
   print("%s"%(c))
   c = int(c)
   print(c)

   d = lesen.readline(4)
   print("%s"%(d))
   d = int(d)
   print(d)

   #Falls mehr Werte gespeichert werden sollen muessen einfach weitere Zeilen ausgelesen werden. Mann muss aber beachten das bei der erstellung der Datei eine weitere "0" an die Datei angehaengt werden muss!

           
   if int(was) == 1:                       # die 1 bzw. 2,3,4 kann mann zur uebersicht auch in die genaue art von information umbenennen (Bsp.Pkt1,Pkt2,Zeit_1...etc)
           a = a + int(änderung)
           
   if int(was) == 2:
           b = b + int(änderung)
           
   if int(was) == 3:
           c = c + int(änderung)

   if int(was) == 4:
           d = d + int(änderung)
   lesen.close
   ueberschreiben = open(str(wer)+".txt", "r+")
   ueberschreiben.truncate()
   ueberschreiben.close
   speichern = open(str(wer)+".txt", "w")
   speichern.write(str(a)+"\n"+str(b)+"\n"+str(c)+"\n"+str(d))
   

verändern("franzgeißler",1,2)               # VOR DEM EINFUEGEN ENTFERNEN!!!


def ausgeben(wer,was):                      # wer = Name der Datei/ des Schuelers; was = welcher der (bis jetzt 4 moeglichen Werte)
   lesen = open(str(wer)+".txt")
   a = lesen.readline()
   a = int(a)
   
   b = lesen.readline(2) 
   b = int(b)

   c = lesen.readline(3)
   c = int(c)

   d = lesen.readline(4)
   d = int(d) 


   if int(was) == 1:                       # die 1 bzw. 2,3,4 kann mann zur uebersicht auch in die genaue art von information umbenennen (Bsp.Pkt1,Pkt2,Zeit_1...etc)
           return(a)
           
   if int(was) == 2:
           return(b)
           
   if int(was) == 3:
           return(c)

   if int(was) == 4:
           return(d)


print(ausgeben("franzgeißler",1))           # VOR DEM EINFUEGEN ENTFERNEN!!!
