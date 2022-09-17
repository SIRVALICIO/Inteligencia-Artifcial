import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import Canvas







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
checkParcheGris=tk.BooleanVar()


canvas=Canvas(master, width=1000, height=1000)
id13=canvas.create_oval(10,10,30,30)
id12=canvas.create_oval(10,10,30,30)
id11=canvas.create_oval(10,10,30,30)
id10=canvas.create_oval(10,10,30,30)
id9=canvas.create_oval(10,10,30,30)
id8=canvas.create_oval(10,10,30,30)
id7=canvas.create_oval(10,10,30,30)
id6=canvas.create_oval(10,10,30,30)
id5=canvas.create_oval(10,10,30,30)
id4=canvas.create_oval(10,10,30,30)
id3=canvas.create_oval(10,10,30,30)
id2=canvas.create_oval(10,10,30,30)
id1=canvas.create_oval(10,10,30,30)



texto13=canvas.create_text(15,15,text="13")
texto12=canvas.create_text(15,15,text="12")
texto11=canvas.create_text(15,15,text="11")
texto10=canvas.create_text(15,15,text="10")
texto9=canvas.create_text(15,15,text="9")
texto8=canvas.create_text(15,15,text="8")
texto7=canvas.create_text(15,15,text="7")
texto6=canvas.create_text(15,15,text="6")
texto5=canvas.create_text(15,15,text="5")
texto4=canvas.create_text(15,15,text="4")
texto3=canvas.create_text(15,15,text="3")
texto2=canvas.create_text(15,15,text="2")
texto1=canvas.create_text(15,15,text="1")


idMa=canvas.create_oval(10,10,30,30,outline='red')
idSe=canvas.create_oval(10,10,30,30,outline='red')
idAm=canvas.create_oval(10,10,30,30,outline='red')
idPer=canvas.create_oval(10,10,30,30,outline='red')
idPud=canvas.create_oval(10,10,30,30,outline='red')


textoMa=canvas.create_text(15,15,text="Ma")
textoSe=canvas.create_text(15,15,text="Se")
textoAm=canvas.create_text(15,15,text="Am")
textoPer=canvas.create_text(15,15,text="Per")
textoPud=canvas.create_text(15,15,text="Pud")

idGermen=canvas.create_oval(10,10,30,30,outline='green')
idFitoto=canvas.create_oval(10,10,30,30,outline='green')
idPudri=canvas.create_oval(10,10,30,30,outline='green')
idGlome=canvas.create_oval(10,10,30,30,outline='green')
idPestalo=canvas.create_oval(10,10,30,30,outline='green')
idBotryodil=canvas.create_oval(10,10,30,30,outline='green')
idMelan=canvas.create_oval(10,10,30,30,outline='green')
idCurvala=canvas.create_oval(10,10,30,30,outline='green')
idMarcPro=canvas.create_oval(10,10,30,30,outline='green')
idMarcLet=canvas.create_oval(10,10,30,30,outline='green')

textoGerme=canvas.create_text(15,15,text="Ger")
textoFitoto=canvas.create_text(15,15,text="Fit")
textoPudri=canvas.create_text(15,15,text="Pud")
textoGlome=canvas.create_text(15,15,text="Glo")
textoPestalo=canvas.create_text(15,15,text="Pes")
textoBotryodil=canvas.create_text(15,15,text="Bot")
textoMelan=canvas.create_text(15,15,text="Mel")
textoCurvala=canvas.create_text(15,15,text="Cur")
textoMarcPro=canvas.create_text(15,15,text="MaP")
textoMarcLet=canvas.create_text(15,15,text="MaL")

canvas.move(id13, 100 + 100, 300)
canvas.move(id12, 100 + 100, 350)
canvas.move(id11, 1 + 100, 0)
canvas.move(id10, 1 + 100, 50)
canvas.move(id9, 1 + 100, 100)
canvas.move(id8, 1 + 100, 150)
canvas.move(id7, 1 + 100, 200)
canvas.move(id6, 1 + 100, 250)
canvas.move(id5, 1 + 100, 300)
canvas.move(id4, 1 + 100, 350)
canvas.move(id3, 1 + 100, 400)
canvas.move(id2, 1 + 100, 450)
canvas.move(id1, 1 + 100, 500)

canvas.move(texto13, 106 + 100, 305)
canvas.move(texto12, 106 + 100, 355)
canvas.move(texto11, 7 + 100, 5)
canvas.move(texto10, 7 + 100, 55)
canvas.move(texto9, 7 + 100, 105)
canvas.move(texto8, 7 + 100, 155)
canvas.move(texto7, 7 + 100, 205)
canvas.move(texto6, 7 + 100, 255)
canvas.move(texto5, 7 + 100, 305)
canvas.move(texto4, 7 + 100, 355)
canvas.move(texto3, 7 + 100, 405)
canvas.move(texto2, 7 + 100, 455)
canvas.move(texto1, 7 + 100, 505)

canvas.move(idMa, 10, 155, )
canvas.move(textoMa, 16, 160)

canvas.move(idSe, 10, 205)
canvas.move(textoSe, 16, 210)

canvas.move(idAm, 10, 255)
canvas.move(textoAm, 16, 260)

canvas.move(idPer, 10, 305)
canvas.move(textoPer, 16, 310)

canvas.move(idPud, 10, 355)
canvas.move(textoPud, 16, 360)

canvas.move(idGermen, 1 + 400, 0)
canvas.move(idFitoto, 1 + 400, 50)
canvas.move(idPudri, 1 + 400, 100)
canvas.move(idGlome, 1 + 400, 200)
canvas.move(idPestalo, 1 + 400, 250)
canvas.move(idBotryodil, 1 + 400, 300)
canvas.move(idMelan, 1 + 400, 350)
canvas.move(idCurvala, 1 + 400, 400)
canvas.move(idMarcPro, 1 + 400, 450)
canvas.move(idMarcLet, 1 + 400, 500)

canvas.move(textoGerme, 7 + 400, 0)
canvas.move(textoFitoto, 7 + 400, 55)
canvas.move(textoPudri, 7 + 400, 105)
canvas.move(textoGlome, 7 + 400, 205)
canvas.move(textoPestalo, 7 + 400, 255)
canvas.move(textoBotryodil, 7 + 400, 305)
canvas.move(textoMelan, 7 + 400, 355)
canvas.move(textoCurvala, 7 + 400, 405)
canvas.move(textoMarcPro, 7 + 400, 455)
canvas.move(textoMarcLet, 7 + 400, 505)




def crearMapa():


    global id13
    global id12
    global id11
    global id10
    global id9
    global id8
    global id7
    global id6
    global id5
    global id4
    global id3
    global id2
    global id1

    global texto13
    global texto12
    global texto11
    global texto10
    global texto9
    global texto8
    global texto7
    global texto6
    global texto5
    global texto4
    global texto3
    global texto2
    global texto1

    global idMa
    global idSe
    global idAm
    global idPer
    global idPud

    global textoMa
    global textoSe
    global textoAm
    global textoPer
    global textoPud

    global idGermen
    global idFitoto
    global idPudri
    global idGlome
    global idPestalo
    global idBotryodil
    global idMelan
    global idCurvala
    global idMarcPro
    global idMarcLet



    global textoGerme
    global textoFitoto
    global textoPudri
    global textoGlome
    global textoPestalo
    global textoBotryodil
    global textoMelan
    global textoCurvala
    global textoMarcPro
    global textoMarcLet

    canvas.itemconfig(id13,fill="white")
    canvas.itemconfig(id12, fill="white")
    canvas.itemconfig(id11,fill="white")
    canvas.itemconfig(id10, fill="white")
    canvas.itemconfig(id9, fill="white")
    canvas.itemconfig(id8, fill="white")
    canvas.itemconfig(id7, fill="white")
    canvas.itemconfig(id6, fill="white")
    canvas.itemconfig(id5, fill="white")
    canvas.itemconfig(id4, fill="white")
    canvas.itemconfig(id3, fill="white")
    canvas.itemconfig(id2, fill="white")
    canvas.itemconfig(id1, fill="white")
    canvas.itemconfig(idMa, fill="white")
    canvas.itemconfig(idSe, fill="white")
    canvas.itemconfig(idPud, fill="white")
    canvas.itemconfig(idAm, fill="white")
    canvas.itemconfig(idPer, fill="white")
    canvas.itemconfig(idGermen, fill="white")
    canvas.itemconfig(idFitoto,fill="white")
    canvas.itemconfig(idPudri, fill="white")
    canvas.itemconfig(idGlome, fill="white")
    canvas.itemconfig(idPestalo, fill="white")
    canvas.itemconfig(idBotryodil, fill="white")
    canvas.itemconfig(idMelan, fill="white")
    canvas.itemconfig(idCurvala, fill="white")
    canvas.itemconfig(idMarcPro, fill="white")
    canvas.itemconfig(idMarcLet, fill="white")






def investigar():
    crearMapa()

    global id13
    global id12
    global id11
    global id10
    global id9
    global id8
    global id7
    global id6
    global id5
    global id4
    global id3
    global id2
    global id1



    global idMa
    global idSe
    global idAm
    global idPer
    global idPud



    global idGermen
    global idFitoto
    global idPudri
    global idGlome
    global idPestalo
    global idBotryodil
    global idMelan
    global idCurvala
    global idMarcPro
    global idMarcLet


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
    print(checkMohoVerAzu.get())
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
    global checkParcheGris
    global LabelTratamiento

    if checkMarron.get()==True:
        canvas.itemconfig(idMa,fill="yellow")

        if checkMohoVerAzu.get()==True:
            canvas.itemconfig(id11,fill="yellow")
            print("como vamos")

            LabelEnfermedad.config(text="La enfermedad es: Germen marrón")
            LabelEnfermedad.place(x=600,y=25)
            LabelTratamiento.config(text="El germen marrón se previene manteniendo el contenido de humedad de la semilla por debajo del 19%, durante el período de calentamiento. "
                                         "\n Se recomienda el tratamiento de la semilla con una mezcla fungicida-bactericida (Thi- ram más Estreptomicina")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idGermen,fill="yellow")

        elif checkSemillasHinchadas.get()==True:

            canvas.itemconfig(id10, fill="yellow")
            LabelEnfermedad.config(text="La enfermedad es: Fitotoxicidad por pesticidas")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="Se recomienta que, en casos tempranos dejar de usar el pesticida usado del momento, y cambiar por uno con menos nivel de acidez")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idFitoto,fill="yellow")

        elif checkParchesBlancos.get() == True or chcekAbanicos.get()==True:

            if checkParchesBlancos.get()==True:

                canvas.itemconfig(id9, fill="yellow")

            if chcekAbanicos.get()==True:

                canvas.itemconfig(id8,fill="yellow")

            LabelEnfermedad.config(text="La enfermedad es: Pudrición de la semilla")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="La enfermedad usualmente se desarrolla por no limpiar la semilla de pulpa infectada, se recomienda usar sustancias protectoras antes de plantarla")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idPudri,fill="yellow")


    if checkMarron.get()==True or checkSecamiento.get()==True:

        if checkMarron.get()==True:

            canvas.itemconfig(idMa, fill="yellow")

        if checkSecamiento.get()==True:

            canvas.itemconfig(idSe,fill="yellow")



        if checkPuntitos.get()==True or checkBordeAmarillo.get()==True:

            if checkPuntitos.get()==True:
                canvas.itemconfig(id5,fill="yellow")

            if checkBordeAmarillo.get()==True:
                canvas.itemconfig(id4,fill="yellow")



            if checkCentroGris.get()==True:

                canvas.itemconfig(id13,fill="yellow")


                LabelEnfermedad.config(text="La enfermedad es: Botryodiplodia")

                LabelEnfermedad.place(x=600, y=25)
                LabelTratamiento.config(
                    text="Cuando el hongo se localiza, lo mejor es limpiar la zona y apartar futuras plantas de la zona afectada, para evitar su reproduccion."
                         "\nPara luego usar sustancias de acidez controlable sobre la palama afectada y limpiar el hongo")
                LabelTratamiento.place(x=600, y=50)
                canvas.itemconfig(idBotryodil,fill="yellow")

            elif checkAreaGris.get()==True:

                canvas.itemconfig(id12, fill="yellow")

                LabelEnfermedad.config(text="La enfermedad es: Melanconim")
                LabelEnfermedad.place(x=600, y=25)
                LabelTratamiento.config(
                    text="Generalmente el ataque de estos hongos es favorecido por humedad ambiental alta y deficiencias en la fertilización. "
                         "\nEl espaciamiento adecuado de las plantitas, la fertilización balanceada y la regulación del riego y del sombrío."
                         "\nDisminuye la incidencia de las manchas foliares. Se recomienda la erradicación de hojas afectadas y aspersiones con fungicidas como Ziram"
                         "\no Captan al 2°/o")
                LabelTratamiento.place(x=600, y=50)
                canvas.itemconfig(idMelan,fill="yellow")

        elif checkAmarilloTranslucido.get()==True:

            canvas.itemconfig(id7, fill="yellow")
            LabelEnfermedad.config(text="La enfermedad es: Glomerella cingulata")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="Generalmente el ataque de estos hongos es favorecido por humedad ambiental alta y deficiencias en la fertilización. "
                     "\nEl espaciamiento adecuado de las plantitas, la fertilización balanceada y la regulación del riego y del sombrío."
                     "\nDisminuye la incidencia de las manchas foliares. Se recomienda la erradicación de hojas afectadas y aspersiones con fungicidas como Ziram"
                     "\no Captan al 2°/o")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idGlome,fill="yellow")

        elif checkParcheGris.get()==True:

            canvas.itemconfig(id6, fill="yellow")
            LabelEnfermedad.config(text="La enfermedad es: Pestolatia")
            LabelEnfermedad.place(x=600,y=25)
            LabelTratamiento.config(text="generalmente se presenta en palmitas debilitadas por alguna condición anormal de carácter nutricional"
                                        "\n o de déficit hídrico, como la deficiencia de magnesio y períodos prolongados de sequía."
                                        "\n Lo mejor es mantener una rutina de hidratacion constate y suplementos en control para la palma")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idPestalo,fill="yellow")

    if checkAmarillo.get()==True or checkSecamiento.get()==True:

        if checkAmarillo.get()==True:
            canvas.itemconfig(idAm, fill="yellow")

        if checkSecamiento.get()==True:
            canvas.itemconfig(idSe,fill="yellow")

        if checkBordeAmarillo.get()==True or checkAnillosgrises.get()==True:

            if checkBordeAmarillo.get()==True:

                canvas.itemconfig(id4,fill="yellow")

            if checkAnillosgrises.get()==True:

                canvas.itemconfig(id3,fill="yellow")


            LabelEnfermedad.config(text="La enfermedad es: Curvalaria masculans")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="verde. En algunos casos, la fertilización excesiva con nitrógeno o potasio, induce la deficiencia de magnesio, debido"
                     "\na efectos antagónicos. Generalmente se emplea sulfato de magnesio como correctivo: un cuarto de onza por palma hasta "
                     "\nlos ocho meses y media onza a mayor edad. También puede aplicarse este producto en aspersión, en solución al 2 % "
                     "\na intervalos de 3-4 días, durante 2-3 semanas.")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(idCurvala,fill="yellow")

    if checkPudricion.get()==True or checkPerdidaBrillo.get()==True:


        if checkPerdidaBrillo.get()==True:
            canvas.itemconfig(idPer,fill="yellow")

        if checkPudricion.get()==True:
            canvas.itemconfig(idPud,fill="yellow")

        if checkFolioCafe.get()==True:

            LabelEnfermedad.config(text="La enfermedad es: Marchitez sorpresiva")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="se realizan campañas de identificación temprana de las palmas enfermas y se procede a su rápida erradicación, complementada"
                     "\ncon el manejo adecuado de las gramíneas presentes en los lotes afectados y la aplicación de insecticidas en el área "
                     "\npara reducir la población de los insectos que pueden estar involucrados en su diseminación, en una forma similar a la recomendado"
                     "\npara el control de la Marchitez letal")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(id2,fill="yellow")

        elif checkBronce.get()==True:

            LabelEnfermedad.config(text="La enfermedad es: Marchites Letal")
            LabelEnfermedad.place(x=600, y=25)
            LabelTratamiento.config(
                text="la enfermedad se está controlando con una detección temprana de los síntomas y la erradicación de las palmas enferma")
            LabelTratamiento.place(x=600, y=50)
            canvas.itemconfig(id1,fill="yellow")



master.geometry("1380x980")
LabelElegir=tk.Label(master,text="Eliga los sintomas que correspondan al estado acutal de su palma: ")

LabelManchas=tk.Label(master,text="Color de maanchas pronunciadas generales: ")
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
checkparaParchesCeniza=ttk.Checkbutton(master , text="Parches gris ceniza",variable=checkParcheGris,onvalue=True,offvalue=False)

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

LabelLista=tk.Label(master,text="BASE DE HECHOS (Rojo): "
                                "\n -Manchas Marrones (Ma)"
                                "\n -Secamiento de la superficie de la hoja (SE)"
                                "\n -Manchas de color amarillo"
                                "\n -Perdida de brillo de los frutos"
                                "\n -Pudricoon de las racies"
                                "\n -SINTOMAS (Negro): "
                                "\n -1 Decoloracion bronce de los folios"
                                "\n -2 Decoloracion cafe de los folios"
                                "\n -3 Amillos de color gris"
                                "\n -4 Bordes de hoja amarillo"
                                "\n -5 Puntitos negros"
                                "\n -6 Parches gris ceniza"
                                "\n -7 Bordes de hoja amarillo "
                                "\n -8 Abanicos gris blanco"
                                "\n -9 Parches blancos"
                                "\n -10 Semillas hinchadas"
                                "\n -11 Moho Verde/azul"
                                "\n -12 Areas de color gris"
                                "\n -13 Centro color gris"
                                "\n ENFERMEDADES(verder):"
                                "\n -Germen marron (Ger)"
                                "\n -Fitotoxicidad por pesticidads (Fit)"
                                "\n -Pudricion de la semilla (Pud)"
                                "\n -Glomerella cingulata (Glo)" 
                                "\n -Pestalotia (Pes)"
                                "\n -Botryodilopia (Bot)"
                                "\n -Melanconim (Mel)"
                                "\n -Curvalaria masculans (Cur)"
                                "\n -Marchites sorpresiva (MaP)"
                                "\n -Marchites Letal (MaL)")


LabelEnfermedad=tk.Label(master,text="")
LabelTratamiento=tk.Label(master,text="")



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
checkparaParchesCeniza.place(x=0,y=245)

LabelLista.place(x=0,y=350)

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




canvas.place(x=500,y=400)

tk.mainloop()