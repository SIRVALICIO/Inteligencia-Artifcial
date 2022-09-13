import tkinter as tk
import tkinter.messagebox
from tkinter import ttk



master=tk.Tk()
checkMa=tk.BooleanVar()
checkBro=tk.BooleanVar()
checkMohoVerAzu=tk.BooleanVar()



master.geometry("1380x980")
LabelColorHoja=tk.Label(master,text="Eliga un color de hoja ")
checkparaMarron= ttk.Checkbutton(master , text="Marron",variable=checkMa,onvalue=True,offvalue=False)
checkparaBronce= ttk.Checkbutton(master , text="Bronce",variable=checkBro,onvalue=True,offvalue=False)
checkparaMohoVerAzu= ttk.Checkbutton(master , text="Bronce",variable=checkMohoVerAzu,onvalue=True,offvalue=False)
LabelColorHoja.place(x=0, y=50)
checkparaMarron.place(x=0, y=70)
checkparaBronce.place(x=0, y=90)

tk.mainloop()