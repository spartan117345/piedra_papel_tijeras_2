from tkinter import *
from tkinter import messagebox

ventana_juego = Tk()

ventana_juego.title("======================juego de piedra-papel-tijeras==================")

ventana_juego.geometry("800x500")

ventana_juego.resizable(0,0)

ventana_juego.config(bg="grey")


frame_2 = Frame(ventana_juego)
frame_2.config(bg="ivory2",width=780, height=125)
frame_2.place(x=10,y=230)

# img_bt_tijeras = PhotoImage(file = "img/tijera.png")

bt_tijeras = Button(frame_2, width = 10, height = 105)
bt_tijeras.place(x=116, y=7)

























































ventana_juego.mainloop()