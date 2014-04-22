import pprint

slova = []

with open ('slova.txt') as soubor:
	for radek in soubor:
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
	assert slovo_podle_indexu(1,"cesky") == "Kolečko" # assert zkontroluje, jestli je to v zavorce true. Kdyz napisu py.test "nazev programu" zkuntroluje asserty u funkci, ktere zacinaji test
	assert slovo_podle_indexu(2,"anglicky") == "Smile"


		
	