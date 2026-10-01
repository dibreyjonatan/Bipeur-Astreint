from load_auth import donnes_connexions
from imap_tools import MailBox
from time import sleep 
from datetime import datetime
from communication_mqtt import MQTT 

broker = 'test.mosquitto.org'
port = 1883
topic_envoie ="/envoie"

sujet=""
corps=""
expediteur= None #"dibreyjonatan"
keyword="mission"
date=None
(email,mot_de_passe)=donnes_connexions()
mail_uid=None
#  forme du critère (objet, expéditeur, mot-clé), lieu et mode de configuration.
def detection() :
    global sujet, corps, expediteur, keyword,date,mail_uid
    date_premier_alerte=None # On memorise l'heure de la première détection
    nouvelle_date_alerte=None
    with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
        print("Connexion réussie !")
        while 1==1 :
            sleep(10)
            # il prend le dernier mail 
            for msg in mailbox.fetch(limit=1, reverse=True):
                mail_uid=msg.uid 
                sujet=msg.subject
                expediteur=msg.from_
                date=msg.date
                corps=msg.text
                print(expediteur, sujet)
                   #objet du mail ex : mission astreint N°XXXX-XXXX  
                if expediteur=="dibrey314@gmail.com" and "mission" in sujet.lower() and "astreint" in sujet.lower() :
                    nouvelle_date_alerte=date
                    

                if nouvelle_date_alerte!=date_premier_alerte :
                    date_premier_alerte=nouvelle_date_alerte
                    print("alerte provient du boss !!!")
                    print("le uid du mail est :",mail_uid)
                    print("date d'émission",date)
                    print("date de détection",datetime.now())
                else :
                    print("c'est le meme mail déjà lu")    

def run() :
    com=MQTT(broker,port)
    com.start()
    while 1==1 :
        com.send(topic_envoie,'1',broker,port)
        sleep(1)
    #detection()
if __name__=="__main__" :
    run()