import pprint

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
	
def test_vuber_karty():
	stav = [[(0,"cesky"),(0,"anglicky"),(1,"cesky"),(1,"anglicky")],
			[(2,"cesky"),(2,"anglicky"),(3,"cesky"),(3,"anglicky")],
			[(4,"cesky"),(4,"anglicky"),(5,"cesky"),(5,"anglicky")],
			[(6,"cesky"),(6,"anglicky"),(7,"cesky"),(7,"anglicky")],
	]
	assert vyber_kartu(stav,0,0) == (0,"cesky")
	assert vyber_kartu(stav,0,1) == (0,"anglicky")
	assert vyber_kartu(stav,2,3) == (5,"anglicky")
	assert vyber_kartu(stav,3,3) == (7,"anglicky")


		
	