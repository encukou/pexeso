import pprint

slova = []

with open('slova.txt') as soubor:
    for radek in soubor:
        slova.append(radek.split())

pprint.pprint(slova)

def slovo_podle_indexu(cislo, jazyk):
    radek = slova[cislo]
    if jazyk == 'C':
        return radek[0]
    elif jazyk == 'A':
        return radek[1]
    else:
        raise ValueError(jazyk)


def test_slovo_podle_indexu():
    assert slovo_podle_indexu(1, 'C') == 'Kolečko'
    assert (slovo_podle_indexu(2, 'A') ==
            'Smile')
