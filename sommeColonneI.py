#calcul de la somme d'une colonne i
import numpy as np

def somme(i,nomfichier):
    filepath = 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier+'.txt'  
    with open(filepath) as fp:
        fp.readline() #saute la premiere ligne de nomfichier.txt
        fp.readline() #saute la deuxieme ligne de nomfichier.txt
        fp.readline() #saute la troisieme ligne de nomfichier.txt
        line = fp.readline()
        s = 0
        while line:
            z=line.split(",")
            s+=int(z[i])
            print(int(z[i]))
            line = fp.readline()
            