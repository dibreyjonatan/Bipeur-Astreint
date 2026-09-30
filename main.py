from load_auth import donnes_connexions
from imap_tools import MailBox
from time import sleep 
from datetime import datetime
sujet=""
corps=""
expediteur= None #"dibreyjonatan"
keyword="mission"
date=None
(email,mot_de_passe)=donnes_connexions()

#  forme du critère (objet, expéditeur, mot-clé), lieu et mode de configuration.
def detection() :
    global sujet, corps, expediteur, keyword,date
    date_premier_alerte=None # On memorise l'heure de la première détection
    nouvelle_date_alerte=None
    with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
        print("Connexion réussie !")
        while 1==1 :
            sleep(10)
            # il prend le dernier mail 
            for msg in mailbox.fetch(limit=1, reverse=True):
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
                    print("date d'émission",date)
                    print("date de détection",datetime.now())
                else :
                    print("c'est le meme mail déjà lu")    

def run() :
    detection()
if __name__=="__main__" :
    run()