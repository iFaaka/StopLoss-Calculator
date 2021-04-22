from tkinter import Label,Button,Entry,Tk, StringVar
longw = Tk()
longw.title("Crypto helper")
longw.resizable(width=False, height=False) #No se puede cambiar tamaño

#Variables

Precioini= StringVar() #https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=59&codigo=59&inicio=45
Porc__gan = StringVar()
Cant__lev = StringVar()




#Operacion



def Calcular():
    Valor1 = (float(Porc__gan.get()) / float(Cant__lev.get()) / 100 ) + 1
    ValorF = float(Valor1) * float(Precioini.get())
    etiqueta = Label(longw, text = ValorF)
    etiqueta.place(x=330,y=230)   



#Boton Calcular
Boton = Button(longw, text="Calcular",font=("Calibri", 14), command=Calcular)
Boton.place(x=230,y=290)


#Precio inicial
Label(longw, text ="Ingrese el precio de la crypto: ", font=("Calibri", 17)).place(x=50,y=30)
Entry(longw, font=("Arial", 10), textvariable=Precioini).place(x=350,y=35)



#Separador
Label(longw, text ="-----------------------------------------------------------------------------------------------------------------",
font=("Calibri", 20)).place(x=10,y=80)




#Calculate profit

#Porcentaje que se espera ganar
Label(longw, text ="¿Cuanto espera ganar?", font=("Calibri", 14)).place(x=80,y=130) #Texto %
Porcent_gan = Entry(longw, font=("Arial", 10),textvariable=Porc__gan)
Porcent_gan.place(x=330,y=135) 


#Cantidad de leverage

Label(longw, text ="¿Que leverage usas?", font=("Calibri", 14)).place(x=80,y=180) #Texto %
Cantidad_lev = Entry(longw, font=("Arial", 10), textvariable=Cant__lev)
Cantidad_lev.place(x=330,y=185) #Cantidad de leverage



#Valor para alcanzar ganancia
Label(longw, text ="El precio buscado es: ", font=("Calibri", 14)).place(x=80,y=230) #Texto %
Valor__gan = Label(longw, text = "valor__fin", font=("Calibri",20))











Button(longw, text="StopLoss -->",font=("Calibri", 14)).place(x=400,y=320)




#Volver


Button(longw, text="Volver",font=("Calibri", 14)).place(x=50,y=310) 




#Extra
Label(longw, text="Hecho con <3 por Faka", font=("Calibri",9)).place(x=460,y=375)
Label(longw, text="v 0.1 ALPHA", font=("Calibri",9)).place(x=1,y=375)

#Prefrences tamaño
longw.geometry("600x400")

#FIN
longw.mainloop()


