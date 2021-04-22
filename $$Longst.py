from tkinter import Label,Button,Entry,Tk
longsw = Tk()
longsw.title("Crypto helper")
longsw.resizable(width=False, height=False) #No se puede cambiar tamaño

#Prefrences tamaño

longsw.geometry("600x400")

#Price initial 

Label(longsw, text ="Ingrese el precio de la crypto: ", font=("Calibri", 17)).place(x=50,y=30)
Entry(longsw, font=("Arial", 10)).place(x=350,y=35)


#Separador
Label(longsw, text ="-----------------------------------------------------------------------------------------------------------------",
font=("Calibri", 20)).place(x=10,y=80)


#Calculate profit

Label(longsw, text ="¿Hasta cuanto para abajo?", font=("Calibri", 14)).place(x=80,y=130) #Texto %
Entry(longsw, font=("Arial", 10)).place(x=330,y=135) #Porcentaje que se espera ganar

Label(longsw, text ="¿Que leverage usas?", font=("Calibri", 14)).place(x=80,y=180) #Texto %
Entry(longsw, font=("Arial", 10)).place(x=330,y=185) #Cantidad de leverage


Label(longsw, text ="El stop va en: ", font=("Calibri", 14)).place(x=80,y=230) #Texto %
Entry(longsw, font=("Arial", 10)).place(x=330,y=235) #Valor para alcanzar ganancia

Button(longsw, text="Calcular",font=("Calibri", 14)).place(x=230,y=290)

Button(longsw, text="StopLoss -->",font=("Calibri", 14)).place(x=400,y=320)

Button(longsw, text="Volver",font=("Calibri", 14)).place(x=50,y=310) 









#Extra
Label(longsw, text="Hecho con <3 por Faka", font=("Calibri",9)).place(x=460,y=375)
Label(longsw, text="v 0.1 ALPHA", font=("Calibri",9)).place(x=1,y=375)

longsw.mainloop()