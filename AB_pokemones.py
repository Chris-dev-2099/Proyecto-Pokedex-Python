from tkinter import *
import tkinter
import os
from PIL import ImageTk, Image

os.system("cls")

info_bulbasaur = ["Tipo: planta - veneno",
                  "Habilidad: Espesura ", "Peso: 6.9kg ", "Altura: 0.7m"]
info_Ivysaur = ["Tipo:planta_veneno",
                "Habilidad: Espesura", "Peso: 13.0kg ", "Altura: 1.0m"]
info_Venusaur = ["Tipo: planta_veneno",
                 "Habilidad: Espesura", "Peso: 100.0kg", "Altura: 2.0m"]
info_Charmander = ["Tipo: Fuego", "Habilidad: Mar llamas",
                   "Peso: 8.5kg", "Altura: 0.6m"]
info_Charmeleon = ["Tipo: Fuego",
                   "Habilidad: Mar llamas", "Peso: 19kg", "Altura: 1.1m"]
info_Charizard = ["Tipo: Fuego - Volador",
                  "Habilidad: Mar llamas", "Peso: 90.5kg", "Altura: 1.7m"]
info_Squirtle = ["Tipo: Agua", "Habilidad: Torrente",
                 "Peso: 9.0kg", "Altura: 0.5m"]
info_Wartortle = ["Tipo: Agua", "Habilidad: Torrente",
                  "Peso: 22.5kg", "Altura: 1.0m"]
info_Blastoise = ["Tipo: Agua", "Habilidad: Torrente",
                  "Peso: 85.5kg", "Altura: 1.6m"]
info_Caterpie = ["Tipo: Bicho", "Habilidad: Polvo escudo",
                 "Peso: 2.9Kg", "Altura: 0.3m"]
info_Metapod = ["Tipo: Bicho", "Habilidad: Mudar",
                "Peso: 9.9kg", "Altura: 0.7m"]
info_Butterfree = ["Tipo: Bicho - Volador",
                   "Habilidad: Ojo compuesto", "Peso: 32Kg", "Altura: 1.1m"]
info_Weedle = ["Tipo: Bicho - Veneno",
               "Habilidad: Fuga", "Peso: 3.2Kg", "Altura: 0.3m"]
info_Kakuna = ["Tipo: Bicho - Veneno",
               "Habilidad: Mudar", "Peso: 10Kg", "Altura: 0.6m"]
info_Beedrill = ["Tipo: Bicho - Veneno",
                 "Habilidad: Enjambre", "Peso: 29.5kg", "Altura: 1.0m"]
info_Pidgey = ["Tipo: Normal - Volador",
               "Habilidad: Vista Lince Tumbos", "Peso: 1.8kg", "Altura: 0.3m"]
info_Pidgeotto = ["Tipo: Normal - Volador",
                  "Habilidad: Vista Lince Tumbos", "Peso: 30kg", "Altura: 1.1m"]
info_Pidgeot = ["Tipo: Normal - Volador",
                "Habilidad: Vista Lince Tumbos", "Peso: 39.5kg", "Altura: 1.5m"]
info_Rattata = ["Tipo: Normal", "Habilidad: Fuga Agallas",
                "Peso: 3.5kg", "Altura: 0.3m"]
info_Raticate = ["Tipo: Normal", "Habilidad: Fuga Agallas",
                 "Peso: 18.5kg", "Altura: 0.7m"]
info_Spearow = ["Tipo: Normal - Volador",
                "Habilidad: Vista Lince", "Peso: 2.0 kg", "Altura: 0.3m"]
info_Fearow = ["Tipo: Normal - Volador",
               "Habilidad: Vista Lince", "Peso: 38.0", "Altura: 1.2m"]
info_EKans = ["Tipo: Veneno", "Habilidad: Intimdación Mudar",
              "Peso: 6.9kg", "Altura: 2.0m"]
info_Arbok = ["Tipo: Veneno", "Habilidad: Intimdación Mudar",
              "Peso: 65.0kg", "Altura: 3.5m"]
info_Pikachu = ["Tipo: Electrico",
                "Habilidad: Electricidad estatica", "Peso: 6.0kg", "Altura: 0.4m"]
info_Raichu = ["Tipo: Electrico",
               "Habilidad: Electricidad estática", "Peso: 30.0kg", "Altura: 0.8m"]
info_Sandshrew = ["Tipo: Tierra", "Habilidad: Velo arena",
                  "Peso: 12.0kg", "Altura: 0.6m"]
info_Sandslash = ["Tipo: Tierra", "Habilidad: Velo arena",
                  "Peso: 29.5kg", "Altura: 1.0m"]
info_Nidoran_F = ["Tipo: Veneno",
                  "Habilidad: Punto tóxico Rivalidad", "Peso: 7.0kg", "Altura: 0.4m"]
info_Nidorina = ["Tipo: Veneno",
                 "Habilidad: Punto tóxico Rivalidad", "Peso: 20.0kg", "Altura: 0.8m"]
info_Nidoqueen = ["Tipo: Veneno - Tierra",
                  "Habilidad: Punto tóxico Rivalidad", "Peso: 60.0kg", "Altura: 1.3m"]
info_Nidoran_M = ["Tipo: Veneno",
                  "Habilidad: Punto tóxico Rivalidad", "Peso: 9.0kg", "Altura: 0.5m"]
info_Nidorino = ["Tipo: Veneno",
                 "Habilidad: Punto tóxico Rivalidad", "Peso: 19.5kg", "Altura: 0.9m"]
info_Nidoking = ["Tipo: Veneno - Tierra",
                 "Habilidad: Punto tóxico Rivalidad", "Peso: 62.0kg", "Altura:1.4m"]
info_Clefairy = ["Tipo: Hada", "Habilidad: Gran encanto Muro mágico",
                 "Peso: 7.5kg", "Altura: 0.6m"]
info_Clefable = ["Tipo: Hada", "Habilidad: Gran encanto Muro mágico",
                 "Peso: 40.0kg", "Altura: 1.3m"]
info_Vulpix = ["Tipo: Fuego", "Habilidad: Absorbe fuego",
               "Peso: 9.9kg", "Altura: 0.6m"]
info_Ninetales = ["Tipo: Fuego", "Habilidad: Absorbe fuego",
                  "Peso: 19.9kg", "Altura: 1.1m"]
info_Jigglypuff = ["Tipo: Normal - Hada",
                   "Habilidad: Gran Encanto-Tenacidad", "Peso: 5.5kg", "Altura: 0.5m"]
info_Wigglytuff = ["Tipo: Normal-Hada",
                   "Habilidad: Gran Encanto-Tenacidad", "Peso: 12.0 kg", "Altura: 1.0 m"]
info_Zubat = ["Tipo: Veneno-Volador",
              "Habilidad: Fuerza Mental", "Peso: 7.5 kg", "Altura: 0.8 m"]
info_Golbat = ["Tipo: Veneno-Volador",
               "Habilidad: Fuerza Mental", "Peso: 55.0 kg", "Altura: 1.6 m"]
info_Oddish = ["Tipo: Planta-Veneno",
               "Habilidad: Clorofila", "Peso: 5.4 kg", "Altura: 0.5 m"]
info_Gloom = ["Tipo: Planta-Veneno",
              "Habilidad: Clorofila", "Peso: 8.6 kg", "Altura: 0.8 m"]
info_Vileplume = ["Tipo: Planta-Veneno",
                  "Habilidad: Clorofila", "Peso: 18.6 kg", "Altura: 1.2 m"]
info_Paras = ["Tipo: Bicho-Planta",
              "Habilidad: Efecto Espora-Piel Seca", "Peso: 5.4 kg", "Altura: 0.3 m"]
info_Parasect = ["Tipo: Bicho-Planta",
                 "Habilidad: Efecto Espora-Piel Seca", "Peso: 29.5 kg", "Altura: 1.0 m"]
info_Venonat = ["Tipo: Bicho-Veneno",
                "Habilidad: Ojo Compuesto-Cromolente", "Peso: 30.0 kg", "Altura: 1.0 m"]
info_Venomoth = ["Tipo: Bicho-Veneno",
                 "Habilidad: Polvo Escudo-Cromolente", "Peso: 12.5 kg", "Altura: 1.5 m"]
info_Diglett = ["Tipo: Tierra", "Habilidad: Trampa arena",
                "Peso: 0.8kg", "Altura: 0.2m"]
info_Dugtrio = ["Tipo: Tierra", "Habilidad: Velo arena",
                "Peso: 33.3kg", "Altura: 0.7m"]
info_Meowth = ["Tipo: Normal", "Habilidad: Recogida",
               "Peso: 4.2kg", "Altura: 0.4m"]
info_Persian = ["Tipo: Normal", "Habilidad: Experto",
                "Peso: 32.0kg", "Altura: 1.0m"]
info_Psyduck = ["Tipo: Agua", "Habilidad: Humedad",
                "Peso: 19.6kg", "Altura: 0.8m"]
info_Golduck = ["Tipo: Agua", "Habilidad: Aclimatacion",
                "Peso: 76.6kg", "Altura: 1.7m"]
info_Mankey = ["Tipo: Lucha", "Habilidad: Irascible",
               "Peso: 28.0kg", "Altura: 0.5m"]
info_Primeape = ["Tipo: Lucha", "Habilidad: Espiritu vital",
                 "Peso: 32.0kg", "Altura: 1.0m"]
info_Growlithe = ["Tipo: Fuego", "Habilidad: Absorbe fuego",
                  "Peso: 19.0kg", "Altura: 0.7m"]
info_Arcanine = ["Tipo: Fuego", "Habilidad: Intimiacion",
                 "Peso: 155.0kg", "Altura: 1.9m"]
info_Poliwag = ["Tipo: Agua", "Habilidad: Humedad",
                "Peso: 12.4kg", "Altura: 0.6m"]
info_Poliwhirl = ["Tipo: Agua", "Habilidad: Absorbe agua",
                  "Peso: 20.0kg", "Altura: 1.0m"]
info_Poliwrath = ["Tipo: Agua-Pelea",
                  "Habilidad: Absorbe agua", "Peso: 54.0kg", "Altura: 1.3m"]
info_Abra = ["Tipo: Psiquico", "Habilidad: Fuerza mental",
             "Peso:19.5kg ", "Altura: 0.9m"]
info_Kadabra = ["Tipo: Psiquico", "Habilidad: Sicronia",
                "Peso: 56.5kg", "Altura: 1.3m"]
info_Alakazam = ["Tipo: Psiquico", "Habilidad: Fuerza mental",
                 "Peso: 48.0kg", "Altura: 1.5m"]
info_Machop = ["Tipo: Lucha", "Habilidad: Agallas",
               "Peso: 19.5kg", "Altura: 0.8m"]
info_Machoke = ["Tipo: Lucha", "Habilidad: Agallas",
                "Peso: 70.5kg", "Altura: 1.5m"]
info_Machamp = ["Tipo: Lucha", "Habilidad: Agallas",
                "Peso: 130.0kg", "Altura: 1.6m"]
info_Bellsprout = ["Tipo: Planta-Veneno",
                   "Habilidad: Clorofila", "Peso: 4.0kg", "Altura: 0.7m"]
info_Weepinbell = ["Tipo: Planta-Veneno",
                   "Habilidad: Clorofila", "Peso: 6.4kg", "Altura: 1.0m"]
info_Victreebel = ["Tipo: Planta-Veneno",
                   "Habilidad: Clorofila", "Peso: 15.5kg", "Altura: 1.7m"]
info_Tentacool = ["Tipo: Agua-Veneno",
                  "Habilidad: Viscosecrecion", "Peso: 45.5kg", "Altura: 0.9m"]
info_Tentacruel = ["Tipo: Agua-Veneno",
                   "Habilidad: Cuerpo puro", "Peso: 55.0kg", "Altura: 1.6m"]
info_Geodude = ["Tipo: Roca-Tierra",
                "Habilidad: Cabeza roca", "Peso: 20.0kg", "Altura: 0.4m"]
info_Graveler = ["Tipo: Roca-Tierra",
                 "Habilidad: Cabeza roca", "Peso: 105.0kg", "Altura: 1.0m"]
info_Golem = ["Tipo: Roca-Tierra", "Habilidad: Cabeza roca",
              "Peso: 300.0kg", "Altura: 1.4m"]
info_Ponyta = ["Tipo: Fuego", "Habilidad: Fuga",
               "Peso: 30.0kg", "Altura: 1.0m"]
info_Rapidash = ["Tipo: Fuego", "Habilidad: Absorbe fuego",
                 "Peso: 95.0kg", "Altura: 1.7m"]
info_Slowpoke = ["Tipo: Agua-Psiquico",
                 "Habilidad: Despiste", "Peso: 36.0kg", "Altura: 1.2m"]
info_Slowbro = ["Tipo: Agua-Psiquico",
                "Habilidad: Ritmo propio", "Peso: 78.5kg", "Altura: 1.6m"]
info_Magnemite = ["Tipo: Electrico-Acero",
                  "Habilidad: Robustez", "Peso: 6.0kg", "Altura: 0.3m"]
info_Magneton = ["Tipo: Electrico-Acero",
                 "Habilidad: Iman", "Peso: 60.0kg", "Altura: 1.0m"]
info_Farfetchd = ["Tipo: Normal-Volador",
                  "Habilidad: Vista lince", "Peso: 15.0kg", "Altura: 0.8m"]
info_Doduo = ["Tipo: Normal-Volador",
              "Habilidad: Fuga", "Peso: 39.2kg", "Altura: 1.4m"]
info_Dodrio = ["Tipo: Normal-Volador",
               "Habilidad: Madrugar", "Peso: 85.2kg", "Altura: 1.8m"]
info_Seel = ["Tipo: Agua-Hielo", "Habilidad: Sebo",
             "Peso: 90.0kg", "Altura: 1.1m"]
info_Dewgong = ["Tipo: Agua-Hielo",
                "Habilidad: Sebo", "Peso: 120.0kg", "Altura:1.7m"]
info_Grimer = ["Tipo: Veneno", "Habilidad: Hedor",
               "Peso: 30.0kg", "Altura: 0.9m"]
info_Muk = ["Tipo: Veneno", "Habilidad: Viscosidad",
            "Peso: 30.0kg", "Altura: 1.2m"]
info_Shellder = ["Tipo: Agua", "Habilidad: Caparazon",
                 "Peso: 4.0kg", "Altura: 0.3m"]
info_Cloyster = ["Tipo:Agua-Hielo", "Habilidad: Encadenado",
                 "Peso: 132.5kg", "Altura: 1.5m"]
info_Gastly = ["Tipo: Fantasma-Veneno",
               "Habilidad: Levitacion", "Peso: 0.1kg", "Altura: 1.3m"]
info_Haunter = ["Tipo: Fantasma-Veneno",
                "Habilidad: Levitacion", "Peso: 0.1kg", "Altura: 1.6m"]
info_Gengar = ["Tipo: Fantasma-Veneno",
               "Habilidad: Cuerpo maldito", "Peso: 40.5kg", "Altura: 1.5m"]
info_Onix = ["Tipo: Roca-Tierra", "Habilidad: Cabeza roca ",
             "Peso: 210.0kg", "Altura: 8.8m"]
info_Drowzee = ["Tipo: Psiquico", "Habilidad: Insomnio",
                "Peso: 32.4kg", "Altura: 1.0m"]
info_Hypno = ["Tipo: Psiquico", "Habilidad: Insomnio",
              "Peso: 75.6kg", "Altura: 1.6m"]
info_Krabby = ["Tipo: Agua", "Habilidad: Corte fuerte",
               "Peso: 6.5kg", "Altura: 0.4m"]
info_Kingler = ["Tipo: Agua", "Habilidad: Corte fuerte",
                "Peso: 60.0kg", "Altura: 1.3m"]
info_Voltorb = ["Tipo: Electrico", "Habilidad: Insonorizar",
                "Peso: 10.4kg", "Altura: 0.5m"]
info_Electrode = ["Tipo: Electrico",
                  "Habilidad: Elec. Estatica, Insonorizar", "Peso: 66,6 kg", "Altura: 1,2 m"]
info_Exeggcute = ["Tipo: Planta-Psiquico",
                  "Habilidad: Clorofila", "Peso: 2,5 kg", "Altura: 0.4 m"]
info_Exeggutor = ["Tipo: Planta-Psiquico",
                  "Habilidad: Clorofila", "Peso: 120.0 kg", "Altura: 2.0 m"]
info_Cubone = ["Tipo: Tierra", "Habilidad: Cabeza Roca-Pararrayos",
               "Peso: 6.5 kg", "Altura: 0.4 m"]
info_Marowak = ["Tipo: Tierra", "Habilidad: Cabeza Roca-Pararrayos",
                "Peso: 45.0 kg", "Altura: 1.0 m"]
info_Hitmonlee = ["Tipo: Lucha", "Habilidad: Flexibilidad-Audaz",
                  "Peso: 49.8 kg", "Altura: 1.5 m"]
info_Hitmonchan = ["Tipo: Lucha", "Habilidad: Vista Lince-Puño Ferreo",
                   "Peso: 50.2 kg", "Altura: 1.4 m"]
info_Lickitung = ["Tipo: Normal", "Habilidad: Despiste-Ritmo Propio",
                  "Peso: 65.5 kg", "Altura: 1.2 m"]
info_Koffing = ["Tipo: Veneno", "Habilidad: Levitacion-Gas Reactivo",
                "Peso: 1.0 kg", "Altura: 0.6 m"]
info_Weezing = ["Tipo: Veneno", "Habilidad: Levitacion-Gas Reactivo",
                "Peso: 9.5 kg", "Altura: 1.2 m"]
info_Rhyhorn = ["Tipo: Tierra-Roca",
                "Habilidad: Cabeza Roca-Pararrayos", "Peso: 115.0 kg", "Altura: 1.0 m"]
info_Rhydon = ["Tipo: Tierra-Roca", "Habilidad: Cabeza Roca-Pararrayos",
               "Peso: 120.0 kg", "Altura: 1.9 m"]
info_Chansey = ["Tipo: Normal", "Habilidad: Cura Natural-Dicha",
                "Peso: 34.6 kg", "Altura: 1.1 m"]
info_Tangela = ["Tipo: Planta", "Habilidad: Clorofila-Defensa Hoja",
                "Peso: 35.0 kg", "Altura: 1.0 m"]
info_Kangaskhan = ["Tipo: Normal", "Habilidad: Madrugar-Intrepido",
                   "Peso: 80.0 kg", "Altura: 2.2 m"]
info_Horsea = ["Tipo: Agua", "Habilidad: Nado Rapido-Francotirador",
               "Peso: 8.0 kg", "Altura: 0.4 m"]
info_Seadra = ["Tipo: Agua", "Habilidad: Punto Toxico-Francotirador",
               "Peso: 25.0 kg", "Altura: 1.2 m"]
info_Goldeen = ["Tipo: Agua", "Habilidad: Nado Rapido-Velo Agua",
                "Peso: 15.0 kg", "Altura: 0.6 m"]
info_Seaking = ["Tipo: Agua", "Habilidad: Nado Rapido-Velo Agua",
                "Peso: 39.0 kg", "Altura: 1.3 m"]
info_Staryu = ["Tipo: Agua", "Habilidad: Cura Natural-Iluminacion",
               "Peso: 34.5 kg", "Altura: 0.8 m"]
info_Starmie = ["Tipo: Agua", "Habilidad: Cura Natural-Iluminacion",
                "Peso: 80.0 kg", "Altura: 1.1 m"]
info_Mr_Mime = ["Tipo: Psiquico-Hada",
                "Habilidad: Insonorizar-Filtro", "Peso: 54.5 kg", "Altura: 1.3 m"]
info_Scyther = ["Tipo: Bicho-Volador",
                "Habilidad: Enjambre-Experto", "Peso: 56.0 kg", "Altura: 1.5 m"]
info_Jynx = ["Tipo: Hielo-Psiciquico",
             "Habilidad: Despiste-Alerta", "Peso: 40.6 kg", "Altura: 1.4 m"]
info_Electabuzz = ["Tipo: Electrico",
                   "Habilidad: Elec. Estatica", "Peso: 30.0 kg", "Altura: 1.1 m"]
info_Magmar = ["Tipo: Fuego", "Habilidad: Cuerpo Llama",
               "Peso: 44.5 kg", "Altura: 1.3 m"]
info_Pinsir = ["Tipo: Bicho",
               "Habilidad: Corte Fuerte-Rompemoldes", "Peso: 55.0 kg", "Altura: 1.5 m"]
info_Tauros = ["Tipo: Normal", "Habilidad: Intimidacion-Irascible",
               "Peso: 88.4 kg", "Altura: 1.4 m"]
info_Magikarp = ["Tipo: Agua", "Habilidad: Nado Rapido",
                 "Peso: 10.0 kg", "Altura: 0.9 m"]
info_Gyarados = ["Tipo: Agua-Volador",
                 "Habilidad: Intimidacion", "Peso: 235.0 kg", "Altura: 6.5 m"]
info_Lapras = ["Tipo: Agua-Hielo", "Habilidad: Absorbe Agua-Caparazon",
               "Peso: 220.0 kg", "Altura: 2.5 m"]
info_Ditto = ["Tipo: Normal", "Habilidad: Flexibilidad",
              "Peso: 4.0 kg", "Altura: 0.3 m"]
info_Eevee = ["Tipo: Normal", "Habilidad: Fuga-Adaptable",
              "Peso: 6.5 kg", "Altura: 0.3 m"]
info_Vaporeon = ["Tipo: Agua", "Habilidad: Absorbe Agua",
                 "Peso: 29.0 kg", "Altura: 1.0 m"]
info_Jolteon = ["Tipo: Electrico", "Habilidad: Absorbe Elec",
                "Peso: 24.5 kg", "Altura: 0,8 m"]
info_Flareon = ["Tipo: Fuego", "Habilidad: Absorbe Fuego",
                "Peso: 25.0 kg", "Altura: 0,9 m"]
info_Porygon = ["Tipo: Normal",
                "Habilidad: Calco-Descarga", "Peso: 36.5 kg", "Altura: 0.8 m"]
info_Omanyte = ["Tipo: Roca-Agua",
                "Habilidad: Caparazón-Nado Rápido", "Peso: 7.5 kg", "Altura: 0.4 m"]
info_Omastar = ["Tipo: Roca-Agua", "Habilidad: Caparazón-Nado Rápido",
                "Peso: 35.0 kg", "Altura: 1.0 m"]
info_Kabuto = ["Tipo: Roca-Agua", "Habilidad: Nado Rápido-Armadura Batalla",
               "Peso: 11.5 kg", "Altura: 0.5 m"]
info_Kabutops = ["Tipo: Roca-Agua",
                 "Habilidad: Nado Rápido-Armadura Batalla", "Peso: 40.5 kg", "Altura: 1.3 m"]
info_Aerodactyl = ["Tipo: Roca-Volador",
                   "Habilidad: Cabeza Roca-Presión", "Peso: 59.0 kg", "Altura: 1.8 m"]
info_Snorlax = ["Tipo: Normal",
                "Habilidad: Sebo-Inmunidad", "Peso: 460.0 kg", "Altura: 2.1 m"]
info_Articuno = ["Tipo: Hielo-Volador",
                 "Habilidad: Presión", "Peso: 55.4 kg", "Altura: 1.7 m"]
info_Zapdos = ["Tipo: Electrico-Volador",
               "Habilidad: Presión", "Peso: 52.6 kg", "Altura: 1.6 m"]
info_Moltres = ["Tipo: Fuego-Volador",
                "Habilidad: Presión", "Peso: 60.0 kg", "Altura: 2.0 m"]
info_Dratini = ["Tipo: Dragon", "Habilidad: Mudar",
                "Peso: 3.3 kg", "Altura: 1.8 m"]
info_Dragonair = ["Tipo: Dragon", "Habilidad: Mudar",
                  "Peso: 16.5 kg", "Altura: 4.0 m"]
info_Dragonite = ["Tipo: Dragon-Volador",
                  "Habilidad: Fuerza Mental", "Peso: 210.0 kg", "Altura: 2.2 m"]
info_Mewtwo = ["Tipo: Psiquico", "Habilidad: Presion",
               "Peso: 122.0 kg", "Altura: 2.0 m"]
info_Mew = ["Tipo: Psiquico", "Habilidad: Sincronia",
            "Peso: 4.0 kg", "Altura: 0.4 m"]


Pokemons = {
    "Bulbasaur": info_bulbasaur,
    "Ivysaur": info_Ivysaur,
    "Venusaur": info_Venusaur,
    "Charmander": info_Charmander,
    "Charmeleon": info_Charmeleon,
    "Charizard": info_Charizard,
    "Squirtle": info_Squirtle,
    "Wartortle": info_Wartortle,
    "Blastoise": info_Blastoise,
    "Caterpie": info_Caterpie,
    "Metapod": info_Metapod,
    "Butterfree": info_Butterfree,
    "Weedle": info_Weedle,
    "Kakuna": info_Kakuna,
    "Beedrill": info_Beedrill,
    "Pidgey": info_Pidgey,
    "Pidgeotto": info_Pidgeotto,
    "Pidgeot": info_Pidgeot,
    "Rattata": info_Rattata,
    "Raticate": info_Raticate,
    "Spearow": info_Spearow,
    "Fearow": info_Fearow,
    "Ekans": info_EKans,
    "Arbok": info_Arbok,
    "Pikachu": info_Pikachu,
    "Raichu": info_Raichu,
    "Sandshrew": info_Sandshrew,
    "Sandslash": info_Sandslash,
    "NidoranF": info_Nidoran_F,
    "Nidorina": info_Nidorina,
    "Nidoqueen": info_Nidoqueen,
    "NidoranM": info_Nidoran_M,
    "Nidorino": info_Nidorino,
    "Nidoking": info_Nidoking,
    "Clefairy": info_Clefairy,
    "Clefable": info_Clefable,
    "Vulpix": info_Vulpix,
    "Ninetales": info_Ninetales,
    "Jigglypuff": info_Jigglypuff,
    "Wigglytuff": info_Wigglytuff,
    "Zubat": info_Zubat,
    "Golbat": info_Golbat,
    "Oddish": info_Oddish,
    "Gloom": info_Gloom,
    "Vileplume": info_Vileplume,
    "Paras": info_Paras,
    "Parasect": info_Parasect,
    "Venonat": info_Venonat,
    "Venomoth": info_Venomoth,
    "Diglett": info_Diglett,
    "Dugtrio": info_Dugtrio,
    "Meowth": info_Meowth,
    "Persian": info_Persian,
    "Psyduck": info_Psyduck,
    "Golduck": info_Golduck,
    "Mankey": info_Mankey,
    "Primeape": info_Primeape,
    "Growlithe": info_Growlithe,
    "Arcanine": info_Arcanine,
    "Poliwag": info_Poliwag,
    "Poliwhirl": info_Poliwhirl,
    "Poliwrath": info_Poliwrath,
    "Abra": info_Abra,
    "Kadabra": info_Kadabra,
    "Alakazam": info_Alakazam,
    "Machop": info_Machop,
    "Machoke": info_Machoke,
    "Machamp": info_Machamp,
    "Bellsprout": info_Bellsprout,
    "Weepinbell": info_Weepinbell,
    "Victreebel": info_Victreebel,
    "Tentacool": info_Tentacool,
    "Tentacruel": info_Tentacruel,
    "Geodude": info_Geodude,
    "Graveler": info_Graveler,
    "Golem": info_Golem,
    "Ponyta": info_Ponyta,
    "Rapidash": info_Rapidash,
    "Slowpoke": info_Slowpoke,
    "Slowbro": info_Slowbro,
    "Magnemite": info_Magnemite,
    "Magneton": info_Magneton,
    "Farfetchd": info_Farfetchd,
    "Doduo": info_Doduo,
    "Dodrio": info_Dodrio,
    "Seel": info_Seel,
    "Dewgong": info_Dewgong,
    "Grimer": info_Grimer,
    "Muk": info_Muk,
    "Shellder": info_Shellder,
    "Cloyster": info_Cloyster,
    "Gastly": info_Gastly,
    "Haunter": info_Haunter,
    "Gengar": info_Gengar,
    "Onix": info_Onix,
    "Drowzee": info_Drowzee,
    "Hypno": info_Hypno,
    "Krabby": info_Krabby,
    "Kingler": info_Kingler,
    "Voltorb": info_Voltorb,
    "Electrode": info_Electrode,
    "Exeggcute": info_Exeggcute,
    "Exeggutor": info_Exeggutor,
    "Cubone": info_Cubone,
    "Marowak": info_Marowak,
    "Hitmonlee": info_Hitmonlee,
    "Hitmonchan": info_Hitmonchan,
    "Lickitung": info_Lickitung,
    "Koffing": info_Koffing,
    "Weezing": info_Weezing,
    "Rhyhorn": info_Rhyhorn,
    "Rhydon": info_Rhydon,
    "Chansey": info_Chansey,
    "Tangela": info_Tangela,
    "Kangaskhan": info_Kangaskhan,
    "Horsea": info_Horsea,
    "Seadra": info_Seadra,
    "Goldeen": info_Goldeen,
    "Seaking": info_Seaking,
    "Staryu": info_Staryu,
    "Starmie": info_Starmie,
    "MrMime": info_Mr_Mime,
    "Scyther": info_Scyther,
    "Jynx": info_Jynx,
    "Electabuzz": info_Electabuzz,
    "Magmar": info_Magmar,
    "Pinsir": info_Pinsir,
    "Tauros": info_Tauros,
    "Magikarp": info_Magikarp,
    "Gyarados": info_Gyarados,
    "Lapras": info_Lapras,
    "Ditto": info_Ditto,
    "Eevee": info_Eevee,
    "Vaporeon": info_Vaporeon,
    "Jolteon": info_Jolteon,
    "Flareon": info_Flareon,
    "Porygon": info_Porygon,
    "Omanyte": info_Omanyte,
    "Omastar": info_Omastar,
    "Kabuto": info_Kabuto,
    "Kabutops": info_Kabutops,
    "Aerodactyl": info_Aerodactyl,
    "Snorlax": info_Snorlax,
    "Articuno": info_Articuno,
    "Zapdos": info_Zapdos,
    "Moltres": info_Moltres,
    "Dratini": info_Dratini,
    "Dragonair": info_Dragonair,
    "Dragonite": info_Dragonite,
    "Mewtwo": info_Mewtwo,
    "Mew": info_Mew,
}