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
               #print(file.iloc[i,0]) affiche l'uid 
               if check == False :
                    # l'alerte n'a pas encore été transmise
                    # transmission
                    count_envoi+=1
                    #print(type(file.iloc[i,0]))
                    com.send(configs.topic_envoie,int(file.iloc[i,0]),configs.broker,configs.port)
                    print("envoie réussit")
                    # mise à jour du fichier csv
                    # On met la transmission à true car la transmission a déjà été effectué
                    file.iloc[i,1]=True
                    file.to_csv("docs/acquittement_log.csv", header=None,index=False,sep=",")
          if count_envoi == 0 :
             pass 
          else :
               print(f"J'ai transmis {count_envoi} alerte(s) au broker ")            
     def reception(com=None):
            # Ce poste prouve bien que la reception se fait tout le temps qu'il y'a la donnée 
            #print(type(com.data))
            if com.data == None :
               pass
            else :
                 print(f"j'ai reçu ca {com.data}")
            # je remet le data à None pour la prochaine reception
            info=int(com.data)
            com.data=None 
            # TODO acquittement 
            file=read_csv("docs/acquittement_log.csv",header=None, sep=",")
            count_recois=0
            for i in range(len(file)):
                   check=file.iloc[i,5]
                   #print(file.iloc[i,5])
                   # On garanti également l'unicité d'acquittement
                   if info==file.iloc[i,0] and check == False :
                        count_recois+=1
                        print("L'astreint a fait l'acquittement")
                        file.iloc[i,5]=True
                        file.to_csv("docs/acquittement_log.csv", header=None,index=False,sep=",")     
            if count_recois == 0 :
                 pass
            else :
                 print("j'ai fait la mise à jour du log des acquittements veuillez l'ouvrir")
            



if __name__=="__main__" :
     a=communication
     a.transmission()           