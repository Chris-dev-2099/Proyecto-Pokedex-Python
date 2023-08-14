from tkinter import *
import tkinter
import os
from io import *
from PIL import ImageTk, Image
from AB_pokemones import *
import json
from ABC_img_pokemones import *


os.system("cls")
# POKEDEX

'''
Grupo: - Christopher Arboleda
       - Andrés Moreano
       - Leo Trejos 
'''


class Pokedex:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Pokedex")
        self.ventana.geometry("620x450")

        self.fondo_1 = Image.open("pokedex_img.png")
        self.fondo_1 = self.fondo_1.resize((620, 450), Image.ANTIALIAS)

        self.fondo_one = ImageTk.PhotoImage(self.fondo_1)
        self.etiquet_fondo = Label(self.ventana, image=self.fondo_one)
        self.etiquet_fondo.place(x=0, y=0)

        self.titulo_principal = tkinter.Label(
            self.ventana, text="Pokedex", font="Helvetica 36", bg="#FF336C")
        self.titulo_principal.place(x=314, y=10, width=205, height=42,)

        self.cajaTexto = Entry(self.ventana, font="Helvetica 10", bg="#D6D6D6")
        self.cajaTexto.place(x=120, y=290, width=75)

        self.mostrar_pokemon = Label(self.ventana, bg="#D6D6D6")
        self.mostrar_pokemon.place(x=365, y=110)

        self.tu_frame = Frame(self.ventana, bg="#73D289")
        self.tu_frame.place(x=79, y=144)

        self.mostrar_imagen = Label(self.tu_frame, bg="#73D289")

        self.boton_1 = Button(self.ventana, text="Buscar", width=7, height=2, bg="#73D289",
                              command=lambda: self.busqueda(Pokemons))
        self.boton_1.place(x=96, y=375, height=38, width=85)

    # Funcion para cambiar las dimensiones de las imagenes
    def resize_image(self, image, new_width, new_height):
        return image.resize((new_width, new_height), Image.ANTIALIAS)

    def busqueda(self, Pokemons):
        poke_buscado = self.cajaTexto.get()
        PK = Pokemons.get(poke_buscado)
        imagen_pokemon = Pokemons_img.get(poke_buscado)
        if PK is not None and imagen_pokemon is not None:
            nombre_pokemon = poke_buscado
            info_pokemon = str(PK).replace("[", "").replace("]", "").replace(
                ",", "\n")  # Convertir a string y separar por líneas
            texto_mostrar = f"Nombre: {nombre_pokemon}\n\nInformación:\n{info_pokemon}"
            self.mostrar_pokemon.config(
                text=texto_mostrar, width=27, height=8, bg="#73D289")

            # ---------------------------------------------------------------------------------------------------------------------------------
            '''Archivo que guardara el historial de busqueda (cambiar la ruta de la ubicación del 
            archivo de ser necesario para su correcto funcionamiento):'''

            archivo = open(
                r"C:\Users\ELNILO.DESKTOP-E6TI75M\Desktop\Proyecto_pokedex\ABCD_Historial_busqueda.txt",'a')
            archivo.write(f"\n{texto_mostrar}\n")
            archivo.close()

            # Mostrar la imagen del Pokémon
            # Cambiar el tamaño de la imagen
            imagen_mostrar = self.resize_image(imagen_pokemon, 130, 130)
            imagen_mostrar = ImageTk.PhotoImage(imagen_mostrar)
            self.mostrar_imagen.config(image=imagen_mostrar)
            self.mostrar_imagen.image = imagen_mostrar
            self.mostrar_imagen.grid(row=4, column=0, padx=13, pady=3)
        else:
            self.mostrar_pokemon.config(text="", width=40, height=12)
            self.mostrar_imagen.config(image=None)
            self.mostrar_imagen.image = None
            self.mostrar_imagen.grid_forget()

    def start(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.start()
