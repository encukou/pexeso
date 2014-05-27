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
delka_nejdelsiho_slova = 0
with open(cesta) as soubor:
    for radek in soubor:
        slova.append(radek.split())

for radek in slova:
    for slovo in radek:
        if len(slovo) > delka_nejdelsiho_slova:
            delka_nejdelsiho_slova = len(slovo)


def slovo_podle_indexu(cislo, jazyk):
    """Najde v našich datech dané slovo

    např. první slovo je Sluníčko,
    >>> slovo_podle_indexu(0, 'C')
    'Sluníčko'
    >>> slovo_podle_indexu(0, 'A')
    'Sun'
    """
    radek = slova[cislo]
    if jazyk == 'C':
        return radek[0]
    elif jazyk == 'A':
        return radek[1]
    else:
        raise ValueError(jazyk)


def vyber_kartu(stav, cislo_radku, cislo_sloupce):
    """Vybere kartu ze stavu na dané pozici"""
    radek = stav[cislo_radku]
    prvek = radek[cislo_sloupce]
    return prvek


def zamichej_karty():
    """Vrátí nový zamíchaný stav"""
    karty = []
    for cislo in range(8):
        for pismeno in 'CA':
            karty.append((cislo, pismeno, False))
    random.shuffle(karty)
    stav = []
    for radek in range(4):
        index = radek * 4
        stav.append(karty[index:index + 4])
    return stav


def vypis_stav(stav):
    for radek in stav:
        for karta in radek:
            cislo, pismeno, otoceno = karta
            slovo = slovo_podle_indexu(cislo, pismeno)
            print(slovo.ljust(delka_nejdelsiho_slova), end=' ')
        print()


vypis_stav(zamichej_karty())
