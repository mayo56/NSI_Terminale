from time import time
from random import randint

def id_gen():
    timestamp = str(round(time()))
    myId = ""
    for i in timestamp:
        myId += i
        myId += str(randint(0,9))
    
    print(myId)

id_gen()