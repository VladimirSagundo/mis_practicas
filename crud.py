from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector

# Conectar a la base de datos
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela"
    )
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()


# Crear la tabla de alumnos si no existe
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT, email VARCHAR(255))")

# Función para leer todos los alumnos de la base de datos
def leer_alumnosDB():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos")
    return cursor.fetchall()

# Función para agregar un nuevo alumno a la base de datos
def agregar_alumnoDB(nombre, edad, email):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (%s, %s, %s)", (nombre, edad, email))
        db.commit()
    except mysql.connector.Error as error:
        messagebox.showerror("Error al agregar el alumno", f"No se pudo agregar el alumno: {error}")
    finally:
        cursor.close()


# Función para actualizar un alumno existente en la base de datos
def actualizar_alumnoDB(id, nombre, edad, email):
    iid = int(id)
    cursor = db.cursor()
    print("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    cursor.execute("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    db.commit()

# Función para eliminar un alumno existente de la base de datos
def eliminar_alumnoDB(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    db.commit()

# Función para mostrar una lista de todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla
    for widget in tabla_alumnos.winfo_children():
        widget.destroy()

# Función para agregar un nuevo alumno
def agregar_alumno():
    # Obtener los datos del nuevo alumno
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()

    # Validar que los campos no estén vacíos
    if not nombre or not edad or not email:
        messagebox.showerror("Error al agregar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Agregar el nuevo alumno
    agregar_alumnoDB(nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()

# Función para actualizar un alumno existente
def actualizar_alumno():
    # Obtener los datos del alumno a actualizar
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()
    id = entrada_id.get()

    # Validar que los campos no estén vacíos
    if not id or not nombre or not edad or not email:
        messagebox.showerror("Error al actualizar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Actualizar el alumno
    actualizar_alumnoDB(id, nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_id.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()


# Función para eliminar un alumno existente
def eliminar_alumno():
    # Obtener el ID del alumno a eliminar
    id = entrada_id.get()

    # Validar que se haya ingresado un ID
    if not id:
        messagebox.showerror("Error al eliminar el alumno", "Por favor ingrese el ID del alumno a eliminar")
        return

    # Preguntar al usuario si está seguro de eliminar el alumno
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este alumno?")

    if confirmar:
        # Eliminar el alumno
        eliminar_alumnoDB(id)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()


# Crear la ventana principal
ventana = Tk()
ancho_ventana = 400
alto_ventana = 300
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana['bg'] = '#383838'
ventana.title("Registro")

# Crear los campos de entrada para los datos del alumno
Label(ventana, text="- Bienvenido -",  font="Times 20", bg="#383838", fg="white").grid(row=0, column=1, padx=0, pady=0)


Label(ventana, text="Id:",  font="Times", bg="#383838", fg="white").grid(row=1, column=0, padx=5, pady=5)
entrada_id = Entry(ventana,  font="Times", bg="#383838", fg="white")
entrada_id.grid(row=1, column=1, padx=5, pady=5)

Label(ventana, text="Nombre:",  font="Times", bg="#383838", fg="white").grid(row=2, column=0, padx=5, pady=5)
entrada_nombre = Entry(ventana,  font="Times", bg="#383838", fg="white")
entrada_nombre.insert(0, "Vladimir")
entrada_nombre.grid(row=2, column=1, padx=5, pady=5)

Label(ventana, text="Edad:",  font="Times", bg="#383838", fg="white").grid(row=3, column=0, padx=5, pady=5)
entrada_edad = Entry(ventana,  font="Times", bg="#383838", fg="white")
entrada_edad.insert(0, "18")
entrada_edad.grid(row=3, column=1, padx=5, pady=5)

Label(ventana, text="Email:",  font="Times", bg="#383838", fg="white").grid(row=4, column=0, padx=5, pady=5)
entrada_email = Entry(ventana,  font="Times", bg="#383838", fg="white")
entrada_email.insert(0, "vladisagudo@gmail.com")
entrada_email.grid(row=4, column=1, padx=5, pady=5)

# Crear los botones para agregar, actualizar y eliminar alumnos
Button(ventana, text="Agregar Alumno", command=agregar_alumno, font="Times", bg="#585858", fg="white").grid(row=1, column=2, padx=7, pady=7)
Button(ventana, text="Actualizar Alumno", command=actualizar_alumno, font="Times", bg="#585858", fg="white").grid(row=2, column=2, padx=7, pady=7)
Button(ventana, text="Eliminar Alumno", command=eliminar_alumno, font="Times", bg="#585858", fg="white").grid(row=3, column=2, padx=7, pady=7)
Button(ventana, text="Cerrar", command=ventana.quit, font="Times", bg="#585858", fg="white").grid(row=5, column=1, padx=3, pady=3)

def lista_registros():
    ventana.destroy()
    subprocess.call(["python", "lista_registros.py"])
Button(ventana, text="Lista de Registros", command=lista_registros, font="Times", bg="#585858", fg="white").grid(row=4, column=2, padx=7, pady=7)
# Crear la tabla para mostrar los alumnos
tabla_alumnos = Frame(ventana)
tabla_alumnos.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

Label(tabla_alumnos, text="ID").grid(row=0, column=0)
Label(tabla_alumnos, text="Nombre").grid(row=0, column=1)
Label(tabla_alumnos, text="Edad").grid(row=0, column=2)
Label(tabla_alumnos, text="Email").grid(row=0, column=3)

# Mostrar la lista de alumnos en la tabla
mostrar_alumnos()

# Iniciar el loop de la ventana
ventana.resizable(width=0, height=0)
ventana.mainloop()