# # import tkinter as tk
# #
# # def afficher_frame_1():
# #     frame_2.pack_forget()
# #     frame_1.pack()
# #
# # def afficher_frame_2():
# #     frame_1.pack_forget()
# #     frame_2.pack()
# #
# # # Création de la fenêtre principale
# # fenetre = tk.Tk()
# #
# # # Création des frames
# # frame_1 = tk.Frame(fenetre, width=200, height=200, bg="red")
# # frame_2 = tk.Frame(fenetre, width=200, height=200, bg="blue")
# #
# # # Création des boutons pour permuter les frames
# # bouton_1 = tk.Button(fenetre, text="Afficher Frame 1", command=afficher_frame_1)
# # bouton_2 = tk.Button(fenetre, text="Afficher Frame 2", command=afficher_frame_2)
# #
# # # Placement des boutons dans la fenêtre
# # bouton_1.pack()
# # bouton_2.pack()
# #
# #
# # # Création des boutons pour permuter les frames
# # bouton_3 = tk.Button(frame_1, text=" bonjour", )
# # bouton_4 = tk.Button(frame_2, text="bonsoir", )
# #
# # # Placement des boutons dans la fenêtre
# # bouton_3.place(x=50,y=50)
# # bouton_4.place(x=50,y=50)
# #
# #
# # # Affichage initial de la frame 1
# # frame_1.pack()
# #
# # # Lancement de la boucle principale de la fenêtre
# # fenetre.mainloop()


# import customtkinter
# from tkinter import *
# from tkinter import messagebox
# import random
#
#
#
# def no(event=None):
#     messagebox.showinfo("Félicitation","Grace à toi l'èspece survivra.\n\n  Un grand merci à toi bro...")
#     quit()
#
# def motionMouse(event):
#     btnYes.place(x=random.randint(20,440), y=random.randint(190,425))
#
#
#
# root =customtkinter.CTk()
# root.geometry("500x500")
# root.title("La survie")
# root.resizable(width=False,height=False)
# root.config(bg="black")
#
#
# label = customtkinter.CTkLabel(root, text="La survie de l'èspece dépendra de ta réponse \n \n Est ce que tu es gay ?",text_color="white", bg_color="black",fg_color="black", font=("Arial",20, "bold"))
# label.pack(pady=10)
# btnYes= customtkinter.CTkButton(root,text="Oui",font=("Arial",20, "bold"), width=60)
# btnYes.place(x=330, y=100)
# btnYes.bind("<Enter>", motionMouse)
#
# btnNo= customtkinter.CTkButton(root,text="Non",font=("Arial",20, "bold"),width=60,command=no)
# btnNo.place(x=110, y=100)
# root.bind("<Return>", no)
# root.mainloop()

#
#

import tkinter as tk
from tkinter import ttk
import gettext

# Création de la fenêtre
window = tk.Tk()

# Configuration de gettext
lang = 'en'  # Langue par défaut
translations = gettext.translation('messages', localedir='locales', languages=[lang])
translations.install()

# Fonction pour changer la langue
def change_language():
    selected_lang = language_combobox.get()
    translations = gettext.translation('messages', localedir='locales', languages=[selected_lang])
    translations.install()
    # Mettre à jour les textes dans l'interface graphique
    label_text.set(gettext.gettext("Hello, World!"))
    button_text.set(gettext.gettext("Click Me"))

# Label
label_text = tk.StringVar()
label = ttk.Label(window, textvariable=label_text)
label.pack()

# Bouton
button_text = tk.StringVar()
button = ttk.Button(window, textvariable=button_text)
button.pack()

# Combobox pour sélectionner la langue
language_combobox = ttk.Combobox(window, values=['en', 'fr', 'es'])  # Ajoutez les langues que vous voulez prendre en charge
language_combobox.set(lang)  # Langue par défaut
language_combobox.bind("<<ComboboxSelected>>", change_language)
language_combobox.pack()

# Lancer la boucle principale de l'interface graphique
window.mainloop()



# var1 = int(input(f"entrer un premier nombre "))
# var2 = int(input(f"entrer un deuxieme nombre "))
# var3 = int(input(f"entrer un troisieme nombre "))

# if var1>var2 and var1>var3 :
#     print("le premier plus grand est "+ var1)
#     premier_plus_grand = var1
# elif var2>var1 and var2>var3 :
#     print(f"le premier plus grand est {var2} ")
#     premier_plus_grand = var2
# elif var3>var1 and var3>var2 :
#     print(f"le premier plus grand est {var3} ")
#     premier_plus_grand = var3
#
# if var1>var2 and var2>var3 :
#     print(f"le premier plus grand est {var1} ")
#     print(f"le deuxieme plus grand est {var2}")
#     print(f"le troisieme plus grand est {var3} ")
#     #deuxieme_plus_grand = var2
# elif var1>var3 and var3>var2 :
#     print(f"le premier plus grand est {var1} ")
#     print(f"le deuxieme plus grand est {var3}")
#     print(f"le troisieme plus grand est {var2} ")
#     #deuxieme_plus_grand = var3
# elif var2>var1 and var1>var3 :
#     print(f"le premier plus grand est {var2} ")
#     print(f"le deuxieme plus grand est {var1}")
#     print(f"le troisieme plus grand est {var3} ")
#     #deuxieme_plus_grand = var1
# elif var2>var3 and var3>var1 :
#     print(f"le premier plus grand est {var2} ")
#     print(f"le deuxieme plus grand est {var3}")
#     print(f"le troisieme plus grand est {var1} ")
#     #deuxieme_plus_grand = var3
# elif var3>var1 and var1>var2 :
#     print(f"le premier plus grand est {var3} ")
#     print(f"le deuxieme plus grand est {var1}")
#     print(f"le troisieme plus grand est {var2} ")
#     #deuxieme_plus_grand = var1
# elif var3>var2 and var2>var1 :
#     print(f"le premier plus grand est {var3} ")
#     print(f"le deuxieme plus grand est {var2}")
#     print(f"le troisieme plus grand est {var1} ")
#     #deuxieme_plus_grand = var2
