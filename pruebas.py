from tkinter import *

def llamada():
    root.destroy()
    obtenido=ventana.get()

 
root = Tk()
root.title("primera ventana")
root.config(bg="black", width=400, height=400)

boton1 = Button(root, text="presioname", command=llamada)
boton1.pack()

ventana = Entry(root)
ventana.pack()


root.mainloop()