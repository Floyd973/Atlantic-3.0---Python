#calcul de la moyenne d'une colonne i
import numpy as np

def moyenne(i,nomfichier):
    filepath = 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier+'.txt'  
    with open(filepath,"r+") as fp:
        fp.readline() #saute la premiere ligne du fichier
        fp.readline() #saute la deuxieme ligne du fichier
        fp.readline() #saute la troisieme ligne de du fichier
        line = fp.readline()
        cnt = 1
        x = []
        while line:
            z=line.split(",")
            x.append(z[i])
            line = fp.readline()
            cnt += 1
    return np.mean(list(map(int,x)))
    