from load_auth import donnes_connexions
from imap_tools import MailBox
from time import sleep 
(email,mot_de_passe)=donnes_connexions()

#  forme du critère (objet, expéditeur, mot-clé), lieu et mode de configuration.
def detection() :
    with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
        print("Connexion réussie !")
        while 1==1 :
            sleep(10)
            for msg in mailbox.fetch(limit=1, reverse=True):
                print(msg.subject)
                print(msg.from_)
                print(msg.date)
                print(msg.text)
                print()

def run() :
    detection()
if __name__=="__main__" :
    run()