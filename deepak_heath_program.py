###Sorry sir but program ko check nhi kiya hu...

import datetime
import pygame

pygame.mixer.init()

water="water.mp3"
eyes="eyes.mp3"
physical="physical.mp3"
print("This program is only valid from 9.A.M to 5.P.M")
# here 20 minute for water
# 30 minute for eyes
# 45 minute for physical excersise

d = datetime.datetime.now()
print(f"Date and Time is {d}")

h=d.hour
m=d.minute
s=d.second
print(f"Now the actual hour is {h}")
m1=0
m2=0
m3=0
f=open("tiwari.txt","a")
while(d.hour>=9 and d.hour<=17):
    if(20+m1==30+m2):
        pygame.mixer.music.load(water)
        pygame.mixer.music.play()
        w=input("write drank to close the music..")
        if(w=="drank"):
            pygame.mixer.music.stop()
            print("drank")
            f.write(f"drinking completed at {d} \n")
            m1=m1+20
            pygame.mixer.music.load(eyes)
            pygame.mixer.music.play()
            e=input("write eydone to close the music.. ")
            if(e=="eydone"):
                pygame.mixer.music.stop()
                print("eyes exercise completed")
                f.write(f"eyes exercise completed at {d} \n")
                m2 = m2 + 30
            else:
                print("plz do eyes exercise")
        else:
            print("plz drink the water")
    elif(20+m1==45+m3):
        pygame.mixer.music.load(water)
        pygame.mixer.music.play()
        w = input("write drank to close the music....")
        if (w == "drank"):
            pygame.mixer.music.stop()
            print("drank")
            f.write(f"drinking completed at {d} \n")
            m1 = m1 + 20
            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()
            p=input("enter pydone to close the music..")
            if(p=="pydone"):
                pygame.mixer.music.stop()
                f.write(f"physical exercise completed at {d} \n")
                m3 = m3 + 45
            else:
                print("plz do physical exercise")
        else:
            print("plz drink the water")
    elif(30+m2==45+m3):
        pygame.mixer.music.load(eyes)
        pygame.mixer.music.play()
        e = input("write eydone to close the music.. ")
        if (e == "eydone"):
            pygame.mixer.music.stop()
            print("eyes exercise completed")
            f.write(f"eyes exercise completed at {d} \n")
            m2 = m2 + 30
            pygame.mixer.music.load(physical)
            pygame.mixer.music.play()
            p = input("enter pydone to close the music..")
            if (p == "pydone"):
                pygame.mixer.music.stop()
                f.write(f"physical exercise completed at {d} \n")
                m3 = m3 + 45
            else:
                print("plz do physical exercise")
        else:
            print("plz do eyes exercise")
    elif(d.minute-m==20+m1):
        m1=m1+20
        pygame.mixer.music.load(water)
        pygame.mixer.music.play()
        w = input("write drank to close the music....")
        if (w == "drank"):
            pygame.mixer.music.stop()
            print("drank")
            f.write(f"drinking completed  at {d} \n")
            m1 = m1 + 20
        else:
            print("plz drink the water")
    elif(d.minute-m==30+m2):
        m2=m2+30
        pygame.mixer.music.load(eyes)
        pygame.mixer.music.play()
        w = input("write eydone to close the music..")
        if (w == "eydone"):
            pygame.mixer.music.stop()
            print("eyes exercise completed")
            f.write(f"eyes exercise completed at {d} \n")
            m1 = m1 + 30
        else:
            print("plz do eyes exercise")
    elif(d.minute-m==45+m3):
        m3=m3+45
        pygame.mixer.music.load(physical)
        pygame.mixer.music.play()
        w = input("write pydone to close the music..")
        if (w == "pydone"):
            pygame.mixer.music.stop()
            print("physical exercise completed")
            f.write(f"physical exercise completed at {d} \n")
            m1 = m1 + 45
        else:
            print("plz do physical exercise")
    d = datetime.datetime.now()

f.close()






