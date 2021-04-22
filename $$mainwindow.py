from tkinter import *
main = Tk()
main.title("Crypto helper")
main.resizable(width=False, height=False) #No se puede cambiar tamaño

#Prefrences tamaño

main.geometry("600x400")

#Hi Text

Label(main, text ="¡Hola Trader!", font=("Calibri", 24)).place(x=200,y=30)
Label(main, text ="¿Que operacion vas a hacer ahora?", font=("Calibri", 18)).place(x=120,y=80)

#Buttons Main

Button(main, text="Long",width=20,height=3, font=("Calibri", 12)).place(x=90,y=200)
Button(main, text="Short",width=20,height=3, font=("Calibri", 12)).place(x=360,y=200)


Button(main, text="Ayuda",width=10,height=1, font=("Calibri", 12)).place(x=250,y=350)

#Extra
Label(main, text="Hecho con <3 por Faka", font=("Calibri",9)).place(x=460,y=375)
Label(main, text="v 0.1 ALPHA", font=("Calibri",9)).place(x=1,y=375)

main.mainloop()