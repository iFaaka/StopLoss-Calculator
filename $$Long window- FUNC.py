from tkinter import Label,Button,Entry,Tk, StringVar
longw = Tk()
longw.title("Crypto helper")
longw.resizable(width=False, height=False) #No se puede cambiar tamaño
dato= StringVar() #https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=59&codigo=59&inicio=45

#Operacion



def Calcular():
    ValorF = int(dato.get()) + 10
    etiqueta = Label(longw, text = ValorF)
    etiqueta.place(x=330,y=230)   



#Calcular
Boton = Button(longw, text="Calcular",font=("Calibri", 14), command=Calcular)
Boton.place(x=230,y=290)



#Prefrences tamaño

longw.geometry("600x400")



Label(longw, text ="Ingrese el precio de la crypto: ", font=("Calibri", 17)).place(x=50,y=30)
Precio_ini = Entry(longw, font=("Arial", 10), textvariable=dato)
Precio_ini.place(x=350,y=35)








#Separador
Label(longw, text ="-----------------------------------------------------------------------------------------------------------------",
font=("Calibri", 20)).place(x=10,y=80)


#Calculate profit

#Porcentaje que se espera ganar
Label(longw, text ="¿Cuanto espera ganar?", font=("Calibri", 14)).place(x=80,y=130) #Texto %
Porcent_gan = Entry(longw, font=("Arial", 10))
Porcent_gan.place(x=330,y=135) 


#Cantidad de leverage

Label(longw, text ="¿Que leverage usas?", font=("Calibri", 14)).place(x=80,y=180) #Texto %
Cant__lev = Entry(longw, font=("Arial", 10))
Cant__lev.place(x=330,y=185) #Cantidad de leverage



#Valor para alcanzar ganancia
Label(longw, text ="El precio buscado es: ", font=("Calibri", 14)).place(x=80,y=230) #Texto %
Valor__gan = Label(longw, text = "valor__fin", font=("Calibri",20))











Button(longw, text="StopLoss -->",font=("Calibri", 14)).place(x=400,y=320)

Button(longw, text="Volver",font=("Calibri", 14)).place(x=50,y=310) 









#Extra
Label(longw, text="Hecho con <3 por Faka", font=("Calibri",9)).place(x=460,y=375)
Label(longw, text="v 0.1 ALPHA", font=("Calibri",9)).place(x=1,y=375)




longw.mainloop()


