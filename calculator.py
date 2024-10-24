import customtkinter
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image


event =None

####                                 FONCTION POUR AFFICHER LES NOMBRES ET LES SIGNES DANS LE "result_entry"
i=0
equation=""


def show( value):
    global i
    global equation
    if value=="%":
        value="/100"
    equation+=value
    result_entry.insert(i,value)
    i=i+1

####                                 FONCTION POUR VIDER LE "result_entry"
def clear(event=None):
    global equation
    result_entry.delete(0, END)
    equation=""

####                                 FONCTION POUR EFFECTUER LES CALCULS
def calculate(event=None):
    try:
        global equation
        result = ""
        result = eval(equation)
        clear()
        result_entry.insert(0,result)
        equation+=result_entry.get()
    except:
        pass#messagebox.showerror(title="error",message="Vous devez entrer un nombre valide.")



def delete(event=None):
    global equation
    result_entry.delete(END)








####                                 FONCTION POUR ALLER AU FRAME DE LA L'HISTORIQUE
def go_to_main_frame():
    frame_calc.grid_forget()
    #main_frame = customtkinter.CTkFrame(app, height=427, width=295)
    main_frame.grid(row=0, column=0, sticky="nsew")  # show main frame


####                                 FONCTION POUR RETOURNER AU FRAME DE LA CALCULATRICE
def back_event():
    main_frame.grid_forget()
    frame_calc.grid(row=0, column=0, padx=0, pady=0,)


####                                 FONCTION POUR ALLER AU FRAME DE L'HISTORIQUE
def go_to_historic_frame():
    main_frame.grid_forget()
    historic_frame.grid(row=0, column=0, sticky="nsew")

####                                 FONCTION POUR RETOURNER AU FRAME DES OPTIONS
def back_to_main_frame1():
    historic_frame.grid_forget()
    main_frame.grid(row=0, column=0, padx=0, pady=0,)


####                                 FONCTION POUR ALLER AU FRAME DES PARAMETRES
def go_to_setting_frame():
    main_frame.grid_forget()
    setting_frame.grid(row=0, column=0, sticky="nsew")

####                                 FONCTION POUR RETOURNER AU FRAME DES OPTIONS
def back_to_main_frame2():
    setting_frame.grid_forget()
    main_frame.grid(row=0, column=0, padx=0, pady=0,)



####                      FONCTION POUR CHANGER LE THEME
def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


####                      FONCTION POUR CHANGER LA LANGUE
def change_language_event( ):
    pass



###########                FONCTION POUR CHANGER LE SCALING



# def change_scaling_event( new_scaling: str):
#     new_scaling_float = int(new_scaling.replace("%", "")) / 100
#     customtkinter.set_widget_scaling(new_scaling_float)






customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

app = customtkinter.CTk()
app.title("calculator")
app.geometry("294x438")
app.config(bg="#000000")
app.iconbitmap("icons\calculator.ico")
# app.resizable(width=False, height=False)
app.minsize(width=294,height=438)
app.maxsize(width=294,height=438)
# app.grid_columnconfigure(0, weight=1)
# app.grid_columnconfigure((0,1,2,3), weight=1)
# #app.grid_rowconfigure((0,1,2,3,4,5), weight=1)




font1= ("Arial",24 ,"bold")
font2= ("Arial",20 ,"bold")

#                                 LE FRAME DE LA CALCULATRICE

frame_calc = customtkinter.CTkFrame(app, height=438, width=298)
frame_calc.grid(row=0, column=0, padx=0, pady=0,)

#                                    CHARGEMENT DES IMAGES

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")

hamberger_menu = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path,"hamburger-menu.png")), size=(30,25))
home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"home_dark.png")),
                                    dark_image=Image.open(os.path.join(image_path,"home_dark.png")) ,size=(18,18))
back_arrow = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path,"back_arrow.png")), size=(22,17))
historic_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path,"history_black.png")),
                                        light_image=Image.open(os.path.join(image_path,"history_black.png")), size=(22,22))
setting_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path,"setting.png")), size=(22,22))
theme_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path,"theme.png")), size=(18,18))




####                                        BOUTON HOME

home_button = customtkinter.CTkButton(frame_calc, corner_radius=1, height=8,width=8, text="Home",border_spacing=1,
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover=False,
                                                   image=home_image ,compound="left", anchor="w" )
home_button.grid(row=0, column=0,padx=(10,0),pady=(8,10), sticky="nw")



##############                        BOUTON HAMBERGER
hamberger_menu_button = customtkinter.CTkButton(frame_calc, corner_radius=1, height=8,width=8, text="",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=hamberger_menu ,compound="left", anchor="e" , command=go_to_main_frame)
hamberger_menu_button.grid(row=0, column=3,padx=(0,10),pady=(2,16), sticky="ne")



result_entry = customtkinter.CTkEntry(frame_calc,height=70, font=font1 ,width=274,border_color="gray",border_width=0 )
result_entry.grid(row=0, column=0,columnspan=5, padx=(10, 10), pady=(43,8),sticky="new" )
#result_entry.grid_columnconfigure(4, weight=1
# )

#                              BOUTON POUR VIDER LE "result_entry"

button1 = customtkinter.CTkButton(frame_calc,command=clear,text="C",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button1.grid(row=1, column=0, padx=10, pady= 10 ,sticky="nw")
app.bind("<Delete>",clear)


#                                       BOUTON DU MODULO

button2 = customtkinter.CTkButton(frame_calc,command=lambda:show("%"),text="%",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button2.grid(row=1, column=1, padx=0, pady=10, sticky="nw")

#                                      BOUTON POUR SUPPRIMER

button3 = customtkinter.CTkButton(frame_calc,command=delete,text="DEL",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button3.grid(row=1, column=2, padx=0, pady= 10 ,sticky="nw")
app.bind("<BackSpace>", delete)


#                            BOUTON POUR FAIRE LA DIVISION ENTIERE
button4 = customtkinter.CTkButton(frame_calc,command=lambda:show("/"),text="/",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button4.grid(row=1,column=3, padx=(0,10) , pady=10,sticky="nw" )

#                            BOUTON POUR FAIRE LA MULTIPLICATION

button5 = customtkinter.CTkButton(frame_calc,command=lambda:show("*"),text="x",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button5.grid(row=2, column=3,  padx=(0,10), pady=10, sticky="nw")


#                                 BOUTON DU CHIFFRE 7
button6 = customtkinter.CTkButton(frame_calc,command=lambda:show("7"),text="7",font=font2,width=60,height=40,fg_color="#808080",hover_color="#2e2a27")
button6.grid(row=2, column=0, padx=10, pady= 10 ,sticky="nw")


##                                 BOUTON DU CHIFFRE 8
button7 = customtkinter.CTkButton(frame_calc,command=lambda:show("8"),text="8",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button7.grid(row=2, column=1, padx=(0,10), pady=10, sticky="nw")

#                                 BOUTON DU CHIFFRE 9

button8 = customtkinter.CTkButton(frame_calc,command=lambda:show("9"),text="9",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button8.grid(row=2, column=2, padx=(0, 10), pady=10, sticky="nw")

#                                 BOUTON POUR L'ADDITION

button9 = customtkinter.CTkButton(frame_calc,command=lambda:show("+"),text="+",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button9.grid(row=3, column=3, padx=(0,10), pady=10, sticky="nw")

##                                 BOUTON DU CHIFFRE 4

button10 = customtkinter.CTkButton(frame_calc,command=lambda:show("4"),text="4",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button10.grid(row=3, column=0, padx=10, pady= 10 ,sticky="nw")

##                                  BOUTON DU CHIFFRE 5

button11 = customtkinter.CTkButton(frame_calc,command=lambda:show("5"),text="5",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button11.grid(row=3, column=1, padx=(0,10), pady=10, sticky="nw")

##                                  BOUTON DU CHIFFRE 6
button12 = customtkinter.CTkButton(frame_calc,command=lambda:show("6"),text="6",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button12.grid(row=3, column=2, padx=(0, 10), pady=10, sticky="nw")

#                                  BOUTON POUR LA SOUSTRACTION

button13 = customtkinter.CTkButton(frame_calc,command=lambda:show("-"),text="-",font=font2,width=60,height=40,fg_color="#b5520b",hover_color="#da610a")
button13.grid(row=4, column=3, padx=(0,10), pady=10, sticky="nw")

#                                     BOUTON DU CHIFFRE 1
button14 = customtkinter.CTkButton(frame_calc,command=lambda:show("1"),text="1",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button14.grid(row=4, column=0, padx=10, pady= 10 ,sticky="nw")


##                                   BOUTON DU CHIFFRE 2

button15 = customtkinter.CTkButton(frame_calc,command=lambda:show("2"),text="2",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button15.grid(row=4, column=1, padx=(0,10), pady=10, sticky="nw")


##                                    BOUTON DU CHIFFRE 3

button16 = customtkinter.CTkButton(frame_calc,command=lambda:show("3"),text="3",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button16.grid(row=4, column=2, padx=(0, 10), pady=10, sticky="nw")


####                                 BOUTON DU CHIFFRE 0
button17 = customtkinter.CTkButton(frame_calc,command=lambda:show("0"),text="0",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button17.grid(row=5, column=0, padx=10, pady= 10 ,sticky="nw")


####                                 BOUTON POUR LA VIRGULE

button18 = customtkinter.CTkButton(frame_calc,command=lambda:show("."),text=".",font=font2,width=60,height=40,fg_color="#2e2a27",hover_color="#2e2a27")
button18.grid(row=5, column=1, padx=(0,10), pady= 10 ,sticky="nw")
#app.bind("<period>",show)


####                                 BOUTON POUR L'EGALITE

button19 = customtkinter.CTkButton(frame_calc,command=calculate,text="=",font=font2,width=133,height=40,fg_color="#b5520b",hover_color="#da610a")
button19.grid(row=5, column=2,columnspan=2, padx=(0,10), pady=10, sticky="nw")
app.bind("<Return>",calculate)



####                                       FRAME DES OPTIONS

main_frame = customtkinter.CTkFrame(master=app,width=295, height=425)
# main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(1, weight=1)


####                            BOUTON RETOUR AU FRAME DE LA CALCULATRICE

back_arrow_button = customtkinter.CTkButton(main_frame, corner_radius=1, height=8,width=10, text="",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),image=back_arrow ,compound="left", anchor="w", command=back_event )
back_arrow_button.place(x=5,y=5 )

####                             BOUTON HISTORIQUE

historic_button = customtkinter.CTkButton(main_frame, corner_radius=1, height=11,width=295, text="Historique",border_spacing=10,
                                                   font=("arial",15),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=historic_image ,compound="left", anchor="w", command=go_to_historic_frame )
historic_button.place(x=0,y=46)


####                             BOUTON PARAMETRE

setting_button = customtkinter.CTkButton(main_frame, corner_radius=1, height=11,width=295, text="parametre",border_spacing=11,
                                                    font=("arial",15),fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=setting_image ,compound="left", anchor="w",command=go_to_setting_frame)
setting_button.place(x=0,y=86 )


####                                        FRAME DE L'HISTORYQUE

historic_frame = customtkinter.CTkFrame(master=app,width=295, height=425)


####                            BOUTON RETOUR AU FRAME DES OPTIONS

back_arrow_button2 = customtkinter.CTkButton(historic_frame, corner_radius=1, height=8,width=10, text="",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),image=back_arrow ,compound="left", anchor="w", command=back_to_main_frame1 )
back_arrow_button2.place(x=5,y=5 )

###                                     TITRE: HISTORIQUE

title_historic_frame = customtkinter.CTkLabel(historic_frame,text="HISTORIQUE",font=("Arial", 20, "bold","underline"),image=historic_image,compound="left")
title_historic_frame.place(x=10,y=33)#pack(ipadx=20,ipady=20 ,expand=True)



####                                        FRAME DES PARAMETRES

setting_frame = customtkinter.CTkFrame(master=app,width=295, height=425)


####                            BOUTON RETOUR AU FRAME DES OPTIONS

back_arrow_button3 = customtkinter.CTkButton(setting_frame, corner_radius=1, height=8,width=10, text="",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),image=back_arrow ,compound="left", anchor="w", command=back_to_main_frame2 )
back_arrow_button3.place(x=5,y=5 )

###                                     TITRE: PARAMETRES

title_setting_frame = customtkinter.CTkLabel(setting_frame,text="PARAMETRE",font=("Arial", 20, "bold","underline"),image=setting_image,compound="left")
title_setting_frame.place(x=10,y=33)#pack(ipadx=20,ipady=20 ,expand=True)

########                               CHOISIR LE THEME

appearance_mode_label = customtkinter.CTkLabel(setting_frame, text="Thème:", font=("arial",15),image=theme_image, compound="left", anchor="w")
appearance_mode_label.place(x=35,y=88)
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(setting_frame, values=["Light", "Dark", "System"], width=155, height=20,
                button_hover_color="#da610a",dropdown_hover_color="#da610a", button_color="#b5520b",fg_color=("#b5520b"),command=change_appearance_mode_event)
appearance_mode_optionemenu.place(x=122,y=90)
appearance_mode_optionemenu.set("Dark")

########                               CHOISIR LA LANGUE

language_label = customtkinter.CTkLabel(setting_frame, text="Langue:", font=("arial",15),image=theme_image, compound="left", anchor="w")
language_label.place(x=35,y=124)
language_optionemenu = customtkinter.CTkOptionMenu(setting_frame, values=["French", "English", "System"], width=155, height=20,
                button_hover_color="#da610a",dropdown_hover_color="#da610a", button_color="#b5520b",fg_color=("#b5520b"),command=change_language_event)
language_optionemenu.place(x=122,y=126)
language_optionemenu.set("System")

#####                     CHOISIR LE SCALING
#
# scaling_label = customtkinter.CTkLabel(setting_frame, text="UI Scaling:", anchor="w")
# scaling_label.place(x=35,y=148)
# scaling_optionemenu = customtkinter.CTkOptionMenu(setting_frame, values=["80%", "90%", "100%", "110%", "120%"],
#                                                                command=change_scaling_event)
# scaling_optionemenu.place(x=122,y=150)
# scaling_optionemenu.set("100%")





def control_num_keypad(event):
    print(event.keysym)
    if event.keysym == "0":
        show("0")
    elif event.keysym == "1":
        show("1")
    elif event.keysym == "2":
        show("2")
    elif event.keysym == "3":
        show("3")
    elif event.keysym == "4":
        show("4")
    elif event.keysym == "5":
        show("5")
    elif event.keysym == "6":
        show("6")
    elif event.keysym == "7":
        show("7")
    elif event.keysym == "8":
        show("8")
    elif event.keysym == "9":
        show("9")
    elif event.keysym == "period":
        show(".")
    elif event.keysym == "slash":
        show("/")
    elif event.keysym == "asterisk":
        show("*")
    elif event.keysym == "plus":
        show("+")
    elif event.keysym == "minus":
        show("-")
    elif event.keysym == "percent" :
        show("%")


app.bind("<Key>",control_num_keypad)





app.mainloop()