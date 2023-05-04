import tkinter as tk
import mysql.connector
from tkinter import ttk
import subprocess

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escuela"
)

mi_cursor = bd.cursor()
mi_cursor.execute("SELECT nombre, edad, email FROM alumnos")
resultado = mi_cursor.fetchall()

# crear ventana de Tkinter
ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Registros")
primero=tk.Label(ventana, text="- Registro de de alumnos -", bg='#383838', fg="white", font='Times 20').pack(pady=30)
# crear Table
tabla = ttk.Treeview(ventana)
tabla['columns'] = ('nombre','edad', 'email')


# ajustar las columnas
tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('nombre', anchor=tk.CENTER, width=200)
tabla.column('edad', anchor=tk.CENTER, width=75)
tabla.column('email', anchor=tk.CENTER, width=250)

# heading
tabla.heading('#0', text='', anchor=tk.CENTER)
tabla.heading('nombre', text='Nombre', anchor=tk.CENTER)
tabla.heading('edad', text='Edad', anchor=tk.CENTER)
tabla.heading('email', text='Email', anchor=tk.CENTER)

ban=True
# agregar datos
for valor in resultado:
  if (ban):
    tabla.insert(parent='', index='end', id=valor[0], tag=['t1'], values=(valor[0], valor[1], valor[2]))
    ban=False
  else:
    tabla.insert(parent='', index='end', id=valor[0], tag=['t2'], values=(valor[0], valor[1], valor[2]))
    ban=True

tabla.tag_configure('t1', foreground= 'white', background = '#383838', font="Times 12")
tabla.tag_configure('t2', foreground='#FFCC00', background = '#003366', font="Times 12")

# mostrar tabla en ventana
tabla.pack()
def regresar():
    ventana.destroy()
    subprocess.call(["python", "crud.py"]) 
button_guardar = tk.Button(ventana, text="Regresar", command=regresar, font="Times", bg="#585858", fg="white")
button_guardar.pack(pady=30)
ventana['bg'] = '#383838'
ventana.resizable(width=0, height=0)
ventana.mainloop()