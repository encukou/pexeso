import pexeso
def test_slovo_podle_indexu():
	
	assert pexeso.slovo_podle_indexu(1,"cesky") == "Kolečko" # assert zkontroluje, jestli je to v zavorce true. Kdyz napisu py.test "nazev programu" zkuntroluje asserty u funkci, ktere zacinaji test
	assert pexeso.slovo_podle_indexu(2,"anglicky") == "Smile"
	
def test_vyber_karty():
	stav = [[(0,"cesky"),(0,"anglicky"),(1,"cesky"),(1,"anglicky")],
			[(2,"cesky"),(2,"anglicky"),(3,"cesky"),(3,"anglicky")],
			[(4,"cesky"),(4,"anglicky"),(5,"cesky"),(5,"anglicky")],
			[(6,"cesky"),(6,"anglicky"),(7,"cesky"),(7,"anglicky")],
	]
	assert pexeso.vyber_kartu(stav,0,0) == (0,"cesky") # chova se jako return a print = vyhodi vyjimku, kdyz to neplati
	assert pexeso.vyber_kartu(stav,0,1) == (0,"anglicky")
	assert pexeso.vyber_kartu(stav,2,3) == (5,"anglicky")
	assert pexeso.vyber_kartu(stav,3,3) == (7,"anglicky")
	
def test_zamichani():
	stav = pexeso.zamichej_karty()
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
	assert pexeso.zamichej_karty() != pexeso.zamichej_karty()