from surveillance import surveillance
class gerer_alerte() :
     def __init__(self,presence=None):
          self.presence=presence
          pass 
     def test_alerte_enregistre(self,new_alerte):
          #print("test")
         
          with open("docs/alerte_log.csv",'r') as f :
               lignes=f.readlines()
          
          self.presence=0   # donc par défaut on suppose que l'alerte est nouvelle 
          L=[]  
          for ligne in lignes  :
              row=ligne.split(',')   
              L.append(row[0]) 
          #return L 
          if new_alerte in L :
               self.presence=1 #donc elle est déjà presente
          
          return self.presence                    
      
     def recouvrement(self,data,configs) :
          # on a besoin de la methode detecter_alerte 
          # Avant recouvrement on calcul la longueur du fichier csv avant 
          with open("docs/alerte_log.csv",'r') as f :
                         lignes=f.readlines()
          length_b=len(lignes) 

          # on boucle sur les derniers 100 messages 
          a=surveillance
          for msg in data :
                a.detect_alerte(msg,configs,gere_alerte=self)  

          with open("docs/alerte_log.csv",'r') as f :
                         lignes=f.readlines()
          length_a=len(lignes)   

          if (length_a - length_b ) == 0 :
                 print("Le système n'a manqué aucune alerte pendant la deconnexion")
          else :
                 print(f"le système a détecter {length_a-length_b} alertes pendant sa coupure et les a ajouter au fichier log")       
                 

                   
                    

          pass 
if __name__=="__main__" :
     a=gerer_alerte()
     print(a.test_alerte_enregistre(10908))
     #print(a.presence)