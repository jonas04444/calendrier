from tkinter import *

#création de la fenetre
master = Tk()

#reglage de la bordure ainsi que de la taille de la fenetre
#personnalisation de la couleur et du logo
master.title("horaire")
master.geometry("1080x720")
master.minsize(480, 360)
master.iconbitmap("logo-tec.ico")
master.config(background='#E3E764')

#créer du texte et personnalisation du texte
lable_title = Label(master, text="affichage de l'horaire", font=("Arial", 30), bg='#E3E764')
lable_title.pack()

#on ajoute d'autre texte
lable_title = Label(master, text="vous pouvez consulter votre horaire", font=("Arial", 30), bg='#E3E764')
lable_title.pack()

#affichage de la fenetre
master.mainloop()
