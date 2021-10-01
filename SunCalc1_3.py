# -*- coding: utf-8 -*-
"""

@author: Rocha y Pineda
"""

import tkinter
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image

def cerrar():
    ventana.quit()
    ventana.destroy()

def calculos():
    hsp = callback()
    pn = 300
    pr = 0.9
    lmd = float(T1.get())*1000*1.2 #Consumo energetico diario + 20%
    NumPaneles = round(lmd/(hsp*pn*pr), 0)
    ER.configure(text= "El número de paneles para abastecer \n el inmueble es de: " + str(NumPaneles)+ " paneles")
    panel = tkinter.PhotoImage(file="paneles.gif")
    panel = panel.subsample(2)
    lpan = tkinter.Label(ventana, image=panel,bg='maroon4')
    lpan.grid(row=5,column=1, padx=5,pady=5)
    lpan.photo = panel

def callback(*args):
    if str(variable.get()) == "2-3 horas":
        hsp = 2.5
    elif str(variable.get()) == "3-4 horas":
        hsp = 3.5
    elif str(variable.get()) == "4-5 horas":
        hsp = 4.5
    elif str(variable.get()) == "6-7 horas":
        hsp = 6.5
    elif str(variable.get()) == "7-8 horas":
        hsp = 7.5
    else:
        hsp = 1
    return hsp




def map():
    mphsp = tkinter.PhotoImage(file="HSP.gif")
    mphsp=mphsp.subsample(1)
    em = tkinter.Toplevel(width=300, height=200)
    em.title("Mapa hora sol pico")
    lfoto = tkinter.Label(em,image=mphsp)
    lfoto.grid(row=0,column=0,sticky="w", padx=5,pady=5)
    lfoto.photo = mphsp

def help():
    hp = tkinter.Toplevel(width=300, height=200)
    hp.title("Ayuda")
    txt = """Hola amigo, bienvenido a SunCalc
    tu herramienta libre para cálculo de paneles solares
    Ten tu factura de la luz a la mano :D
    Para facilitar tus calculos tomamos los valores
    La bateria y el circuito abierto tendran valores nominales de 24V
    por ende se tomara un panel por rama, la cantidad de paneles que
    necesitas son la cantidad de paneles en paralelo
    La potencia nominal de los paneles es de 300W
    ---Esta es una versión de prueba---"""
    lfoto = tkinter.Label(hp,text = txt)
    lfoto.grid(row=0,column=0,sticky="w", padx=5,pady=5)

ventana = tkinter.Tk()
ventana.wm_title("SunCalc")
ventana.geometry('1080x580')
ventana.configure(background='maroon4')
var = tkinter.StringVar()

# Configuar indicie de la lista de opciones
OptionList = [
"2-3 horas",
"3-4 horas",
"4-5 horas",
"6-7 horas",
"7-8 horas"
]
variable = tkinter.StringVar(ventana)
variable.set(OptionList[0])

#Primer letrero
E1 = tkinter.Label(ventana, text='Gasto diario (KWh)', bg='maroon4',
                   fg='yellow green', font=('Comic Sans MS',22))
E1.grid(row=0,column=0,sticky="w", padx=10, pady=10)

#Primer texto
T1 = tkinter.Entry(ventana, width=50)
T1.grid(row=0,column=1,sticky="w", padx=10, pady=10)

#2 letrero
E2 = tkinter.Label(ventana, text='Hora sol pico',bg='maroon4', fg='yellow green',
                   font=('Comic Sans MS',22))
E2.grid(row=1,column=0,sticky="w", padx=10, pady=10)


#Boton 1
B1 = tkinter.Button(ventana, text='Calcular', command=calculos,bg='DeepPink4',fg='yellow green')
B1.grid(row=2, column=0, sticky="w", padx=10, pady=10)

#Boton cerrar
B2 = tkinter.Button(ventana, text='Salir', command=cerrar,bg='DeepPink4',fg='yellow green')
B2.grid(row=2, column=1, sticky="w", padx=10, pady=10)

#Boton mapa
B3 = tkinter.Button(ventana, text="?", command= map,bg='DeepPink4',fg='yellow green')
B3.grid(row=1,column=2, sticky="w", padx=10,pady=10)

#Boton ayuda
B4 = tkinter.Button(ventana, text="Ayuda", command= help,bg='DeepPink4',fg='yellow green')
B4.grid(row=12,column=0, sticky="w", padx=10,pady=10)



#resultados
ER = tkinter.Label(ventana, text="", bg='maroon4', fg='yellow green',
                   font=('Comic Sans MS',22))
ER.grid(row=3, column=1, sticky="w", padx=10, pady=10)

#Lista de hora sol pico

opt = tkinter.OptionMenu(ventana, variable, *OptionList)
opt.config(width=40, font=('Helvetica', 12),bg='DeepPink4',fg='yellow green')
opt["menu"].config(bg="DeepPink4",fg='yellow green')
opt.grid(row=1,column=1,sticky="w", padx=10, pady=10)
variable.trace("w",callback)


tkinter.mainloop()
