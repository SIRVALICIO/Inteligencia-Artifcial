import tkinter as tk
import tkinter.messagebox
from tkinter import ttk







master=tk.Tk()
checkMarron=tk.BooleanVar()
checkBronce=tk.BooleanVar()
checkMohoVerAzu=tk.BooleanVar()
checkAmarillo=tk.BooleanVar()
checkPuntitos=tk.BooleanVar()
checkBordeAmarillo=tk.BooleanVar()
checkCentroGris=tk.BooleanVar()
checkAreaGris=tk.BooleanVar()
checkAmarilloTranslucido=tk.BooleanVar()
checkAnillosgrises=tk.BooleanVar()
checkParchesBlancos=tk.BooleanVar()
checkFolioCafe=tk.BooleanVar()
checkSemillasHinchadas=tk.BooleanVar()
chcekAbanicos=tk.BooleanVar()
checkSecamiento=tk.BooleanVar()
checkPerdidaBrillo=tk.BooleanVar()
checkPudricion=tk.BooleanVar()


def investigar():

    global checkMarron
    print(checkMarron)
    global checkBronce
    global checkMohoVerAzu

    global checkAmarillo
    global checkPuntitos
    global checkBordeAmarillo
    global checkCentroGris
    print(checkCentroGris.get())
    print(checkPuntitos.get())
    global checkAreaGris

    global checkAmarilloTranslucido
    global checkAnillosgrises
    global checkParchesBlancos
    global checkFolioCafe
    global checkSemillasHinchadas
    global chcekAbanicos
    global checkSecamiento
    global checkPerdidaBrillo
    global checkPudricion

    if checkMarron.get()==True and checkAmarillo==False:

        if checkMohoVerAzu.get()==True:

            LabelEnfermedad.config(text="La enfermedad es: Germen marrón")
            LabelEnfermedad.place(x=600,y=25)
        elif checkSemillasHinchadas.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Fitotoxicidad por pesticidas")
            LabelEnfermedad.place(x=600, y=25)
        elif checkParchesBlancos.get() == True or chcekAbanicos.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Pudrición de la semilla")
            LabelEnfermedad.place(x=600, y=25)
    if checkMarron.get()==True or checkSecamiento.get()==True:
        print("aqui")
        if checkPuntitos.get()==True or checkBordeAmarillo.get()==True:
            print("llegue 2")
            if checkCentroGris.get()==True:
                LabelEnfermedad.config(text="La enfermedad es: Botryodiplodia")
                LabelEnfermedad.place(x=600, y=25)
            elif checkAreaGris.get()==True:
                LabelEnfermedad.config(text="La enfermedad es: Melanconim")
                LabelEnfermedad.place(x=600, y=25)
        elif checkAmarilloTranslucido.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Glomerella cingulata")
            LabelEnfermedad.place(x=600, y=25)
        else:
            LabelEnfermedad.config(text="La enfermedad es: Pestalotia")
            LabelEnfermedad.place(x=600, y=25)
    if checkAmarillo.get()==True or checkSecamiento.get()==True:
        if checkBordeAmarillo.get()==True or checkAnillosgrises.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Curvalaria masculans")
            LabelEnfermedad.place(x=600, y=25)
    if checkPudricion.get()==True or checkPerdidaBrillo.get()==True:
        if checkFolioCafe.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Marchitez sorpresiva")
            LabelEnfermedad.place(x=600, y=25)

        elif checkBronce.get()==True:
            LabelEnfermedad.config(text="La enfermedad es: Marchites Letal")
            LabelEnfermedad.place(x=600, y=25)




master.geometry("1380x980")
LabelElegir=tk.Label(master,text="Eliga los sintomas que correspondan al estado acutal de su palma: ")

LabelManchas=tk.Label(master,text="color de maanchas pronunciadas generales: ")
checkparaAmarillo=ttk.Checkbutton(master , text="Amarillo",variable=checkAmarillo,onvalue=True,offvalue=False)
checkparaMarron= ttk.Checkbutton(master , text="Marron",variable=checkMarron,onvalue=True,offvalue=False)

LabelManchasDeHoja=tk.Label(master,text="color y tipos de las manchas en las hojas:")
checkparaPuntitos=ttk.Checkbutton(master , text="Puntitos negros",variable=checkPuntitos,onvalue=True,offvalue=False)
checkparaBordesAmarillos=ttk.Checkbutton(master , text="Bordes amarillos",variable=checkBordeAmarillo,onvalue=True,offvalue=False)
checkparaCentroGris=ttk.Checkbutton(master , text="Centro gris",variable=checkCentroGris,onvalue=True,offvalue=False)
checkparaAreaGris=ttk.Checkbutton(master , text="Areas grises",variable=checkAreaGris,onvalue=True,offvalue=False)
checkparaAmarilloTranslucido=ttk.Checkbutton(master , text="Borde amarillo translucido",variable=checkAmarilloTranslucido,onvalue=True,offvalue=False)
checkparaAnilloGris=ttk.Checkbutton(master , text="Anillos grises",variable=checkAnillosgrises,onvalue=True,offvalue=False)
checkparaParchesBlancos=ttk.Checkbutton(master , text="Parches blancos",variable=checkParchesBlancos,onvalue=True,offvalue=False)

LabelFolios=tk.Label(master,text="Color de decolarcion de los folios/hojas: ")
checkparaBronce= ttk.Checkbutton(master , text="Bronce",variable=checkBronce,onvalue=True,offvalue=False)
checkparaFolioCafe=ttk.Checkbutton(master , text="Cafe",variable=checkFolioCafe,onvalue=True,offvalue=False)

LabelOtros=tk.Label(master,text="Otras sintomas: ")
checkParaSemillas=ttk.Checkbutton(master , text="Semillas hinchadas",variable=checkSemillasHinchadas,onvalue=True,offvalue=False)
checkParaAbanicos=ttk.Checkbutton(master , text="Abanicos de color gris",variable=chcekAbanicos,onvalue=True,offvalue=False)
checkParaSecamiento=ttk.Checkbutton(master , text="Secamiento de la superficie de la hoja",variable=checkSecamiento,onvalue=True,offvalue=False)
checkParaPerdidaBrillo=ttk.Checkbutton(master , text="Perdida de brillo de los furtos",variable=checkPerdidaBrillo,onvalue=True,offvalue=False)
checkParaPudricion=ttk.Checkbutton(master , text="Pudricion de las raices",variable=checkPudricion,onvalue=True,offvalue=False)
checkparaMohoVerAzu= ttk.Checkbutton(master , text="Moho Verde/Azul",variable=checkMohoVerAzu,onvalue=True,offvalue=False)

botonInvestigar=tk.Button(master,text="Buscar enfermedad",command=investigar)

LabelEnfermedad=tk.Label(master,text="")
LabelSolucion=tk.Label(master,text="")

LabelElegir.place(x=0, y=0)

LabelManchas.place(x=0,y=25)

checkparaMarron.place(x=0, y=45)
checkparaAmarillo.place(x=0,y=65)
LabelManchasDeHoja.place(x=0,y=85)
checkparaPuntitos.place(x=0,y=105)
checkparaBordesAmarillos.place(x=0,y=125)
checkparaCentroGris.place(x=0, y=145)
checkparaAreaGris.place(x=0, y=165)
checkparaAmarilloTranslucido.place(x=0, y=185)
checkparaAnilloGris.place(x=0, y=205)
checkparaParchesBlancos.place(x=0, y=225)

LabelFolios.place(x=300,y=25)
checkparaBronce.place(x=300,y=45)
checkparaFolioCafe.place(x=300,y=65)

LabelOtros.place(x=300,y=85)
checkParaSemillas.place(x=300,y=105)
checkParaAbanicos.place(x=300,y=125)
checkParaSecamiento.place(x=300,y=145)
checkParaPerdidaBrillo.place(x=300,y=165)
checkParaPudricion.place(x=300,y=185)
checkparaMohoVerAzu.place(x=300,y=205)

botonInvestigar.place(x=300,y=225)





tk.mainloop()