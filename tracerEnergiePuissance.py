# ce programme permet de récolter une colonne i_x et i_y du fichier test2 sous forme de liste et de tracer y=f(x)
import re
from matplotlib import pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


def courbeEnergiePuissance(i_x,i_e,nomfichier):# numéro colonne abscisse, numéro colonne ordonnée (14 pour energie elect conso), nom du fichier à traiter
    filepath= 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier+'.txt'  #chemin répertoire à changer
    with open(filepath) as fp:
        fp.readline() #saute la premiere ligne de nomfichier
        fp.readline() #saute la deuxieme ligne de nomfichier
        line = fp.readline()
        entete=line.split(",") #enregistre l'entete pour prendre le nom
        nomColonneX=entete[i_x]
        nomColonneE=entete[i_e]
        x = [] # abscisse
        e = [] # energie
        line=fp.readline()
        cnt=0
        while line:
            z=line.split(",") # la fonction split permet de convertir la ligne de log en liste
            x.append(z[i_x])
            if cnt==0:
                e.append(int(z[i_e])/1000) #1000impulsions/kWh
            else:
                e.append(int(z[i_e])/1000+e[cnt-1]) #cumul de l'énergie enregistrée par le compteur
            line = fp.readline()
            cnt+=1
        p = [] # liste des valeurs de puissance
        for i in range(1,np.size(e)):
            p.append((float(e[i])-float(e[i-1]))/(float(x[i])-float(x[i-1]))) #formule de la pente

    plotly.offline.plot({
    "data": [go.Scatter(x=x, y=e, name='Energie en J'), go.Scatter(x=x, y=p, name='Puissance en W')],
    "layout": go.Layout(title=nomColonneE+" en fonction de "+nomColonneX)
})

