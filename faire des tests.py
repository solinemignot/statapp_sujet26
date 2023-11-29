import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/onyxia/work/projet-python/"
file_name1="caracteristiques_"+str(2009)+".csv"
f=open(path+file_name1,'r')
text=f.read()
text=text[0:10000]
i=0
while i <(len(text)-100):
    if text[i:i+7]=='2009000':
        j=i+2
        nombre=0
        indice=0
        print('hey')
        while text[j:j+7]!='2009000':
            j+=1
            if text[j]==',':
                nombre+=1
            if nombre==12:
                indice=j
        if nombre==16:
            text=text[:indice]+text[indice+1:]
    i+=1

print(text)






