import random
import pprint
import os.path

slova = []

# Najdeme cestu k datovému souboru
# Proměnnou __file__ Python automaticky nastaví na cestu k aktuálnímu programu
#   (souboru .py)
# Funkce os.path.dirname vrátí jméno adresáře, ve kterém se nachází daný soubor
# Funkce os.path.join spojuje jména adresářů, podadresářů a souborů
# Výsledek je, že v `cesta` bude cesta k našemu datovému souboru
cesta = os.path.join(os.path.dirname(__file__), 'slova.txt')
with open(cesta) as soubor:
    for radek in soubor:
        slova.append(radek.split())

def slovo_podle_indexu(cislo, jazyk):
    radek = slova[cislo]
    if jazyk == 'C':
        return radek[0]
    elif jazyk == 'A':
        return radek[1]
    else:
        raise ValueError(jazyk)

def vyber_kartu(stav, cislo_radku, cislo_sloupce):
    radek = stav[cislo_radku]
    prvek = radek[cislo_sloupce]
    return prvek

def zamichej_karty():
    karty = []
    for cislo in range(8):
        for pismeno in 'CA':
            karty.append((cislo, pismeno))
    random.shuffle(karty)
    stav = []
    for radek in range(4):
        index = radek * 4
        stav.append(karty[index:index + 4])
    return stav
