import pexeso

stav = [[(0,"cesky", False),(0,"anglicky", False),(1,"cesky", False),(1,"anglicky", False)],
			[(2,"cesky",False),(2,"anglicky", False),(3,"cesky", False),(3,"anglicky", False)],
			[(4,"cesky", False),(4,"anglicky", False),(5,"cesky", False),(5,"anglicky", False)],
			[(6,"cesky", False),(6,"anglicky", False),(7,"cesky", False),(7,"anglicky", False)],
	]
	
def test_slovo_podle_indexu():
	
	assert pexeso.slovo_podle_indexu(1,"cesky") == "Kolečko" # assert zkontroluje, jestli je to v zavorce true. Kdyz napisu py.test "nazev programu" zkuntroluje asserty u funkci, ktere zacinaji test
	assert pexeso.slovo_podle_indexu(2,"anglicky") == "Smile"
	
def test_vyber_karty():
	
	assert pexeso.vyber_kartu(stav,0,0) == (0,"cesky", False) # chova se jako return a print = vyhodi vyjimku, kdyz to neplati
	assert pexeso.vyber_kartu(stav,0,1) == (0,"anglicky", False)
	assert pexeso.vyber_kartu(stav,2,3) == (5,"anglicky", False)
	assert pexeso.vyber_kartu(stav,3,3) == (7,"anglicky", False)
	
def test_zamichani():
	stav = pexeso.zamichej_karty()
	assert len(stav) == 4
	prvky = []
	for radek in stav:
		assert len(radek) == 4
		prvky += radek
	for cislo in range(8):
		for pismeno in "cesky", "anglicky":
			prvek = cislo, pismeno, False
			assert prvky.count(prvek)  == 1 # metoda count na seznamu vrati pocet prvku. radek zkontroluje, jestli je kazda kombinace pismena a cisla jenom jednou

def test_nahodneho_zamichani():
	assert pexeso.zamichej_karty() != pexeso.zamichej_karty()
	
def vytvor_zakladni_stav():
	zakladni_stav = [
    [(0, 'C', False), (0, 'A', False), (1, 'C', False), (1, 'A', False)],
    [(2, 'C', False), (2, 'A', False), (3, 'C', False), (3, 'A', False)],
    [(4, 'C', False), (4, 'A', False), (5, 'C', False), (5, 'A', False)],
    [(6, 'C', False), (6, 'A', False), (7, 'C', False), (7, 'A', False)],
	]
	return zakladni_stav

def vytvor_zakladni_hru():
	zakladni_stav = vytvor_zakladni_stav()
	zakladni_hra = {
    'stav': zakladni_stav,
    'aktivni_karta': None,
	}
	return zakladni_hra

def zkontroluj_otoceni(stav, otocene_karty):
    for radek in range(4):
        for sloupec in range(4):
            prvek = pexeso.vyber_kartu(stav, radek, sloupec)
            if (radek, sloupec) in otocene_karty:
                assert prvek[2] == True
            else:
                assert prvek[2] == False

def test_hry2():
    hra = vytvor_zakladni_hru()
    hra = pexeso.udelej_tah(hra, 1, 2)
    zkontroluj_otoceni(hra['stav'], [(1, 2)])
    assert hra['aktivni_karta'] == (1, 2)

    hra = pexeso.udelej_tah(hra, 0, 0)
    zkontroluj_otoceni(hra['stav'], [])
    assert hra['aktivni_karta'] == None

    hra = pexeso.udelej_tah(hra, 1, 2)
    zkontroluj_otoceni(hra['stav'], [(1, 2)])
    assert hra['aktivni_karta'] == (1, 2)

    hra = pexeso.udelej_tah(hra, 1, 3)
    zkontroluj_otoceni(hra['stav'], [(1, 2), (1, 3)])
    assert hra['aktivni_karta'] == None
				

def test_hry():
    hra = vytvor_zakladni_hru()
    hra = pexeso.udelej_tah(hra, 1, 2)
    zkontroluj_otoceni(hra['stav'], [(1, 2)])
    assert hra['aktivni_karta'] == (1, 2)

    hra = pexeso.udelej_tah(hra, 0, 0)
    zkontroluj_otoceni(hra['stav'], [])
    assert hra['aktivni_karta'] == None

    hra = pexeso.udelej_tah(hra, 1, 2)
    zkontroluj_otoceni(hra['stav'], [(1, 2)])
    assert hra['aktivni_karta'] == (1, 2)

    hra = pexeso.udelej_tah(hra, 1, 3)
    zkontroluj_otoceni(hra['stav'], [(1, 2), (1, 3)])
    assert hra['aktivni_karta'] == None
