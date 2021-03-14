from tkinter import*
from tkinter import messagebox


root = Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("800x615") ## Dandole las dimensiones a la ventana
root.iconbitmap("juego.ico")
root.resizable(0,0)

imagen1 = PhotoImage(file="piedra.png")
imagen2 = PhotoImage(file="papel.png")
imagen3 = PhotoImage(file="tijera.png")
imagen4 = PhotoImage(file="piedra2.png")
imagen5 = PhotoImage(file="papel2.png")
imagen6 = PhotoImage(file="tijera2.png")
imagen7 = PhotoImage(file="duelo.png")

frame=Frame(root)
frame.place(x=225,y=595,width=350)
frame2=Frame(root)
frame2.place(x=225,y=80,width=350)
copyright_XD=Label(frame)
copyright_XD.pack()
copyright_XD.config(text="Proyecto realizado por Gustavo Laverde",font="Arial 10")
reglas=Label(frame2)
reglas.pack()
reglas.config(text="REGLAS: Cada jugador eligira su movimiento\nsin que el otro vea, cuando los dos escojan\nsu movimiento deberan presionar VS",font="Arial 10")

jugadorOne = ""
jugadorOne_Listo = False
jugadorTwo = ""
jugadorTwo_Listo = False

def piedra():
    global jugadorOne
    global jugadorOne_Listo
    jugadorOne = "piedra"
    jugadorOne_Listo = True

def papel():
    global jugadorOne
    global jugadorOne_Listo
    jugadorOne = "papel"
    jugadorOne_Listo = True

def tijera():
    global jugadorOne
    global jugadorOne_Listo
    jugadorOne = "tijera"
    jugadorOne_Listo = True

def Piedra():
    global jugadorTwo
    global jugadorTwo_Listo
    jugadorTwo = "Piedra"
    jugadorTwo_Listo = True

def Papel():
    global jugadorTwo
    global jugadorTwo_Listo
    jugadorTwo = "Papel"
    jugadorTwo_Listo = True

def Tijera():
    global jugadorTwo
    global jugadorTwo_Listo
    jugadorTwo = "Tijera"
    jugadorOne_Listo = True

def duelo():
    if jugadorOne_Listo==True & jugadorTwo_Listo == True:
        if jugadorOne == "piedra":
            if jugadorTwo == "Piedra":
                messagebox.showinfo("Piedra, Papel o Tijera","Los jugadores han EMPATADO")
            elif jugadorTwo == "Papel":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 2 ha GANADO")
            elif jugadorTwo == "Tijera":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 1 ha GANADO")
        elif jugadorOne == "papel":
            if jugadorTwo == "Piedra":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 1 ha GANADO")
            elif jugadorTwo == "Papel":
                messagebox.showinfo("Piedra, Papel o Tijera","Los jugadores han EMPATADO")
            elif jugadorTwo == "Tijera":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 2 ha GANADO")
        elif jugadorOne == "tijera":
            if jugadorTwo == "Piedra":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 2 ha GANADO")
            elif jugadorTwo == "Papel":
                messagebox.showinfo("Piedra, Papel o Tijera","El jugador 1 ha GANADO")
            elif jugadorTwo == "Tijera":
                messagebox.showinfo("Piedra, Papel o Tijera","Los jugadores han EMPATADO")
    else:
        messagebox.showwarning("Piedra, Papel o Tijera","Elijan Por favor")

jugador1 = Label(root,text="JUGADOR 1",font="Arial 20").place(x=10,y=10)
piedra_boton = Button(root,image=imagen1,cursor="hand2",command=piedra).place(x=10,y=60)
papel_boton = Button(root,image=imagen2,cursor="hand2",command=papel).place(x=10,y=252)
tijera_boton = Button(root,image=imagen3,cursor="hand2",command=tijera).place(x=10,y=449)

jugador2 = Label(root,text="JUGADOR 2",font="Arial 20").place(x=630,y=10)
piedra_boton2 = Button(root,image=imagen4,cursor="hand2",command=Piedra).place(x=583,y=60)
papel_boton2 = Button(root,image=imagen5,cursor="hand2",command=Papel).place(x=583,y=252)
tijera_boton2 = Button(root,image=imagen6,cursor="hand2",command=Tijera).place(x=583,y=449)

Duelo_boton = Button(root,image=imagen7,bd=0,cursor="hand2",command=duelo).place(x=300,y=230)

root.mainloop() 