from tkinter import*
from math import*
import tkinter
from tkinter import messagebox
from tkinter import ttk

##____________________________________________________ASPECTO EXTERNO____________________________________________________##
root = tkinter.Tk()
root.title("solucion de Triangulos")
root.geometry("305x450") ## Dandole las dimensiones a la ventana
root.iconbitmap("triangulo.ico")
root.resizable(0,0)

nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

p0 = ttk.Frame(nb)
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)

nb.add(p0,text='ventana1')
nb.add(p1,text='AAL',state="hidden")
nb.add(p2,text='LLA',state="hidden")

imagen1 = PhotoImage(file="triangulo.png")
imagen2 = PhotoImage(file="logo.png")
Triangulo = Label(p1,image=imagen1).place(x=0, y=5)
Triangulo2 = Label(p2,image=imagen1).place(x=0, y=5)

frame3=Frame(p0)
frame3.place(x=35,y=405)
copyright_XD=Label(frame3)
copyright_XD.pack()
copyright_XD.config(text="Proyecto realizado por Gustavo Laverde",font="Arial 10")
##____________________________________________________ASPECTO EXTERNO____________________________________________________##
##_________________________________________________INTERFAZ DE COMIENZO__________________________________________________##

def  pesta1():
    nb.select(p1)
def  pesta2():
    nb.select(p2)

escrito1 = Label(p0, text = "Datos:\n2 Angulos y 1 Lado",font="Arial 20").place(x=30,y=20)
escrito2 = Label(p0, text = "Datos:\n2 Lados y 1 Angulo",font="Arial 20").place(x=30,y=220)

botonLLA = Button(p0, text="CASO 1",command=pesta1,bd=3,cursor="hand2").place(x=100,y=90,width=100,height=100)
botonLLA = Button(p0, text="CASO 2",command=pesta2,bd=3,cursor="hand2").place(x=100,y=290,width=100,height=100)

##_________________________________________________INTERFAZ DE COMIENZO__________________________________________________##
##________________________________________________CALCULADORA DE ANGULOS_________________________________________________##
anguloA=StringVar()
anguloB=StringVar()
anguloC=StringVar()

"""def calculoangulos():
    C=180- float(anguloA.get()) - float(anguloB.get())
    ##print("{:.2f}".format(C))
    anguloC.set("{:.2f}".format(C))"""

anguloA.set("0.00")
anguloB.set("0.00")
anguloC.set("0.00")

AnguloA = Label(p1, text="Angulo A: ",font="Arial 10").place(x=50,y=170)
entradaA = Entry(p1, textvariable=anguloA,font="Arial 10").place(x=120,y=170,width=75)

AnugloB = Label(p1, text="Angulo B: ",font="Arial 10").place(x=50,y=200)
entradaB = Entry(p1, textvariable=anguloB,font="Arial 10").place(x=120,y=200,width=75)

AnugloC = Label(p1, text="Angulo C: ",font="Arial 10").place(x=50,y=230)
entradaC = Entry(p1, textvariable=anguloC,state="disable",font="Arial 10").place(x=120,y=230,width=75)

##boton = Button(p1, text="Calcular",command=calculoangulos,bd=3).place(x=250,y=170,width=100,height=80)

##_________________________________________________CALCULADORA DE ANGULOS_________________________________________________##
##_________________________________________________CALCULADORA DE LADOS_________________________________________________##
lado=StringVar()
lado1=StringVar()
lado2=StringVar()
opuesto=StringVar()
lado.set("00")
lado1.set("00")
lado2.set("00")
etiqueta1=""
etiqueta2=""

ang=0.00
k=0.00
#frame = Frame(p1).place(x=70,y=420)

frame=Frame(p1)
frame.place(x=50,y=420)
nota=Label(frame)
nota.pack()

def calculolados():
    
    C=180- float(anguloA.get()) - float(anguloB.get())
    ##print("{:.2f}".format(C))

    global etiqueta1
    global etiqueta2
    nota.config(text="")
    #nota= Label(p1, text="                                                ",font="Arial 10").place(x=70,y=420)
    if float(anguloA.get()) == 0 or float(anguloB.get()) == 0 or float(lado.get())==0 or C <= 0 :
        ##nota.config(text="INTRODUCIR VALORES COHERENTES")
        messagebox.showwarning("Error","Introducir valores coherentes")

        #nota= Label(p1, text="Introducir valores coherentes",font="Arial 10").place(x=70,y=420)

    else:
        anguloC.set("{:.2f}".format(C))

        if opuesto.get() == "A":
            etiqueta1="Lado B"
            etiqueta2="lado C"
            ang=(float(anguloA.get())*pi)/180
            ang1=(float(anguloB.get())*pi)/180
            ang2=(float(anguloC.get())*pi)/180
            k=float(lado.get())/sin(ang)
            lado1.set("{:.2f}".format(k*sin(ang1)))
            lado2.set("{:.2f}".format(k*sin(ang2)))

        if opuesto.get() == "B":
            etiqueta1="Lado A"
            etiqueta2="lado C"
            ang=(float(anguloB.get())*pi)/180
            ang1=(float(anguloA.get())*pi)/180
            ang2=(float(anguloC.get())*pi)/180
            k=float(lado.get())/sin(ang)
            lado1.set("{:.2f}".format(k*sin(ang1)))
            lado2.set("{:.2f}".format(k*sin(ang2)))

        if opuesto.get() == "C":
            etiqueta1="Lado A"
            etiqueta2="lado B"
            ang=(float(anguloC.get())*pi)/180
            ang1=(float(anguloA.get())*pi)/180
            ang2=(float(anguloB.get())*pi)/180
            k=float(lado.get())/sin(ang)
            lado1.set("{:.2f}".format(k*sin(ang1)))
            lado2.set("{:.2f}".format(k*sin(ang2)))
        
        Lado1 = Label(p1, text=etiqueta1,font="Arial 10").place(x=50,y=290)
        entradal1 = Entry(p1, textvariable=lado1,state="disable",font="Arial 10").place(x=120,y=290,width=75)

        Lado2 = Label(p1, text=etiqueta2,font="Arial 10").place(x=50,y=320)
        entradal2 = Entry(p1, textvariable=lado2,state="disable",font="Arial 10").place(x=120,y=320,width=75)

Lado= Label(p1, text="Lado: ",font="Arial 10").place(x=50,y=260)
entradaLado = Entry(p1, textvariable=lado,font="Arial 10").place(x=148,y=260,width=45)

##Opuesto_a= Label(p1, text="Opuesto a: ",font="Arial 10").place(x=50,y=290)
lados=Spinbox(p1,values=("A","B","C"),wrap=True,textvariable=opuesto,state='readonly',font="Arial 10").place(x=120,y=260,width=25)

boton = Button(p1, text="Calcular",command=calculolados,bd=3,image=imagen2,cursor="hand2").place(x=100,y=380,width=100,height=30)

##_________________________________________________CALCULADORA DE LADOS_________________________________________________##
##____________________________________________________CASO DE LADOS_____________________________________________________##
angO=StringVar()
ladoA=StringVar()
ladoB=StringVar()
ladoC=StringVar()
ang1=StringVar()
ang2=StringVar()
opuestoang=StringVar()

ladoC.set("00")
ladoA.set("00")
ladoB.set("00")
ang1.set("0.00")
ang2.set("0.00")
angO.set("00")
etiquetaang1=""
etiquetaang2=""


def calculolados2():
    global etiquetaang1
    global etiquetaang2

    if float(ladoA.get()) == 0 or float(ladoB.get()) == 0 or float(angO.get())==0  :
        messagebox.showwarning("Error","Introducir valores coherentes")

    else:
        if opuestoang.get() == "A":
            etiquetaang1 = "Anuglo B:"
            etiquetaang2 = "Anuglo C:"
            angOflotante = (float(angO.get())*pi)/180
            k=float(ladoA.get())/sin(angOflotante)
            aux = (float(ladoB.get())/k)
            k1 = asin(aux)
            ang1.set("{:.2f}".format((k1*180)/pi))
            k2 = 180 - float(angO.get())- float(ang1.get())
            ang2.set("{:.2f}".format(k2))
            ladc = k*sin((float(ang2.get())*pi)/180)
            ladoC.set("{:.2f}".format(ladc))

        if opuestoang.get() == "B":
            etiquetaang1 = "Anuglo A:"
            etiquetaang2 = "Anuglo C:"
            angOflotante = (float(angO.get())*pi)/180
            k=float(ladoB.get())/sin(angOflotante)
            aux = (float(ladoA.get())/k)
            k1 = asin(aux)
            ang1.set("{:.2f}".format((k1*180)/pi))
            k2 = 180 - float(angO.get())- float(ang1.get())
            ang2.set("{:.2f}".format(k2))
            ladc = k*sin((float(ang2.get())*pi)/180)
            ladoC.set("{:.2f}".format(ladc))

        if opuestoang.get() == "C":
            etiquetaang1 = "Anuglo A:"
            etiquetaang2 = "Anuglo B:"
            angOflotante = (float(angO.get())*pi)/180
            a=pow(float(ladoA.get()),2)+pow(float(ladoB.get()),2)-(2*float(ladoA.get())*float(ladoB.get())*cos(angOflotante))
            ladc= sqrt(a)
            ladoC.set("{:.2f}".format(ladc))
            k=float(ladoC.get())/sin(angOflotante)
            aux11 = (float(ladoA.get())/k)
            k1 = asin(aux11)
            aux22 = (float(ladoB.get())/k)
            k2 = asin(aux22)
            ang1.set("{:.2f}".format((k1*180)/pi))
            ang2.set("{:.2f}".format((k2*180)/pi))

        LadoC = Label(p2, text="Lado C:",font="Arial 10").place(x=50,y=260)
        entradalLadoC = Entry(p2, textvariable=ladoC,font="Arial 10",state="disable").place(x=120,y=260,width=75)

        Anguloop1 = Label(p2, text=etiquetaang1,font="Arial 10").place(x=50,y=290)
        entradalanguloop1 = Entry(p2, textvariable=ang1,font="Arial 10",state="disable").place(x=120,y=290,width=75)

        Anguloop2 = Label(p2, text=etiquetaang2,font="Arial 10").place(x=50,y=320)
        entradalanguloop2 = Entry(p2, textvariable=ang2,font="Arial 10",state="disable").place(x=120,y=320,width=75)

LadoA = Label(p2, text="Lado A: ",font="Arial 10").place(x=50,y=170)
entradaLadoA = Entry(p2, textvariable=ladoA,font="Arial 10").place(x=120,y=170,width=75)

LadoB = Label(p2, text="Lado B: ",font="Arial 10").place(x=50,y=200)
entradaLadoB = Entry(p2, textvariable=ladoB,font="Arial 10").place(x=120,y=200,width=75)

anguloop = Label(p2, text="Angulo: ",font="Arial 10").place(x=50,y=230)
entradaanguloop = Entry(p2, textvariable=angO,font="Arial 10").place(x=148,y=230,width=45)
anguloopuesto=Spinbox(p2,values=("A","B","C"),wrap=True,textvariable=opuestoang,state='readonly',font="Arial 10").place(x=120,y=230,width=25)

boton = Button(p2, text="Calcular",command=calculolados2,bd=3,image=imagen2,cursor="hand2").place(x=100,y=380,width=100,height=30)

##____________________________________________________CASO DE LADOS_____________________________________________________##

root.mainloop() 