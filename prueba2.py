from tkinter import *
from tkinter.ttk import * 
from time import strftime

def hora():
	string = strftime('%H:%M:%S %p')
	etiqueta.config(text=string)
	etiqueta.after(1000, hora)
 
ventana = Tk()
ventana.title('Hora') 
etiqueta = Label(ventana, font=('arial', 20, 'bold'), background='black', foreground='white') 
etiqueta.pack(anchor='center')
hora() 

mainloop()
