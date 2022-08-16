import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from scipy.stats import skew
from statistics import mode
from scipy.stats import kurtosis
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

from scipy import stats

archivo="abalone.csv"
datos=pd.read_csv(archivo)
datos.columns=["Sex","length","Diameter","Heigth","Whole Heigth","Shucked weight","Viscera weight","Shell weight","Rings"]


master=tk.Tk()
x=""
y=0
variable1=""
variable2=""
alpha=0


media=0
moda=0
mediana=0
asimetria=0
kurtosis=0
#checkT=tk.IntVar()
checkA=tk.IntVar()


atipicos=False


master.geometry("1380x980")




#def checkT(): if(checkT.get()==1):atipicos=False
def mostrarcheck():
    checkparaT.pack()

def ocultarcheck():
    checkparaT.pack_forget()

def mostrarList():
    listboxV.pack()
def ocultarList():
    listboxV.pack_forget()

def mostrarList2():
    listboxV2.pack()

def ocultarList2():
    listboxV2.pack_forget()


def mostrarLabelV1():
    LabelV1.pack()
def ocultarLabelv1():
    LabelV1.pack_forget()



def mostrarLabelV2():
    LabelV2.pack()
def ocultarLabelv2():
    LabelV2.pack_forget()

def ocultartext():
    textoVariable.pack_forget()
def mostartext():
    textoVariable.pack()

def mostrarGraficar():
    botonGrafico.pack()
def ocultarGraficar():
    botonGrafico.pack_forget()

def mostrarModa():
    LabelModa.config(text="La moda es: "+str(moda))
    LabelModa.pack()
def ocultarModa():
    LabelModa.pack_forget()

def mostrarMedia():
    LabelMedia.config(text="La media es: " + str(media))
    LabelMedia.pack()
def ocultarMedia():
    LabelMedia.pack_forget()

def mostrarMediana():
    LabelMediana.config(text="La mediana es: " + str(mediana))
    LabelMediana.pack()
def ocultarMediana():
    LabelMediana.pack_forget()

def mostrarAsimetria():
    LabelAsimetria.config(text="La Asimteria es: " + str(asimetria))
    LabelAsimetria.pack()
def ocultarAsimetria():
    LabelAsimetria.pack_forget()

def mostrarKurtosis():
    LabelKurtosis.config(text="La Kurtosis es: " + str(kurtosis))
    LabelKurtosis.pack()
def ocultarKurtosis():
    LabelKurtosis.pack_forget()

fig = Figure(figsize=(5, 5),
                 dpi=100)
canvas = FigureCanvasTkAgg(fig,
                               master=master)
def ocultartodo():
    ocultartext()
    ocultarcheck()
    ocultarLabelv2()
    ocultarList2()
    ocultarLabelv2()
    ocultarList()
    ocultarLabelv1()
    ocultarGraficar()
    ocultarAsimetria()
    ocultarMedia()
    ocultarKurtosis()
    ocultarMediana()
    ocultarModa()
    canvas.get_tk_widget().pack_forget()


def checkAT():
    global atipicos
    if(checkA.get()==1):
        ocultarGraficar()
        ocultarAsimetria()
        ocultarMedia()
        ocultarKurtosis()
        ocultarMediana()
        ocultarModa()

        atipicos=True
        mostartext()
        canvas.get_tk_widget().pack_forget()
        mostrarGraficar()
    elif(checkA.get()==0):
        atipicos=False
        ocultartext()
        ocultarGraficar()
        ocultarAsimetria()
        ocultarMedia()
        ocultarKurtosis()
        ocultarMediana()
        ocultarModa()
        canvas.get_tk_widget().pack_forget()
        mostrarGraficar()
    print(atipicos)


def eliminarAtipicos(Variable,alpha,DF):

    Data=DF
    Q1=np.percentile(Data[Variable], 25,
               method = 'midpoint')
    Q3=np.percentile(Data[Variable], 75,
               method = 'midpoint')
    IQR=Q3-Q1
    print(Data.shape)
    print("IQR",IQR)
    upper = np.where(DF[Variable] >= (Q3 + alpha * IQR))

    lower = np.where(DF[Variable] <= (Q1 - alpha * IQR))
    Data.drop(upper[0], inplace = True)
    Data.drop(lower[0], inplace = True)
    print(Data.shape)
    return Data

def graficar():
    global canvas
    global alpha
    global moda
    global media
    global mediana
    global asimetria
    global kurtosis


    copia = datos.copy()
    fig.clear()

    if(atipicos==True):
        print("vamos a eliminar")
        alpha=float(str(textoVariable.get(1.0, "end-1c")))
        copia = eliminarAtipicos(variable1, alpha, copia)
        if variable2!="":
            copia=eliminarAtipicos(variable2, alpha, copia)

    if(y==1):
        plot = fig.add_subplot(111)
        if(variable1==variable2):
            tkinter.messagebox.showinfo("Error al graficar","NO se puede hacer un diagrama con 2 variables iguales")

        else:

                try:
                    plot.scatter(copia[variable1], copia[variable2])

                    canvas.draw()


                except:
                    tkinter.messagebox.showinfo("Error al graficar",
                                                "NO se puede hacer un diagrama con 2 variables que no presentan la misma cantidad de densidad")



    elif(y==2):

            plot = fig.add_subplot(111)

            plot.hist(copia[variable1])


            canvas.draw()


    elif(y==3):

            plot = fig.add_subplot(111)

            stats.probplot(copia[variable1],dist=stats.norm, sparams=(6,),plot=plot)

            canvas.draw()



    elif(y==4):


            plot = fig.add_subplot(111)

            plot.boxplot(copia[variable1])

            canvas.draw()



            canvas.draw()
    moda = mode(copia[variable1])
    print(copia[variable1])
    mediana = copia[variable1].median()
    asimetria = copia[variable1].skew()
    media=copia[variable1].mean()
    kurtosis=copia[variable1].kurtosis()
    canvas.get_tk_widget().pack()

    mostrarModa()
    mostrarMedia()
    mostrarMediana()
    mostrarAsimetria()
    mostrarKurtosis()

LabelGrafica=tk.Label(master,text="Elige un tipo de grafica")


LabelModa=tk.Label(master,text="")
LabelMediana=tk.Label(master,text="")
LabelMedia=tk.Label(master,text="")
LabelAsimetria=tk.Label(master,text="")
LabelKurtosis=tk.Label(master,text="")


LabelGrafica.pack()

listaDeGraficos=tk.StringVar()

listboxTG=ttk.Combobox(master,
                     textvariable=listaDeGraficos,
                     height=6)
listboxTG["values"]=["Histograma","Cajas y vigotes","Normal","Dispercion"]
listboxTG["state"]="readonly"







listboxTG.pack()


textoVariable=tk.Text(master, height=1,
    width=8)


listaDevariables = tk.StringVar()
listboxV = ttk.Combobox(master,
                                 textvariable=listaDevariables,
                                 height=6)
listboxV["values"] = ["Sex","length","Diameter","Heigth","Whole Heigth","Shucked weight","Viscera weight","Shell weight","Rings"]
listboxV["state"] = "readonly"


listaDevariables2 = tk.StringVar()
listboxV2 = ttk.Combobox(master,
                                 textvariable=listaDevariables2,
                                 height=6)
listboxV2["values"] = ["Sex","length","Diameter","Heigth","Whole Heigth","Shucked weight","Viscera weight","Shell weight","Rings"]
listboxV2["state"] = "readonly"


LabelV1=tk.Label(master,text="Elige una variable")
LabelV2=tk.Label(master,text="Elige una segunda variable")

checkparaT= ttk.Checkbutton(master,text="Sin atipicos (Poner el valor de alpha)",command=checkAT,variable=checkA,onvalue=1,offvalue=0)


botonGrafico=tk.Button(master,text="Graficar",command=graficar)

def GraficoSeleccionado(event):
    global y
    x=listaDeGraficos.get()



    if x=="Dispercion":
        y=1
        print("llegue")

        ocultartodo()


        mostrarLabelV1()


        mostrarList()

        mostrarLabelV2()
        mostrarList2()
        mostrarcheck()
        mostrarGraficar()

    if x=="Histograma":
        y=2
        print("llegue")

        ocultartodo()



        mostrarLabelV1()


        mostrarList()
        mostrarcheck()
        mostrarGraficar()

    if x=="Normal":
        y=3
        print("llegue")
        ocultartodo()



        mostrarLabelV1()

        mostrarList()
        mostrarcheck()
        mostrarGraficar()

    if x == "Cajas y vigotes":
        y=4

        print("llegue")
        ocultartodo()




        mostrarLabelV1()


        mostrarList()
        mostrarcheck()
        mostrarGraficar()


def VariableSeleccionada1(event):
    global  variable1
    variable1=listboxV.get()
    print(variable1)


def VariableSeleccionada2(event):
    global variable2
    variable2 = listboxV2.get()
    print(variable2)


listboxTG.bind("<<ComboboxSelected>>",GraficoSeleccionado)
listboxV.bind("<<ComboboxSelected>>",VariableSeleccionada1)
listboxV2.bind("<<ComboboxSelected>>",VariableSeleccionada2)


#check=tk.Radiobutton(master,text="chechbutton",height=5,width=5,font=("Serif",6)) check.pack()
tk.mainloop()

#root=tk.Tk()

