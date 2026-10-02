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
               
            #  if int(row[0]) == new_alerte :
             #      print(row[0])
              #     self.presence=k   
               #    k=1     
          return self.presence                    
          #return k           

if __name__=="__main__" :
     a=gerer_alerte()
     print(a.test_alerte_enregistre(10908))
     #print(a.presence)