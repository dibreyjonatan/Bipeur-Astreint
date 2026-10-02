
from datetime import datetime
import csv

class surveillance():
    def __init__():
        pass
    def detect_alerte(com,msg,configs,gere_alerte):
         pass 
         if msg.from_ == configs.expediteur and configs.ordre in msg.subject.lower() and configs.employer in msg.subject.lower() :
                # test de présence d'un mail déjà détecter 
                # si 0, donc pas encore detecter, si 1 dejè détecter 
                #print(mail_uid) 
                test_mail=1
                _=gere_alerte.test_alerte_enregistre(msg.uid)
                #print(deja_detecter)
                #print(gere_alerte.presence)
                if gere_alerte.presence == 1 :
                        print("c'est une alerte mais déjà détecter !")
                    
                            #donc l'alerte est unique et non redondante
                if gere_alerte.presence  == 0 and test_mail==1:
                        print("alerte provient du boss !!!")
                        print("le uid du mail est :",msg.uid)
                        print("date d'émission",msg.date)
                        print("date de détection",datetime.now())
                        ## Ecriture dans le fichier csv d'alerte 
                        # uid, expediteur,date_alerte,date_detection
                        with open('docs/alerte_log.csv', mode='a', newline='') as fichier:
                                write= csv.writer(fichier)
                                write.writerow([msg.uid,msg.from_,msg.date,datetime.now()])
                            ## Envoie alerte, qui sera uid 
                        com.send(configs.topic_envoie,msg.uid,configs.broker,configs.port)
                        print("envoie réussit")
                        ## Je fais le fichier d'acquittement avec un status false 
                        ## le fichier csv d'acquittement est le suivant
                        ## uid, date d'émission, date d'acquittement, status
                        with open('docs/acquittement_log.csv', mode='a', newline='') as fichier:
                                write= csv.writer(fichier)
                                write.writerow([msg.uid,msg.from_,datetime.now(),"date_acquittement", False])
                            
        
if __name__== "__main__" :
       a=surveillance
       #a.detect_alerte(None,None,None,None)
