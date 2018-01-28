## ce programme permet d'envoyer un mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def envoiMailSiAnomalie(depart, mdp, arrivee, nomfichier, temps): # adresse mail départ, mot de passe, adresse mail arrivée, info sur le field test et date de l'erreur, l'heure de l'erreur
    fromaddr = depart
    toaddr = arrivee
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Erreur LOG"
    
    body = "Une anomalie a été détectée au Field Test"+nomfichier+":\nL'heure de l'erreur est:"+temps+"\nVoici le lien d'accès au site web : http://phoenix44.pythonanywhere.com/index" # à compléter
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587) #paramètres du serveur de Gmail pour les courriels // d’abord le serveur en question (ou son adresse IP), puis le port utilisé// si vous utilisez un autre service, comme Yahoo par exemple, vous devez trouver les informations correspondantes
    server.starttls()
    server.login(fromaddr, mdp)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("le message d'anomalie a bien été envoyé à l'adresse "+arrivee)
    server.quit()