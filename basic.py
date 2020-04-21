from imutils import paths
import argparse
import time 
import sys
import cv2
import os
import pickle
from os import listdir
def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))
def hash(image ) :
    hashsize = 8 
    #resize to 9*8 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    resized = cv2.resize(image, (hashsize +1 , hashsize) ) 


    #compute the gradient 
    diff = resized[: , 1:] > resized[: ,:-1] 


    return sum([2** i for(i, v ) in enumerate(diff.flatten()) if v] )
    


def pro( dire ):

    try: 
        path = dire
        files = os.listdir(path ) 


# r=root, d=directories, f = files

        return files 
            

    except :
        path =os.getcwd()+dire

        files = []
# r=root, d=directories, f = files

        files = os.listdir(path) 
        return files 


def process(dir):
    filename = pro(dir)
    s= [] 
    do = "/"
    for x in filename :
        img = cv2.imread(dir+do+ x)
        m =(hash(img))
        try : 
            d = s.index(m)
            os.remove(dir+do+x) 
        except :
            s.append(m)    
    n = 1  
    while 1 :
        if(os.path.exists("out"+str(n)+".bin")) :
            n=n+1
            continue 
        else :
            output = open("out"+str(n)+".bin" , "wb") 
            break 
        
        
        pickle.dump(s , output )
    return s 
                   
a = process("grain")
b = process("needle")

print(a)
print(b)