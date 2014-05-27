import pprint
from random import shuffle
import os.path

slova = []
cesta = os.path.join(os.path.dirname(__file__), 'slova.txt') # dirname najde jmeno adresare, kde je soubor zatim (slova), join vlozi slova za nazev te cesty
with open (cesta) as soubor:
	for radek in soubor:
		if radek.strip():
			slova.append(radek.split())
		


def slovo_podle_indexu(cislo, jazyk):
	if jazyk == "cesky":
		index = 0
	elif jazyk == "anglicky":
		index = 1
	else:
		raise ValueError(jazyk) # resi, kdyz se zada spatny jazyk
	return (slova[cislo][index])
	
print (slovo_podle_indexu(3,"cesky"))


def vyber_kartu(seznam,radek,sloupec): # kdyz zavolam s argumentem(stav,0,0), vrati (0,"cesky")
		return seznam[radek][sloupec]
		


def zamichej_karty(): # funkce shuffle v modulu random zamicha seznam
	seznam_karet = []
	seznam_zamichanych_karet = []
	
	for cislo in range(8):
		for pismeno in "cesky", "anglicky":
			prvek = (cislo,pismeno)
			seznam_karet.append(prvek)
	shuffle(seznam_karet)
	for neco in range(4):
		index = neco * 4
		seznam_zamichanych_karet.append(seznam_karet[index:index+4])		
	return (seznam_zamichanych_karet)
pprint.pprint (zamichej_karty())	

# funkce vs. metoda: metodu volam na objektu = napisu seznam.append, u funkce vkladam objekt jako argument - pisu shuffle(seznam_karet)	
		
	


		
	