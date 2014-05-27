import pexeso


def test_slovo_podle_indexu():
    assert pexeso.slovo_podle_indexu(1, 'C') == 'Kolečko'
    assert pexeso.slovo_podle_indexu(2, 'A') == 'Smile'


def test_vyberu_karty():
    stav = [
        [(0, 'C'), (0, 'A'), (1, 'C'), (1, 'A')],
        [(2, 'C'), (2, 'A'), (3, 'C'), (3, 'A')],
        [(4, 'C'), (4, 'A'), (5, 'C'), (5, 'A')],
        [(6, 'C'), (6, 'A'), (7, 'C'), (7, 'A')],
    ]
    assert pexeso.vyber_kartu(stav, 0, 0) == (0, 'C')
    assert pexeso.vyber_kartu(stav, 0, 1) == (0, 'A')
    assert pexeso.vyber_kartu(stav, 2, 3) == (5, 'A')
    assert pexeso.vyber_kartu(stav, 3, 3) == (7, 'A')


def test_zamichani():
    stav = pexeso.zamichej_karty()
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
    assert pexeso.zamichej_karty() != pexeso.zamichej_karty()
