import sqlite3

# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("base_prueba.db")
# Creamos (si no existe) una tabla creada alumnos con sus campos
conexion.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad integer
                    )""")
conexion.close()
conexion = sqlite3.connect("base_prueba.db")
# Insertamos dos alumnos
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Ligia", 27))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Vladimir", 18))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Jorge", 18))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Jesús", 19))
# Este es necesario para que se ejecuten laas consultas anteriores
conexion.commit()

# Recuperamos un elementos de la tabla alumnos y lo imprimimos
#alumno = conexion.execute("select * from alumnos where nombre like 'Ligia'")
alumno = conexion.execute("select nombre, edad from alumnos ")
# Esto es para solamente traer el primero o bien para traer uno
fila = alumno.fetchall()
#imprimimos la fila (el alumno)
print(fila)
# Cerramos la conexión con SQLITE
conexion.close()