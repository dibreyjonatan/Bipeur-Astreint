from load_auth import donnes_connexions
from imap_tools import MailBox
from time import sleep 
from datetime import datetime
import csv
from communication_mqtt import MQTT 
from configs.configuration import config 
from gestion_alerte import gerer_alerte
gere_alerte=None
com=None 
configs=None 
(email,mot_de_passe)=donnes_connexions()
mail_uid=None
#  forme du critère (objet, expéditeur, mot-clé), lieu et mode de configuration.
def detection() :
    global configs,com, gere_alerte
    deja_detecter=0
    with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
        print("Connexion à la boite mail réussie !")
        while 1==1 :
            sleep(10)
            # il prend le dernier mail, le mail le plus haut dans l'application 
            for msg in mailbox.fetch(limit=1, reverse=True):
                mail_uid=msg.uid 
                sujet=msg.subject
                expediteur=msg.from_
                date_alerte=msg.date
                corps=msg.text
                print(expediteur, sujet) 
                #print(configs.expediteur, configs.ordre,configs.employer) 
                #objet du mail ex : mission astreint N°XXXX-XXXX  
                test_mail=0
                if expediteur == configs.expediteur and configs.ordre in sujet.lower() and configs.employer in sujet.lower() :
                     # test de présence d'un mail déjà détecter 
                     # si 0, donc pas encore detecter, si 1 dejè détecter 
                    #print(mail_uid) 
                    test_mail=1
                    deja_detecter=gere_alerte.test_alerte_enregistre(mail_uid)
                    #print(deja_detecter)
                    #print(gere_alerte.presence)
                    if gere_alerte.presence == 1 :
                         print("c'est une alerte mais déjà détecter !")
            
                    #donc l'alerte est unique et non redondante
                if gere_alerte.presence  == 0 and test_mail==1:
                    print("alerte provient du boss !!!")
                    print("le uid du mail est :",mail_uid)
                    print("date d'émission",date_alerte)
                    print("date de détection",datetime.now())
                    ## Ecriture dans le fichier csv d'alerte 
                    # uid, expediteur,date_alerte,date_detection
                    with open('docs/alerte_log.csv', mode='a', newline='') as fichier:
                            write= csv.writer(fichier)
                            write.writerow([mail_uid,expediteur,date_alerte,datetime.now()])
                    ## Envoie alerte, qui sera uid 
                    com.send(configs.topic_envoie,mail_uid,configs.broker,configs.port)
                    print("envoie réussit")
                    ## Je fais le fichier d'acquittement avec un status false 
                    ## le fichier csv d'acquittement est le suivant
                    ## uid, date d'émission, date d'acquittement, status
                    with open('docs/acquittement_log.csv', mode='a', newline='') as fichier:
                            write= csv.writer(fichier)
                            write.writerow([mail_uid,expediteur,datetime.now(),"date_acquittement", False])
                # TODO     
                
                #Check si l'uid reçu figure dans le tableau et je verifie l'acquittement     
                ## à la reception on est censé avoir l'uid et l'acquittement     
                else :
                    pass 
                    #print("c'est le meme mail déjà lu")    

def run() :
    global com, configs, gere_alerte
    configs=config()
    configs.load_configs()
    gere_alerte= gerer_alerte()
    #print(configs.broker,configs.port,configs.topic_reception)
    com=MQTT(configs.broker,configs.port,configs.topic_reception)
    com.start() 
    detection()
if __name__=="__main__" :
    run()