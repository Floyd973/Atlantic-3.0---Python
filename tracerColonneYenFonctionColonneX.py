# ce programme permet de récolter une colonne i_x et i_y du fichier test2 sous forme de liste et de tracer y=f(x)
import re
from matplotlib import pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


def courbeXY(i_x,i_y,nomfichier):# numéro colonne abscisse, numéro colonne ordonnée (14 pour energie elect conso), nom du fichier à traiter
    filepath= 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier+'.txt'  #chemin répertoire à changer
    with open(filepath) as fp:
        fp.readline() #saute la premiere ligne de test2.txt
        fp.readline() #saute la deuxieme ligne de test2.txt
        line = fp.readline()
        entete=line.split(",") #enregistre l'entete pour prendre le nom
        nomColonneX=entete[i_x]
        nomColonneY=entete[i_y]
        x = [] # abscisse
        y = [] # ordonnee
        line=fp.readline()
        while line:
            z=line.split(",") # la fonction split permet de convertir la ligne de log en liste
            x.append(z[i_x])
            y.append(int(z[i_y])/1000) #1000impulsions/kWh
            line = fp.readline()
        
    plotly.offline.plot({
    "data": [Scatter(x=x, y=y, name='Energie')],
    "layout": go.Layout(title=nomColonneY+" en fonction de "+nomColonneX)
}) #tracé de la courbe
