import tkinter as tk
import os
import subprocess

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "Vladimir" and contrasena == "Sagundo":
        resultado.config(text="¡¡ Inicio de sesión exitoso !!", font='Arial', fg="white")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Inicio de sesión")

def __init__(self, master):
   self.master = master

   

# Crear campos de entrada para el nombre de usuario y la contraseña
primero=tk.Label(ventana, text="- Usuario -", bg='#383838', fg="white", font='Times 20').pack(pady=10)
nombre_usuario = tk.Entry(ventana, fg="white",)
nombre_usuario.insert(0, "Vladimir")
nombre_usuario.pack(pady=20)
tk.Label(ventana, text="- Contraseña -", bg='#383838', fg="white", font='Times 20').pack(pady=10)
contrasena_usuario = tk.Entry(ventana, show="*", fg="white")
contrasena_usuario.insert(0, "Sagundo")
contrasena_usuario.pack(pady=15)
nombre_usuario['bg'] = '#424242'
contrasena_usuario['bg'] = '#424242'

def menú():
    ventana.destroy()
    subprocess.call(["python", "Proyecto_menú.py"]) 

def base_de_datos():
    ventana.destroy()
    subprocess.call(["python", "base_de_datos.py"])

def inicio():
    print ("Inicio Exitoso")
# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=inicio, fg="white")
iniciar_sesion.pack(padx=100, pady=10)
iniciar_sesion['bg'] = '#585858'

#salir = tk.Button(ventana, text="Regresar", command=menú, fg="white")
#salir.pack(padx=40, pady=70)
#salir.pack()
#salir['bg'] = '#585858'


# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
ventana.resizable(width=0, height=0)
resultado.pack(pady=10)
resultado['bg'] = '#383838'
ventana['bg'] = '#383838'
ventana.mainloop()