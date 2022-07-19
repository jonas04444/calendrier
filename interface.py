from tkinter import *

#création de la fenetre
master = Tk()

#reglage de la bordure ainsi que de la taille de la fenetre
#personnalisation de la couleur et du logo
master.title("horaire")
master.geometry("1080x720")
master.minsize(480, 360)
master.iconbitmap("logo-tec.ico")


master.config(background="#E3E764")

#création frame
frame = Frame(master, bg='#E3E764')

#créer du texte et personnalisation du texte
lable_title = Label(master, text="affichage de l'horaire", font=("Arial", 30), bg='#E3E764', bd=1, relief=SUNKEN)
lable_title.pack()

#on ajoute d'autre texte
lable_title = Label(master, text="vous pouvez consulter votre horaire", font=("Arial", 30), bg='#E3E764')
lable_title.pack()

#ajout d'un bouton pour afficher l'horaire
yt_button = Button(frame, text="afficher horaire", font=("Arial", 30), bg='#E3E764', width=20, height=1)
yt_button.pack()

#bouton pour changement de service
yt_button = Button(frame, text="changement de service", font=("Arial", 30), bg='#E3E764', width=20, height=1)
yt_button.pack()

yt_button = Button(frame, text="demande de congés", font=("Arial", 30), bg='#E3E764', width=20, height=1)
yt_button.pack()

#afficher la frame
frame.pack(expand=YES)

#affichage de la fenetre
master.mainloop()
