# Cette classe sera chargé de la communication avec l'exterieur
from pandas import read_csv 
class communication :
     def __init__():
          pass
     def transmission(com=None, configs=None):
          # lecture du fichier acquittement
          # si l'alerte n'a pas encore été émise, envoyer et remplacer par true 
          file=read_csv("docs/acquittement_log.csv",header=None, sep=",")
          #print("taille du fichier",len(file))
          #print(file)
          count_envoi=0
          for i in range(len(file)):
               # lecture de la deuxième column
               check=file.iloc[i,1]
               print(file.iloc[i,0])
               if check == False :
                    # l'alerte n'a pas encore été transmise
                    # transmission
                    count_envoi+=1
                    #com.send(configs.topic_envoie,file.iloc[i,0],configs.broker,configs.port)
                    print("envoie réussit")
                    # mise à jour du fichier csv
                    # On met la transmission à true car la transmission a déjà été effectué
                    file.iloc[i,1]=True
                    file.to_csv("docs/acquittement_log.csv", header=None,index=False,sep=",")
          if count_envoi == 0 :
             pass 
          else :
               print(f"J'ai transmis {count_envoi} alertes au broker ")            
     def reception(com=None):
            if com.data == None :
               pass
            else :
                 print(f"j'ai reçu ca {com.data}")
                 

if __name__=="__main__" :
     a=communication
     a.transmission()           