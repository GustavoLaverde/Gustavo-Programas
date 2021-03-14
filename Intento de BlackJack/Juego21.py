import time 
import random
from tkinter import*
from tkinter import messagebox
##___________________________________________________________________________________________________##
##__________________________________________GRANDES RASGOS___________________________________________##
root = Tk()
root.title("BLACKJACK")
root.geometry("500x330") ## Dandole las dimensiones a la ventana
root.iconbitmap("carta.ico")
root.resizable(0,0)
root.config(background="skyblue")
imagen1 = PhotoImage(file="plantarse.png")
imagen2 = PhotoImage(file="pedir.png")
imagen3 = PhotoImage(file="comenzar.png")
frame3=Frame(root)
frame3.place(x=260,y=310)
copyright_XD=Label(frame3)
copyright_XD.pack()
copyright_XD.config(text="Proyecto realizado por Gustavo Laverde",font="Arial 10",background="skyblue")
##___________________________________________________________________________________________________##
##_______________________________________CREACION DE LA BARAJA_______________________________________##
palos= ["\u2660","\u2665","\u2666","\u2663"]
tantos=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
mazo= []
diccionario = {}
i=1

for t in tantos:
    for p in palos:
        carta = "{}{}".format(t,p)
        mazo.append(carta)
        diccionario["{}{}".format(t,p)]=i
    i=i+1
for j in range(36,52,1):
    diccionario[mazo[j]]=10
#print(diccionario)
#print(mazo.index("9\u2663"))
random.shuffle( mazo )
#print(mazo)
#print( mazobarajeado)
##___________________________________________________________________________________________________##
##_________________________________DECLARACION DE VARIABLES Y DEMAS__________________________________##
comenzado = False
index_mazo = 3
a = 190
b = 100
frame=Frame(root)
frame.place(x=50,y=270)
frame1=Frame(root)
frame1.place(x=50,y=100)
suma=Label(frame)
suma.pack()
suma1=Label(frame1)
suma1.pack()
suma.config(text="Suma:",font="Arial 12",background="skyblue")
suma1.config(text="Suma:",font="Arial 12",background="skyblue")
total = 0
totalcrupier = 0
##___________________________________________________________________________________________________##
##______________________________________CREACION DE FUNCIONES________________________________________##
def COMENZAR():
    mazo_barajeado=mazo
    global comenzado 
    global total
    global totalcrupier
    comenzado = True
    #print(mazo_barajeado)
    #print(mazo_barajeado[0])
    total = diccionario[mazo_barajeado[0]]+diccionario[mazo_barajeado[1]]
    totalcrupier = diccionario[mazo_barajeado[2]]
    num1=   Label(root, text=mazo_barajeado[0],font="Arial 40",bg="white").place(x=10,y=200)
    num2=   Label(root, text=mazo_barajeado[1],font="Arial 40").place(x=100,y=200)
    num11=  Label(root, text=mazo_barajeado[2],font="Arial 40").place(x=10,y=20)
    suma.config(text="Suma:{}".format(total),font="Arial 12",background="skyblue")
    suma1.config(text="Suma:{}".format(totalcrupier),font="Arial 12",background="skyblue")

def PEDIR():
    mazo_barajeado=mazo
    global index_mazo
    global total
    global a
    global comenzado
    if comenzado == True:
        total = total + diccionario[mazo_barajeado[index_mazo]]
        num3=   Label(root, text=mazo_barajeado[index_mazo],font="Arial 40").place(x=a,y=200)
        index_mazo=index_mazo+1
        suma.config(text="Suma:{}".format(total),font="Arial 12")
        a=a+90
        if total > 21 :
            messagebox.showinfo("PERDISTE","Usted se paso de 21")
            root.destroy()

def PLANTARSE():
    mazo_barajeado=mazo
    global index_mazo
    global totalcrupier
    global b
    global total
    if comenzado == True:
        comenzado == False
        while totalcrupier <= 16:
            num33=   Label(root, text=mazo_barajeado[index_mazo],font="Arial 40").place(x=b,y=20)
            totalcrupier = totalcrupier + diccionario[mazo_barajeado[index_mazo]]
            suma1.config(text="Suma:{}".format(totalcrupier),font="Arial 12",background="skyblue")
            index_mazo = index_mazo +1
            b =b +90
        if totalcrupier > 21:
            messagebox.showinfo("GANASTE","El cuprier se paso de 21")
            root.destroy()
        else: 
            juegocrupier = 21 - totalcrupier
            mijuego = 21 - total
            if mijuego < juegocrupier:
                messagebox.showinfo("GANASTE","¡¡GANASTE EL JUEGO!!")
                root.destroy()
            else:
                if mijuego == juegocrupier :
                    messagebox.showinfo("EMPATE","Ambos juegos son iguales")
                    root.destroy()
                else:
                    messagebox.showinfo("PERDISTE","El juego del cuprier es mejor")
                    root.destroy()
##___________________________________________________________________________________________________##
##__________________________________CREACION DE BOTONES E INTERFAZ___________________________________##
comenzar = Button(root,image=imagen3,bd=3,cursor="hand2",command=COMENZAR).place(x=10,y=142,width=100,height=30)
plantarse = Button(root,image=imagen1,bd=3,cursor="hand2",command=PLANTARSE).place(x=390,y=142,width=100,height=30)
pedir = Button(root,image=imagen2,bd=3,cursor="hand2",command=PEDIR).place(x=200,y=142,width=60,height=30)
##___________________________________________________________________________________________________##
##___________________________________________________________________________________________________##
root.mainloop() 