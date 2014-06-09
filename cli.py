import sys

import pexeso

def hraj(cesta):
    try:
        hra = pexeso.nacti_hru_ze_souboru(cesta)
    except FileNotFoundError:
        hra = {'stav': pexeso.zamichej_karty(), 'aktivni_karta': None}
    pexeso.vypis_stav(hra['stav'])
    radek = int(input('Řádek? ')) - 1
    sloupec = int(input('Sloupec? ')) - 1
    pexeso.udelej_tah(hra, radek, sloupec)
    pexeso.vypis_stav(hra['stav'])
    pexeso.uloz_hru_do_souboru(hra, cesta)


if __name__ == '__main__':
    hraj(sys.argv[1])
