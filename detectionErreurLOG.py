## ce programme permet de détecter une erreur relevée par le LOG et d'envoyer par la suite un mail d'alerte
## il est à inclure dans une boucle qui traitera automatiquement les données du log à chaque réception de celui ci

def detectionErreur(nomfichier): #nomfichier: nom du fichier dans lequel on cherche l'erreur
    filepath = 'C:/Users/SAMUNG/Downloads/EMN/Mission Courte/'+nomfichier+'.txt'  
    with open(filepath) as fp:
        fp.readline() #saute la premiere ligne de nomfichier.txt
        fp.readline() #saute la deuxieme ligne de nomfichier.txt
        line=fp.readline() #saute la troisieme ligne de nomfichier.txt
        z=line.split(",")
        line = fp.readline()
        x = []
        cnt=0
        seuil2=1000
        while line :
            z=line.split(",")
            temps=z[0]
            erreur1= (z[75] != ' 3.0') #' 3.0' à remplacer par ' 255.255'
            erreur2= (int(z[12]) > seuil2)
            if (erreur1): # si la colonne d'erreur (colonne 75) affiche une erreur (ici si la valeur de la colonne 75 est différente de '1', c'est une erreur)
                envoiMailSiErreurLOG('chng.keke@gmail.com', '13777799769', 'chngclr@gmail.com',nomfichier,temps)
                break # sort de la boucle si erreur détectée pour ne pas spammer
            elif (erreur2):
                envoiMailSiAnomalie('chng.keke@gmail.com', '13777799769', 'chngclr@gmail.com',nomfichier,temps)
            line = fp.readline()
            cnt+=1
