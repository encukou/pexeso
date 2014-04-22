import pprint
from random import shuffle

slova = []

with open ('slova.txt') as soubor:
	for radek in soubor:
		if radek.strip():
			slova.append(radek.split())
		
pprint.pprint(slova)

def slovo_podle_indexu(cislo, jazyk):
	if jazyk == "cesky":
		index = 0
	elif jazyk == "anglicky":
		index = 1
	else:
		raise ValueError(jazyk) # resi, kdyz se zada spatny jazyk
	return (slova[cislo][index])
	
print (slovo_podle_indexu(3,"cesky"))

def test_slovo_podle_indexu():
	print (slova)
	assert slovo_podle_indexu(1,"cesky") == "Kolečko" # assert zkontroluje, jestli je to v zavorce true. Kdyz napisu py.test "nazev programu" zkuntroluje asserty u funkci, ktere zacinaji test
	assert slovo_podle_indexu(2,"anglicky") == "Smile"
	
def test_vyber_karty():
	stav = [[(0,"cesky"),(0,"anglicky"),(1,"cesky"),(1,"anglicky")],
			[(2,"cesky"),(2,"anglicky"),(3,"cesky"),(3,"anglicky")],
			[(4,"cesky"),(4,"anglicky"),(5,"cesky"),(5,"anglicky")],
			[(6,"cesky"),(6,"anglicky"),(7,"cesky"),(7,"anglicky")],
	]
	assert vyber_kartu(stav,0,0) == (0,"cesky") # chova se jako return a print = vyhodi vyjimku, kdyz to neplati
	assert vyber_kartu(stav,0,1) == (0,"anglicky")
	assert vyber_kartu(stav,2,3) == (5,"anglicky")
	assert vyber_kartu(stav,3,3) == (7,"anglicky")

def vyber_kartu(seznam,radek,sloupec): # kdyz zavolam s argumentem(stav,0,0), vrati (0,"cesky")
		return seznam[radek][sloupec]
		
def test_zamichani():
	stav = zamichej_karty()
	assert len(stav) == 4
	prvky = []
	for radek in stav:
		assert len(radek) == 4
		prvky += radek
	for cislo in range(8):
		for pismeno in "cesky", "anglicky":
			prvek = cislo, pismeno
			assert prvky.count(prvek)  == 1 # metoda count na seznamu vrati pocet prvku. radek zkontroluje, jestli je kazda kombinace pismena a cisla jenom jednou

def test_nahodneho_zamichani():
	assert zamichej_karty() != zamichej_karty()

def zamichej_karty(): # funkce shuffle v modulu random zam9ch8 seznam
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
zamichej_karty()	

# funkce vs. metoda: metodu volam na objektu = napisu seznam.append, u funkce pisu shuffle(seznam_karet)	
		
	


		
	