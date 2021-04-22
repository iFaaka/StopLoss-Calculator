from tkinter import Label, Button, Entry, Tk, StringVar
main = Tk()
main.title("Crypto helper")
main.geometry("600x400")

Precioini= StringVar() #https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=59&codigo=59&inicio=45
Porc__perd = StringVar()
Cant__lev = StringVar()


#Precio inicial
Label(main, text ="Ingrese el precio de la crypto: ", font=("Calibri", 17)).place(x=50,y=30)
Entry(main, font=("Arial", 10), textvariable=Precioini).place(x=350,y=35)

#Separador
Label(main, text ="-----------------------------------------------------------------------------------------------------------------",
font=("Calibri", 20)).place(x=10,y=80)


#Operacion

def Calcular():
    Valor1 = (float(Porc__perd.get()) / float(Cant__lev.get()) / 100 ) - 1
    ValorF = float(Valor1) * float(Precioini.get()) * -1
    etiqueta = Label(main, text = ValorF)
    etiqueta.place(x=330,y=230)   



#Boton Calcular
Boton = Button(main, text="Calcular",font=("Calibri", 14), command=Calcular)
Boton.place(x=230,y=290)


#Labels 

#Porcentaje que se espera ganar
Label(main, text ="¿Cuanto podes soportar para abajo?", font=("Calibri", 14)).place(x=10,y=130) #Texto %
Porcent_perd = Entry(main, font=("Arial", 10),textvariable=Porc__perd)
Porcent_perd.place(x=330,y=135) 


#Cantidad de leverage

Label(main, text ="¿Que leverage usas?", font=("Calibri", 14)).place(x=80,y=180) #Texto %
Cantidad_lev = Entry(main, font=("Arial", 10), textvariable=Cant__lev)
Cantidad_lev.place(x=330,y=185) #Cantidad de leverage



#Valor para alcanzar ganancia
Label(main, text ="El stop va en: ", font=("Calibri", 14)).place(x=80,y=230) #Texto %
Valor__gan = Label(main, text = "valor__fin", font=("Calibri",20))


#Extra
Label(main, text="Hecho con <3 por Faka", font=("Calibri",9)).place(x=460,y=375)
Label(main, text="v 0.1 ALPHA", font=("Calibri",9)).place(x=1,y=375)

main.mainloop()