from load_auth import donnes_connexions
from imap_tools import MailBox
from time import sleep 
from communication_mqtt import MQTT 
from configs.configuration import config 
from gestion_alerte import gerer_alerte
from surveillance import surveillance 
from communication import communication
com_t=None 
surveille=None 
gere_alerte=None
com=None 
configs=None 
(email,mot_de_passe)=donnes_connexions()
mail_uid=None
#  forme du critère (objet, expéditeur, mot-clé), lieu et mode de configuration.
def main() :
    global configs,com, gere_alerte
    with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
        print("Connexion à la boite mail réussie !")
       
        # Recouvrement en cas de perte de connexion ou lors d'une reconnexion 
        # pour satisfait le besoin BES-012 ( aucun mail manqué )
        data=[]
        for msg in mailbox.fetch(limit=configs.limit_recouvrement, reverse=True):
            data.append(msg)
        gere_alerte.recouvrement(data,configs)

        while 1==1 :
            sleep(10)
            # il prend le dernier mail, le mail le plus haut dans l'application 
            for msg in mailbox.fetch(limit=1, reverse=True):
                surveille.detect_alerte(msg,configs,gere_alerte)
                  #print(configs.expediteur, configs.ordre,configs.employer) 
                  #objet du mail ex : mission astreint N°XXXX-XXXX  

            # TODO : une classe communication pour transmettre et recevoir les alertes et acquittement respectivement
            com_t.transmission(com,configs)
            com_t.reception(com)
                 

def run() :
    global com, configs, gere_alerte,surveille,com_t
    com_t=communication
    surveille=surveillance 
    configs=config()
    configs.load_configs()
    gere_alerte= gerer_alerte()
    #print(configs.broker,configs.port,configs.topic_reception)
    com=MQTT(configs.broker,configs.port,configs.topic_reception)
    com.start() 
    main()
if __name__=="__main__" :
    run()