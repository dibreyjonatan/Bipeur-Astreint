class gerer_alerte() :
     def __init__():
          pass 
     def test_alerte_enregistre(new_alerte):
          #print("test")
          presence=False
          with open("docs/alerte_log.csv",'r') as f :
               lignes=f.readlines()
          for ligne in lignes  :
              row=ligne.split(',')    
              if int(row[0]) == new_alerte :
                   presence==True 
          return presence            

if __name__=="__main__" :
     a=gerer_alerte
     print(a.test_alerte_enregistre(2736))