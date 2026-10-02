
class config() :
    
    def __init__(self,L=[],broker=None,port=None,topic_e=None,topic_r=None,expediteur=None,ordre=None,employer=None):
        pass
        self.L=L
        self.broker=broker
        self.port=port
        self.topic_envoie=topic_e
        self.topic_reception=topic_r
        self.expediteur=expediteur
        self.ordre=ordre
        self.employer=employer

    def load_configs(self):
        with open('configuration.txt','r') as f:
         lignes=f.readlines()
         #print(lignes)
        for ligne in lignes :
           #print(ligne.split('='))
           x=ligne.split('=')  # permet de creer une liste de deux columns par ligne.
           #strip c'est pour enlever les \n à la fin de chaque ligne retenu
           # l'idée ici est de prendre la donnée à la position 1 et d'enlever le \n
           self.L.append(x[1].strip('\n'))
       

a=config()
a.load_configs()
print(a.L)
