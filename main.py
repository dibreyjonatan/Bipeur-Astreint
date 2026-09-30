from load_auth import donnes_connexions
from imap_tools import MailBox

(email,mot_de_passe)=donnes_connexions()

with MailBox("imap.gmail.com").login(email, mot_de_passe) as mailbox:
    for msg in mailbox.fetch(limit=10, reverse=True):
        print(msg.subject)
        print(msg.from_)
        print(msg.date)
        print(msg.text)
        print()
print("Connexion réussie !")
