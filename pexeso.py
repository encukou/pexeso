import pprint
from random import shuffle
import os.path

slova = []

cesta = os.path.join(os.path.dirname(__file__), 'slova.txt') # dirname najde jmeno adresare, kde je soubor zatim (slova), join vlozi slova za nazev te cesty
with open (cesta) as soubor:
	for radek in soubor:
		if radek.strip():
			slova.append(radek.split())

def zjisti_delku_nejdelsiho_slova():
	delka = 0
	for radek in slova:
		for slovo in radek:
			if len(slovo) > delka:
				delka = len(slovo)
	return delka

	
def slovo_podle_indexu(cislo, jazyk):
	if jazyk == "cesky":
		index = 0
	elif jazyk == "anglicky":
		index = 1
	else:
		raise ValueError(jazyk) # resi, kdyz se zada spatny jazyk
	return (slova[cislo][index])
	


def vyber_kartu(stav,radek,sloupec): # kdyz zavolam s argumentem(stav,0,0), vrati (0,"cesky")
		return stav[radek][sloupec]
		


def zamichej_karty(): # funkce shuffle v modulu random zamicha seznam
	seznam_karet = []
	seznam_zamichanych_karet = []
	otoceno = False
	for cislo in range(8):
		for pismeno in "cesky", "anglicky":
			prvek = (cislo,pismeno,otoceno)
			seznam_karet.append(prvek)
	shuffle(seznam_karet)
	for neco in range(4):
		index = neco * 4
		seznam_zamichanych_karet.append(seznam_karet[index:index+4])		
	return (seznam_zamichanych_karet)
print (zamichej_karty())	


def vypis_stav(seznam_karet):
	delka = zjisti_delku_nejdelsiho_slova()
	for radek in seznam_karet:
		for karta in radek:
			cislo = karta[0]
			jazyk = karta[1]
			if karta[2]:
				print (slovo_podle_indexu(cislo, jazyk).ljust(delka),end=" ") # end=" " dela v python 3.4 to same, co carka
			else:
				print (delka*"?",end=" ")
		print ()
vypis_stav(zamichej_karty())	

"""zakladni_stav = [
    [(0, 'C', False), (0, 'A', False), (1, 'C', False), (1, 'A', False)],
    [(2, 'C', False), (2, 'A', False), (3, 'C', False), (3, 'A', False)],
    [(4, 'C', False), (4, 'A', False), (5, 'C', False), (5, 'A', False)],
    [(6, 'C', False), (6, 'A', False), (7, 'C', False), (7, 'A', False)],
]

zakladni_hra = {
    'stav': zakladni_stav,
    'aktivni_karta': None,
}"""

def otoc_kartu(stav,radek,sloupec,nove_otoceni):
	""" sem se maji napsat komentare k funkci """ 
	cislo, jazyk, stare_otoceni = stav[radek][sloupec] # stav[radek][sloupec] vrati trojici, tu tuple, ve ktere mam cislo, jazyk, otoceni
	stav[radek][sloupec] = cislo, jazyk, nove_otoceni

def udelej_tah(hra, radek, sloupec):
	if  hra['aktivni_karta'] == None:
		otoc_kartu(hra['stav'],radek,sloupec,True)
		hra['aktivni_karta'] = (radek,sloupec)
	else:
		aktivni_radek, aktivni_sloupec = hra['aktivni_karta']
		nove_otoceny_obrazek = vyber_kartu(hra['stav'],radek,sloupec)[0]
		puvodni_obrazek = vyber_kartu(hra['stav'],aktivni_radek,aktivni_sloupec)[0]
		if nove_otoceny_obrazek == puvodni_obrazek:
			otoc_kartu(hra['stav'],radek,sloupec,True)
		else:
			otoc_kartu(hra['stav'],aktivni_radek,aktivni_sloupec,False)
		hra['aktivni_karta'] = None
	return hra

# funkce vs. metoda: metodu volam na objektu = napisu seznam.append, u funkce vkladam objekt jako argument - pisu shuffle(seznam_karet)	
		
	


		
	