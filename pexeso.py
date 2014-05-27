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

pprint.pprint(slova)

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


def test_slovo_podle_indexu():
    assert slovo_podle_indexu(1, 'C') == 'Kolečko'
    assert slovo_podle_indexu(2, 'A') == 'Smile'

def test_vyberu_karty():
    stav = [
        [(0, 'C'), (0, 'A'), (1, 'C'), (1, 'A')],
        [(2, 'C'), (2, 'A'), (3, 'C'), (3, 'A')],
        [(4, 'C'), (4, 'A'), (5, 'C'), (5, 'A')],
        [(6, 'C'), (6, 'A'), (7, 'C'), (7, 'A')],
    ]
    assert vyber_kartu(stav, 0, 0) == (0, 'C')
    assert vyber_kartu(stav, 0, 1) == (0, 'A')
    assert vyber_kartu(stav, 2, 3) == (5, 'A')
    assert vyber_kartu(stav, 3, 3) == (7, 'A')

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

def test_zamichani():
    stav = zamichej_karty()
    assert len(stav) == 4
    prvky = []
    for radek in stav:
        assert len(radek) == 4
        prvky += radek
    for cislo in range(8):
        for pismeno in 'C', 'A':
            prvek = cislo, pismeno
            assert prvky.count(prvek) == 1

def test_nahodneho_zamichani():
    # (Tehnle test v jednom z 20922789888000
    # případů neprojde)
    assert zamichej_karty() != zamichej_karty()
