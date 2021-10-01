"""
Hola mundo en Tkinter

"""

#import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class Aplicacion():
    root = Tk()

    #root.geometry('300x200')
    root.title("Hola mundo")
    root.resizable(1,0)

    def Saludar():
        #Ventana emergente
        em = Toplevel(width=300, height=200)
        em.title("Que se dice")
        lbl3 = Label(em,text="Hola Juan Carlo, Cómo está chupapija")
        btn2 = Button(em, text="Adios", command= em.destroy, bg="lightblue")

        lbl3.grid(row=0,column=0,sticky="w", padx=5,pady=5)
        btn2.grid(row=1,column=0,sticky="w", padx=5,pady=5)

        #root.wait_window(em)
        #exit()

    frame = Frame(root, width=480, height=320)
    frame.pack()
    frame.config(cursor="pirate",bg="lightblue",bd=25,relief="sunken")
    #root.iconbitmap('hola.xbm')

    #Cambiar fuente
    #fuente = font.Font(weight = "bold")
    #Crear etiqueta
    lbl1 = Label(frame, text="Usuario: ")#, font = fuente)
    txt1 = Entry(frame)#, font = fuente)
    txt1.config(justify="center", state="normal")
    lbl2 = Label(frame, text="Contraseña: ")
    txt2 = Entry(frame, show= "*")
    btn1 = Button(frame, text="Saludar", command= Saludar, bg="lightgreen")
    imagen = PhotoImage(file="elbicho.gif")
    #posicionar etiqueta
    #lbl1.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
    lbl1.grid(row=0,column=0,sticky="w", padx=5,pady=5)
    txt1.grid(row=0,column=1,sticky="w", padx=5,pady=5)
    lbl2.grid(row=1,column=0,sticky="w", padx=5,pady=5)
    txt2.grid(row=1,column=1,sticky="w", padx=5,pady=5)
    btn1.grid(row=2,column=1,sticky="e", padx=5,pady=5)


    foto = PhotoImage(file="elbicho.gif")

    #foto=foto.zoom()
    foto=foto.subsample(3)
    label1 = Label(frame,image=foto)
    label1.grid(row=3,column=0,sticky="w", padx=5,pady=5)
    #image1 = Image.open("elbicho.gif")
    #test = ImageTk.PhotoImage(Image.open("elbicho.gif"))
    #label1 = Label(frame,image=test)
    #label1.grid(row=3,column=0,sticky="w", padx=5,pady=5)


    root.mainloop()



def main():
    screen = Aplicacion()
    return 0


if __name__ == "__main__":
    main()
