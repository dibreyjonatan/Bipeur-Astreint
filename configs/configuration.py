
class config() :
    
    def __init__(self,L=[],broker=None,port=None,topic_e=None,topic_r=None,expediteur=None,ordre=None,employer=None):
        pass
        self.L=L
        self.broker=broker
        self.port=port
        # topic_envoie ="/envoie"   envoie de la supervision --> Broker MQTT
        # topic_reception="/sender"  reception broker MQTT --> PC supervision 
        self.topic_envoie=topic_e
        self.topic_reception=topic_r
        self.expediteur=expediteur
        self.ordre=ordre
        self.employer=employer

    def read_configs(self):
        with open('configs/configuration.txt','r') as f:
         lignes=f.readlines()
         #print(lignes)
        for ligne in lignes :
           #print(ligne.split('='))
           x=ligne.split('=')  # permet de creer une liste de deux columns par ligne.
           #strip c'est pour enlever les \n à la fin de chaque ligne retenu
           # l'idée ici est de prendre la donnée à la position 1 et d'enlever le \n
           self.L.append(x[1].strip('\n'))
    def load_configs(self):
        self.read_configs()       
        self.broker=self.L[0].strip(' ')
        self.port=int(self.L[1])
        self.topic_envoie=self.L[2].strip(' ')
        self.topic_reception=self.L[3].strip(' ')
        self.expediteur=self.L[4].strip(' ')
        self.ordre=self.L[5].strip(' ')
        self.employer=self.L[6].strip(' ')
if __name__=="__main__" :
    a=config()
    a.load_configs()
    print(a.broker, a.port, a.topic_envoie, a.topic_reception, a.expediteur, a.ordre, a.employer)
    print(a.broker, a.port, a.topic_envoie, a.topic_reception, a.expediteur, a.ordre, a.employer)
