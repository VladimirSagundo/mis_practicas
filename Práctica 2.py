import tkinter as tktk


class MenuScreen(tktk.Frame):    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Ejemplo de pantalla con menú")

        # Creamos el menú superior
        self.menu_bar = tktk.Menu(self.master)
        self.master.config(menu=self.menu_bar)


        # Creamos las opciones del menúa
        self.file_menu = tktk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir archivo", command=self.open_file)
        self.file_menu.add_command(label="Guardar archivo", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        

        self.edit_menu = tktk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        

        self.edit_menu = tktk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Insertar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Imagen", command=self.image_names)
        #tktk.Button(self, text="Imagen", command=self.press_button)

        # Agregamos algunos widgets a la pantalla
        self.label = tktk.Label(self, text="¡Bienvenido a mi programa!")
        self.label.pack(pady=70)
        self.button = tktk.Button(self, text="Presiona para algo divertido", command=self.press_button)
        self.button.pack()
        self.label['bg'] = '#5f9ea0'
        self.button['bg'] = '#5f9ea0'
 

        self.pack()

    def open_file(self):
        print("Abrir archivo")

    def save_file(self):
        print("Guardar archivo")

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Copiar")

    def paste(self):
        print("Pegar")

    def press_button(self):
        print("Botón presionado")

    def image_names(self):
        print("Imagen")


root = tktk.Tk()
root.geometry("420x380")
root['bg'] = '#5f9ea0'
app = MenuScreen(root)
app['bg'] = '#5f9ea0'
app.mainloop()