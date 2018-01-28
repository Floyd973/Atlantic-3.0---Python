# ce programme permet de tracer le COP 
##on suppose que les données LOG et CICE sont synchronisées, si faudra par la suite écrire des conditions pour traiter les données qui sont acquises en même temps

import re
from matplotlib import pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

## à modifier

def courbeCOP(i_consoElec,i_Te,i_Ts,nomfichier_log,nomfichier_cice):# indice colonne conso électrique (13), indice colonne T°_entrante (on suppose que ce soit T°1 (6)), indice colonne T°_sortante (on suppose que ce soit T°8 (13), nom du fichier LOG, nom du fichier CICE
    c_eau=1
    rho_eau=1
    V_eau=200 #volume eau (pas cst)
    cst=c_eau*rho_eau*V_eau ##constante dans l'expression de la puissance thermique
    COP = []
    filepath_log = 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier_log+'.txt'  #chemin répertoire à changer
    with open(filepath_log) as fp_log:
        fp_log.readline() #saute la premiere ligne de nomfichier_log.txt
        fp_log.readline() #saute la deuxieme ligne de nomfichier_log.txt
        entete=fp_log.readline().split(",") #enregistre l'entete pour prendre le nom
        nomColonneX=entete[0]
        line = fp_log.readline()
        x = []
        conso_Elec = [] # liste puissance elec
        while line:
            z=line.split(",")
            x.append(z[0])
            conso_Elec.append(z[i_consoElec])
            line = fp_log.readline()
        
    filepath_cice = 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier_cice+'.txt'  #chemin répertoire à changer
    with open(filepath_cice) as fp_cice:
        for i in range(1,15):
            fp_cice.readline() #saute les premieres lignes de nomfichier_cice.txt
        line=fp_cice.readline()
        t_e = [] #température entrante
        t_s = [] #température sortante 
        while line:
            z=line.split(";")
            t_e.append(z[i_Te])
            t_s.append(z[i_Ts])
            line = fp_cice.readline()
        cnt=0
        for i in range(0,np.size(t_e)-1):
            for j in range (0,5):
                value=float(conso_Elec[cnt])/(cst*(float(t_s[i])-float(t_e[i])))
                cnt+=1
                COP.append(value)
    plotly.offline.plot({
    "data": [Scatter(x=x, y=COP)],
    "layout": go.Layout(title="COP en fonction de "+nomColonneX)
})