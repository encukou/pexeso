import pexeso


zakladni_stav = [
    [(0, 'C', False), (0, 'A', False), (1, 'C', False), (1, 'A', False)],
    [(2, 'C', False), (2, 'A', False), (3, 'C', False), (3, 'A', False)],
    [(4, 'C', False), (4, 'A', False), (5, 'C', False), (5, 'A', False)],
    [(6, 'C', False), (6, 'A', False), (7, 'C', False), (7, 'A', False)],
]

zakladni_hra = {
    'stav': zakladni_stav,
    'aktivni_karta': None,
}


def test_slovo_podle_indexu():
    assert pexeso.slovo_podle_indexu(1, 'C') == 'Kolečko'
    assert pexeso.slovo_podle_indexu(2, 'A') == 'Smile'


def test_vyberu_karty():
    assert pexeso.vyber_kartu(zakladni_stav, 0, 0) == (0, 'C', False)
    assert pexeso.vyber_kartu(zakladni_stav, 0, 1) == (0, 'A', False)
    assert pexeso.vyber_kartu(zakladni_stav, 2, 3) == (5, 'A', False)
    assert pexeso.vyber_kartu(zakladni_stav, 3, 3) == (7, 'A', False)


def test_zamichani():
    stav = pexeso.zamichej_karty()
    assert len(stav) == 4
    prvky = []
    for radek in stav:
        assert len(radek) == 4
        prvky += radek
    for cislo in range(8):
        for pismeno in 'C', 'A':
            prvek = cislo, pismeno, False
            assert prvky.count(prvek) == 1


def test_nahodneho_zamichani():
    # (Tehnle test v jednom z 20922789888000
    # případů neprojde)
    assert pexeso.zamichej_karty() != pexeso.zamichej_karty()


def zkontroluj_otoceni(stav, otocene_karty):
    for radek in range(4):
        for sloupec in range(4):
            prvek = pexeso.vyber_kartu(stav, radek, sloupec)
            if (radek, sloupec) in otocene_karty:
                assert prvek[2] == True
            else:
                assert prvek[2] == False


def test_hry():
    hra = zakladni_hra

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
