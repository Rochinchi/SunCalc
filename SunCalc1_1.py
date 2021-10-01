# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:48:50 2021

@author: nicol
"""

import tkinter
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image

def cerrar():
    ventana.quit()
    ventana.destroy()

def calculos():
    V1 = float(T1.get())
    V2 = float(T2.get())
    rest = V1*V2
    var.set(str(rest))

ventana = tkinter.Tk()
ventana.wm_title("SunCalc")
ventana.geometry('1080x580')
ventana.configure(background='purple')
var = tkinter.StringVar()

#Primer letrero
E1 = tkinter.Label(ventana, text='Primer valor', bg='black', fg='white',
                   font=('Verdana',20))
E1.grid(row=0,column=0,sticky="w", padx=10, pady=10)

#Primer texto
T1 = tkinter.Entry(ventana, width=50)
T1.grid(row=0,column=1,sticky="w", padx=10, pady=10)

#2 letrero
E2 = tkinter.Label(ventana, text='Primer valor', bg='black', fg='white',
                   font=('Verdana',20))
E2.grid(row=1,column=0,sticky="w", padx=10, pady=10)

#2 texto
T2 = tkinter.Entry(ventana, width=50)
T2.grid(row=1,column=1,sticky="w", padx=10, pady=10)

#Boton 1
B1 = tkinter.Button(ventana, text='Calcular', command=calculos)
B1.grid(row=2, column=0, sticky="w", padx=10, pady=10)

#Boton cerrar
B2 = tkinter.Button(ventana, text='Salir', command=cerrar)
B2.grid(row=2, column=1, sticky="w", padx=10, pady=10)

#resultados
ER = tkinter.Label(ventana, textvariable=(var), bg='black', fg='white',
                   font=('Verdana',20))
ER.grid(row=3, column=1, sticky="w", padx=10, pady=10)

#Foto
#Imagen = tkinter.PhotoImage(file='paneles.gif')
#imag = ttk.Label(ventana, image=Imagen)
#imag.grid(row=3, column=0, sticky="w", padx=5, pady=5)

tkinter.mainloop()
