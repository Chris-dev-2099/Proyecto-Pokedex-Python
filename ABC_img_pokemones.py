from tkinter import *
import tkinter
import os
from PIL import ImageTk, Image

ruta_imagen_Bulbasaur = "Bulbasaur.png"
ruta_imagen_Ivysaur = "Ivysaur.png"
ruta_imagen_Venusaur = "Venusaur.png"
ruta_imagen_Charmander = "Charmander.png"
ruta_imagen_Charmeleon = "Charmeleon.png"
ruta_imagen_Charizard = "Charizard.png"
ruta_imagen_Squirtle = "Squirtle.png"
ruta_imagen_Wartortle = "Wartortle.png"
ruta_imagen_Blastoise = "Blastoise.png"
ruta_imagen_Caterpie = "Caterpie.png"
ruta_imagen_Metapod = "Metapod.png"
ruta_imagen_Butterfree = "Butterfree.png"
ruta_imagen_Weedle = "Weedle.png"
ruta_imagen_Kakuna = "Kakuna.png"
ruta_imagen_Beedrill = "Beedrill.png"
ruta_imagen_Pidgey = "Pidgey.png"
ruta_imagen_Pidgeotto = "Pidgeotto.png"
ruta_imagen_Pidgeot = "Pidgeot.png"
ruta_imagen_Rattata = "Rattata.png"
ruta_imagen_Raticate = "Raticate.png"
ruta_imagen_Spearow = "Spearow.png"
ruta_imagen_Fearow = "Fearow.png"
ruta_imagen_Ekans = "Ekans.png"
ruta_imagen_Arbok = "Arbok.png"
ruta_imagen_Pikachu = "Pikachu.png"
ruta_imagen_Raichu = "Raichu.png"
ruta_imagen_Sandshrew = "Sandshrew.png"
ruta_imagen_Sandslash = "Sandslash.png"
ruta_imagen_Nidoran = "NidoranF.png"
ruta_imagen_Nidorina = "Nidorina.png"
ruta_imagen_Nidoqueen = "Nidoqueen.png"
ruta_imagen_NidoranM= "NidoranM.png"
ruta_imagen_Nidorino = "Nidorino.png"
ruta_imagen_Nidoking = "Nidoking.png"
ruta_imagen_Clefairy = "Clefairy.png"
ruta_imagen_Clefable = "Clefable.png"
ruta_imagen_Vulpix = "Vulpix.png"
ruta_imagen_Ninetales = "Ninetales.png"
ruta_imagen_Jigglypuff = "Jigglypuff.png"
ruta_imagen_Wigglytuff = "Wigglytuff.png"
ruta_imagen_Zubat = "Zubat.png"
ruta_imagen_Golbat = "Golbat.png"
ruta_imagen_Oddish = "Oddish.png"
ruta_imagen_Gloom = "Gloom.png"
ruta_imagen_Vileplume = "Vileplume.png"
ruta_imagen_Paras = "Paras.png"
ruta_imagen_Parasect = "Parasect.png"
ruta_imagen_Venonat = "Venonat.png"
ruta_imagen_Venomoth = "Venomoth.png"
ruta_imagen_Diglett = "Diglett.png"
ruta_imagen_Dugtrio = "Dugtrio.png"
ruta_imagen_Meowth = "Meowth.png"
ruta_imagen_Persian = "Persian.png"
ruta_imagen_Psyduck = "Psyduck.png"
ruta_imagen_Golduck = "Golduck.png"
ruta_imagen_Mankey = "Mankey.png"
ruta_imagen_Primeape = "Primeape.png"
ruta_imagen_Growlithe = "Growlithe.png"
ruta_imagen_Arcanine = "Arcanine.png"
ruta_imagen_Poliwag = "Poliwag.png"
ruta_imagen_Poliwhirl = "Poliwhirl.png"
ruta_imagen_Poliwrath = "Poliwrath.png"
ruta_imagen_Abra = "Abra.png"
ruta_imagen_Kadabra = "Kadabra.png"
ruta_imagen_Alakazam = "Alakazam.png"
ruta_imagen_Machop = "Machop.png"
ruta_imagen_Machoke = "Machoke.png"
ruta_imagen_Machamp = "Machamp.png"
ruta_imagen_Bellsprout = "Bellsprout.png"
ruta_imagen_Weepinbell = "Weepinbell.png"
ruta_imagen_Victreebel = "Victreebel.png"
ruta_imagen_Tentacool = "Tentacool.png"
ruta_imagen_Tentacruel = "Tentacruel.png"
ruta_imagen_Geodude = "Geodude.png"
ruta_imagen_Graveler = "Graveler.png"
ruta_imagen_Golem = "Golem.png"
ruta_imagen_Ponyta = "Ponyta.png"
ruta_imagen_Rapidash = "Rapidash.png"
ruta_imagen_Slowpoke = "Slowpoke.png"
ruta_imagen_Slowbro = "Slowbro.png"
ruta_imagen_Magnemite = "Magnemite.png"
ruta_imagen_Magneton = "Magneton.png"
ruta_imagen_Farfetchd = "Farfetchd.png"
ruta_imagen_Doduo = "Doduo.png"
ruta_imagen_Dodrio = "Dodrio.png"
ruta_imagen_Seel = "Seel.png"
ruta_imagen_Dewgong = "Dewgong.png"
ruta_imagen_Grimer = "Grimer.png"
ruta_imagen_Muk = "Muk.png"
ruta_imagen_Shellder = "Shellder.png"
ruta_imagen_Cloyster = "Cloyster.png"
ruta_imagen_Gastly = "Gastly.png"
ruta_imagen_Haunter = "Haunter.png"
ruta_imagen_Gengar = "Gengar.png"
ruta_imagen_Onix = "Onix.png"
ruta_imagen_Drowzee = "Drowzee.png"
ruta_imagen_Hypno = "Hypno.png"
ruta_imagen_Krabby = "Krabby.png"
ruta_imagen_Kingler = "Kingler.png"
ruta_imagen_Voltorb = "Voltorb.png"
ruta_imagen_Electrode = "Electrode.png"
ruta_imagen_Exeggcute = "Exeggcute.png"
ruta_imagen_Exeggutor = "Exeggutor.png"
ruta_imagen_Cubone = "Cubone.png"
ruta_imagen_Marowak = "Marowak.png"
ruta_imagen_Hitmonlee = "Hitmonlee.png"
ruta_imagen_Hitmonchan = "Hitmonchan.png"
ruta_imagen_Lickitung = "Lickitung.png"
ruta_imagen_Koffing = "Koffing.png"
ruta_imagen_Weezing = "Weezing.png"
ruta_imagen_Rhyhorn = "Rhyhorn.png"
ruta_imagen_Rhydon = "Rhydon.png"
ruta_imagen_Chansey = "Chansey.png"
ruta_imagen_Tangela = "Tangela.png"
ruta_imagen_Kangaskhan = "Kangaskhan.png"
ruta_imagen_Horsea = "Horsea.png"
ruta_imagen_Seadra = "Seadra.png"
ruta_imagen_Goldeen = "Goldeen.png"
ruta_imagen_Seaking = "Seaking.png"
ruta_imagen_Staryu = "Staryu.png"
ruta_imagen_Starmie = "Starmie.png"
ruta_imagen_Mr_Mime = "MrMime.png"
ruta_imagen_Scyther = "Scyther.png"
ruta_imagen_Jynx = "Jynx.png"
ruta_imagen_Electabuzz = "Electabuzz.png"
ruta_imagen_Magmar = "Magmar.png"
ruta_imagen_Pinsir = "Pinsir.png"
ruta_imagen_Tauros = "Tauros.png"
ruta_imagen_Magikarp = "Magikarp.png"
ruta_imagen_Gyarados = "Gyarados.png"
ruta_imagen_Lapras = "Lapras.png"
ruta_imagen_Ditto = "Ditto.png"
ruta_imagen_Eevee = "Eevee.png"
ruta_imagen_Vaporeon = "Vaporeon.png"
ruta_imagen_Jolteon = "Jolteon.png"
ruta_imagen_Flareon = "Flareon.png"
ruta_imagen_Porygon = "Porygon.png"
ruta_imagen_Omanyte = "Omanyte.png"
ruta_imagen_Omastar = "Omastar.png"
ruta_imagen_Kabuto = "Kabuto.png"
ruta_imagen_Kabutops = "Kabutops.png"
ruta_imagen_Aerodactyl = "Aerodactyl.png"
ruta_imagen_Snorlax = "Snorlax.png"
ruta_imagen_Articuno = "Articuno.png"
ruta_imagen_Zapdos = "Zapdos.png"
ruta_imagen_Moltres = "Moltres.png"
ruta_imagen_Dratini = "Dratini.png"
ruta_imagen_Dragonair = "Dragonair.png"
ruta_imagen_Dragonite = "Dragonite.png"
ruta_imagen_Mewtwo = "Mewtwo.png"
ruta_imagen_Mew = "Mew.png"

from PIL import Image

imagen_Bulbasaur = Image.open(ruta_imagen_Bulbasaur)
imagen_Ivysaur = Image.open(ruta_imagen_Ivysaur)
imagen_Venusaur = Image.open(ruta_imagen_Venusaur)
imagen_Charmander = Image.open(ruta_imagen_Charmander)
imagen_Charmeleon = Image.open(ruta_imagen_Charmeleon)
imagen_Charizard = Image.open(ruta_imagen_Charizard)
imagen_Squirtle = Image.open(ruta_imagen_Squirtle)
imagen_Wartortle = Image.open(ruta_imagen_Wartortle)
imagen_Blastoise = Image.open(ruta_imagen_Blastoise)
imagen_Caterpie = Image.open(ruta_imagen_Caterpie)
imagen_Metapod = Image.open(ruta_imagen_Metapod)
imagen_Butterfree = Image.open(ruta_imagen_Butterfree)
imagen_Weedle = Image.open(ruta_imagen_Weedle)
imagen_Kakuna = Image.open(ruta_imagen_Kakuna)
imagen_Beedrill = Image.open(ruta_imagen_Beedrill)
imagen_Pidgey = Image.open(ruta_imagen_Pidgey)
imagen_Pidgeotto = Image.open(ruta_imagen_Pidgeotto)
imagen_Pidgeot = Image.open(ruta_imagen_Pidgeot)
imagen_Rattata = Image.open(ruta_imagen_Rattata)
imagen_Raticate = Image.open(ruta_imagen_Raticate)
imagen_Spearow = Image.open(ruta_imagen_Spearow)
imagen_Fearow = Image.open(ruta_imagen_Fearow)
imagen_Ekans = Image.open(ruta_imagen_Ekans)
imagen_Arbok = Image.open(ruta_imagen_Arbok)
imagen_Pikachu = Image.open(ruta_imagen_Pikachu)
imagen_Raichu = Image.open(ruta_imagen_Raichu)
imagen_Sandshrew = Image.open(ruta_imagen_Sandshrew)
imagen_Sandslash = Image.open(ruta_imagen_Sandslash)
imagen_Nidoran = Image.open(ruta_imagen_Nidoran)
imagen_Nidorina = Image.open(ruta_imagen_Nidorina)
imagen_Nidoqueen = Image.open(ruta_imagen_Nidoqueen)
imagen_NidoranM= Image.open(ruta_imagen_NidoranM)
imagen_Nidorino = Image.open(ruta_imagen_Nidorino)
imagen_Nidoking = Image.open(ruta_imagen_Nidoking)
imagen_Clefairy = Image.open(ruta_imagen_Clefairy)
imagen_Clefable = Image.open(ruta_imagen_Clefable)
imagen_Vulpix = Image.open(ruta_imagen_Vulpix)
imagen_Ninetales = Image.open(ruta_imagen_Ninetales)
imagen_Jigglypuff = Image.open(ruta_imagen_Jigglypuff)
imagen_Wigglytuff = Image.open(ruta_imagen_Wigglytuff)
imagen_Zubat = Image.open(ruta_imagen_Zubat)
imagen_Golbat = Image.open(ruta_imagen_Golbat)
imagen_Oddish = Image.open(ruta_imagen_Oddish)
imagen_Gloom = Image.open(ruta_imagen_Gloom)
imagen_Vileplume = Image.open(ruta_imagen_Vileplume)
imagen_Paras = Image.open(ruta_imagen_Paras)
imagen_Parasect = Image.open(ruta_imagen_Parasect)
imagen_Venonat = Image.open(ruta_imagen_Venonat)
imagen_Venomoth = Image.open(ruta_imagen_Venomoth)
imagen_Diglett = Image.open(ruta_imagen_Diglett)
imagen_Dugtrio = Image.open(ruta_imagen_Dugtrio)
imagen_Meowth = Image.open(ruta_imagen_Meowth)
imagen_Persian = Image.open(ruta_imagen_Persian)
imagen_Psyduck = Image.open(ruta_imagen_Psyduck)
imagen_Golduck = Image.open(ruta_imagen_Golduck)
imagen_Mankey = Image.open(ruta_imagen_Mankey)
imagen_Primeape = Image.open(ruta_imagen_Primeape)
imagen_Growlithe = Image.open(ruta_imagen_Growlithe)
imagen_Arcanine = Image.open(ruta_imagen_Arcanine)
imagen_Poliwag = Image.open(ruta_imagen_Poliwag)
imagen_Poliwhirl = Image.open(ruta_imagen_Poliwhirl)
imagen_Poliwrath = Image.open(ruta_imagen_Poliwrath)
imagen_Abra = Image.open(ruta_imagen_Abra)
imagen_Kadabra = Image.open(ruta_imagen_Kadabra)
imagen_Alakazam = Image.open(ruta_imagen_Alakazam)
imagen_Machop = Image.open(ruta_imagen_Machop)
imagen_Machoke = Image.open(ruta_imagen_Machoke)
imagen_Machamp = Image.open(ruta_imagen_Machamp)
imagen_Bellsprout = Image.open(ruta_imagen_Bellsprout)
imagen_Weepinbell = Image.open(ruta_imagen_Weepinbell)
imagen_Victreebel = Image.open(ruta_imagen_Victreebel)
imagen_Tentacool = Image.open(ruta_imagen_Tentacool)
imagen_Tentacruel = Image.open(ruta_imagen_Tentacruel)
imagen_Geodude = Image.open(ruta_imagen_Geodude)
imagen_Graveler = Image.open(ruta_imagen_Graveler)
imagen_Golem = Image.open(ruta_imagen_Golem)
imagen_Ponyta = Image.open(ruta_imagen_Ponyta)
imagen_Rapidash = Image.open(ruta_imagen_Rapidash)
imagen_Slowpoke = Image.open(ruta_imagen_Slowpoke)
imagen_Slowbro = Image.open(ruta_imagen_Slowbro)
imagen_Magnemite = Image.open(ruta_imagen_Magnemite)
imagen_Magneton = Image.open(ruta_imagen_Magneton)
imagen_Farfetchd = Image.open(ruta_imagen_Farfetchd)
imagen_Doduo = Image.open(ruta_imagen_Doduo)
imagen_Dodrio = Image.open(ruta_imagen_Dodrio)
imagen_Seel = Image.open(ruta_imagen_Seel)
imagen_Dewgong = Image.open(ruta_imagen_Dewgong)
imagen_Grimer = Image.open(ruta_imagen_Grimer)
imagen_Muk = Image.open(ruta_imagen_Muk)
imagen_Shellder = Image.open(ruta_imagen_Shellder)
imagen_Cloyster = Image.open(ruta_imagen_Cloyster)
imagen_Gastly = Image.open(ruta_imagen_Gastly)
imagen_Haunter = Image.open(ruta_imagen_Haunter)
imagen_Gengar = Image.open(ruta_imagen_Gengar)
imagen_Onix = Image.open(ruta_imagen_Onix)
imagen_Drowzee = Image.open(ruta_imagen_Drowzee)
imagen_Hypno = Image.open(ruta_imagen_Hypno)
imagen_Krabby = Image.open(ruta_imagen_Krabby)
imagen_Kingler = Image.open(ruta_imagen_Kingler)
imagen_Voltorb = Image.open(ruta_imagen_Voltorb)
imagen_Electrode = Image.open(ruta_imagen_Electrode)
imagen_Exeggcute = Image.open(ruta_imagen_Exeggcute)
imagen_Exeggutor = Image.open(ruta_imagen_Exeggutor)
imagen_Cubone = Image.open(ruta_imagen_Cubone)
imagen_Marowak = Image.open(ruta_imagen_Marowak)
imagen_Hitmonlee = Image.open(ruta_imagen_Hitmonlee)
imagen_Hitmonchan = Image.open(ruta_imagen_Hitmonchan)
imagen_Lickitung = Image.open(ruta_imagen_Lickitung)
imagen_Koffing = Image.open(ruta_imagen_Koffing)
imagen_Weezing = Image.open(ruta_imagen_Weezing)
imagen_Rhyhorn = Image.open(ruta_imagen_Rhyhorn)
imagen_Rhydon = Image.open(ruta_imagen_Rhydon)
imagen_Chansey = Image.open(ruta_imagen_Chansey)
imagen_Tangela = Image.open(ruta_imagen_Tangela)
imagen_Kangaskhan = Image.open(ruta_imagen_Kangaskhan)
imagen_Horsea = Image.open(ruta_imagen_Horsea)
imagen_Seadra = Image.open(ruta_imagen_Seadra)
imagen_Goldeen = Image.open(ruta_imagen_Goldeen)
imagen_Seaking = Image.open(ruta_imagen_Seaking)
imagen_Staryu = Image.open(ruta_imagen_Staryu)
imagen_Starmie = Image.open(ruta_imagen_Starmie)
imagen_Mr_Mime = Image.open(ruta_imagen_Mr_Mime)
imagen_Scyther = Image.open(ruta_imagen_Scyther)
imagen_Jynx = Image.open(ruta_imagen_Jynx)
imagen_Electabuzz = Image.open(ruta_imagen_Electabuzz)
imagen_Magmar = Image.open(ruta_imagen_Magmar)
imagen_Pinsir = Image.open(ruta_imagen_Pinsir)
imagen_Tauros = Image.open(ruta_imagen_Tauros)
imagen_Magikarp = Image.open(ruta_imagen_Magikarp)
imagen_Gyarados = Image.open(ruta_imagen_Gyarados)
imagen_Lapras = Image.open(ruta_imagen_Lapras)
imagen_Ditto = Image.open(ruta_imagen_Ditto)
imagen_Eevee = Image.open(ruta_imagen_Eevee)
imagen_Vaporeon = Image.open(ruta_imagen_Vaporeon)
imagen_Jolteon = Image.open(ruta_imagen_Jolteon)
imagen_Flareon = Image.open(ruta_imagen_Flareon)
imagen_Porygon = Image.open(ruta_imagen_Porygon)
imagen_Omanyte = Image.open(ruta_imagen_Omanyte)
imagen_Omastar = Image.open(ruta_imagen_Omastar)
imagen_Kabuto = Image.open(ruta_imagen_Kabuto)
imagen_Kabutops = Image.open(ruta_imagen_Kabutops)
imagen_Aerodactyl = Image.open(ruta_imagen_Aerodactyl)
imagen_Snorlax = Image.open(ruta_imagen_Snorlax)
imagen_Articuno = Image.open(ruta_imagen_Articuno)
imagen_Zapdos = Image.open(ruta_imagen_Zapdos)
imagen_Moltres = Image.open(ruta_imagen_Moltres)
imagen_Dratini = Image.open(ruta_imagen_Dratini)
imagen_Dragonair = Image.open(ruta_imagen_Dragonair)
imagen_Dragonite = Image.open(ruta_imagen_Dragonite)
imagen_Mewtwo = Image.open(ruta_imagen_Mewtwo)
imagen_Mew = Image.open(ruta_imagen_Mew)

Pokemons_img = {
    "Bulbasaur": imagen_Bulbasaur,
    "Ivysaur": imagen_Ivysaur,
    "Venusaur": imagen_Venusaur,
    "Charmander": imagen_Charmander,
    "Charmeleon": imagen_Charmeleon,
    "Charizard": imagen_Charizard,
    "Squirtle": imagen_Squirtle,
    "Wartortle": imagen_Wartortle,
    "Blastoise": imagen_Blastoise,
    "Caterpie": imagen_Caterpie,
    "Metapod": imagen_Metapod,
    "Butterfree": imagen_Butterfree,
    "Weedle": imagen_Weedle,
    "Kakuna": imagen_Kakuna,
    "Beedrill": imagen_Beedrill,
    "Pidgey": imagen_Pidgey,
    "Pidgeotto": imagen_Pidgeotto,
    "Pidgeot": imagen_Pidgeot,
    "Rattata": imagen_Rattata,
    "Raticate": imagen_Raticate,
    "Spearow": imagen_Spearow,
    "Fearow": imagen_Fearow,
    "Ekans": imagen_Ekans,
    "Arbok": imagen_Arbok,
    "Pikachu": imagen_Pikachu,
    "Raichu": imagen_Raichu,
    "Sandshrew": imagen_Sandshrew,
    "Sandslash": imagen_Sandslash,
    "NidoranF": imagen_Nidoran,
    "Nidorina": imagen_Nidorina,
    "Nidoqueen": imagen_Nidoqueen,
    "NidoranM": imagen_NidoranM,
    "Nidorino": imagen_Nidorino,
    "Nidoking": imagen_Nidoking,
    "Clefairy": imagen_Clefairy,
    "Clefable": imagen_Clefable,
    "Vulpix": imagen_Vulpix,
    "Ninetales": imagen_Ninetales,
    "Jigglypuff": imagen_Jigglypuff,
    "Wigglytuff": imagen_Wigglytuff,
    "Zubat": imagen_Zubat,
    "Golbat": imagen_Golbat,
    "Oddish": imagen_Oddish,
    "Gloom": imagen_Gloom,
    "Vileplume": imagen_Vileplume,
    "Paras": imagen_Paras,
    "Parasect": imagen_Parasect,
    "Venonat": imagen_Venonat,
    "Venomoth": imagen_Venomoth,
    "Diglett": imagen_Diglett,
    "Dugtrio": imagen_Dugtrio,
    "Meowth": imagen_Meowth,
    "Persian": imagen_Persian,
    "Psyduck": imagen_Psyduck,
    "Golduck": imagen_Golduck,
    "Mankey": imagen_Mankey,
    "Primeape": imagen_Primeape,
    "Growlithe": imagen_Growlithe,
    "Arcanine": imagen_Arcanine,
    "Poliwag": imagen_Poliwag,
    "Poliwhirl": imagen_Poliwhirl,
    "Poliwrath": imagen_Poliwrath,
    "Abra": imagen_Abra,
    "Kadabra": imagen_Kadabra,
    "Alakazam": imagen_Alakazam,
    "Machop": imagen_Machop,
    "Machoke": imagen_Machoke,
    "Machamp": imagen_Machamp,
    "Bellsprout": imagen_Bellsprout,
    "Weepinbell": imagen_Weepinbell,
    "Victreebel": imagen_Victreebel,
    "Tentacool": imagen_Tentacool,
    "Tentacruel": imagen_Tentacruel,
    "Geodude": imagen_Geodude,
    "Graveler": imagen_Graveler,
    "Golem": imagen_Golem,
    "Ponyta": imagen_Ponyta,
    "Rapidash": imagen_Rapidash,
    "Slowpoke": imagen_Slowpoke,
    "Slowbro": imagen_Slowbro,
    "Magnemite": imagen_Magnemite,
    "Magneton": imagen_Magneton,
    "Farfetchd": imagen_Farfetchd,
    "Doduo": imagen_Doduo,
    "Dodrio": imagen_Dodrio,
    "Seel": imagen_Seel,
    "Dewgong": imagen_Dewgong,
    "Grimer": imagen_Grimer,
    "Muk": imagen_Muk,
    "Shellder": imagen_Shellder,
    "Cloyster": imagen_Cloyster,
    "Gastly": imagen_Gastly,
    "Haunter": imagen_Haunter,
    "Gengar": imagen_Gengar,
    "Onix": imagen_Onix,
    "Drowzee": imagen_Drowzee,
    "Hypno": imagen_Hypno,
    "Krabby": imagen_Krabby,
    "Kingler": imagen_Kingler,
    "Voltorb": imagen_Voltorb,
    "Electrode": imagen_Electrode,
    "Exeggcute": imagen_Exeggcute,
    "Exeggutor": imagen_Exeggutor,
    "Cubone": imagen_Cubone,
    "Marowak": imagen_Marowak,
    "Hitmonlee": imagen_Hitmonlee,
    "Hitmonchan": imagen_Hitmonchan,
    "Lickitung": imagen_Lickitung,
    "Koffing": imagen_Koffing,
    "Weezing": imagen_Weezing,
    "Rhyhorn": imagen_Rhyhorn,
    "Rhydon": imagen_Rhydon,
    "Chansey": imagen_Chansey,
    "Tangela": imagen_Tangela,
    "Kangaskhan": imagen_Kangaskhan,
    "Horsea": imagen_Horsea,
    "Seadra": imagen_Seadra,
    "Goldeen": imagen_Goldeen,
    "Seaking": imagen_Seaking,
    "Staryu": imagen_Staryu,
    "Starmie": imagen_Starmie,
    "MrMime": imagen_Mr_Mime,
    "Scyther": imagen_Scyther,
    "Jynx": imagen_Jynx,
    "Electabuzz": imagen_Electabuzz,
    "Magmar": imagen_Magmar,
    "Pinsir": imagen_Pinsir,
    "Tauros": imagen_Tauros,
    "Magikarp": imagen_Magikarp,
    "Gyarados": imagen_Gyarados,
    "Lapras": imagen_Lapras,
    "Ditto": imagen_Ditto,
    "Eevee": imagen_Eevee,
    "Vaporeon": imagen_Vaporeon,
    "Jolteon": imagen_Jolteon,
    "Flareon": imagen_Flareon,
    "Porygon": imagen_Porygon,
    "Omanyte": imagen_Omanyte,
    "Omastar": imagen_Omastar,
    "Kabuto": imagen_Kabuto,
    "Kabutops": imagen_Kabutops,
    "Aerodactyl": imagen_Aerodactyl,
    "Snorlax": imagen_Snorlax,
    "Articuno": imagen_Articuno,
    "Zapdos": imagen_Zapdos,
    "Moltres": imagen_Moltres,
    "Dratini": imagen_Dratini,
    "Dragonair": imagen_Dragonair,
    "Dragonite": imagen_Dragonite,
    "Mewtwo": imagen_Mewtwo,
    "Mew": imagen_Mew,
}