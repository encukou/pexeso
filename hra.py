import sys
import os.path
import pexeso

def hrej():
	"""1. dostane na prikazovem radku jmeno souboru
	2. pokusoubor existuje, nacte hru, pokud ne, vytvori novou hru pomoci zamichej karty os.path.exists()
	3. vypise na cmd osbah hry
	4. zepta se hrace, kam chce tahnout
	5. udela tah a vypise novy stav hry
	6. novy stav zapise do souboru (ktery dostane v argumentu """	
	jmeno_souboru = sys.argv[1]
	if os.path.exists(jmeno_souboru):
		hra = pexeso.nacti_hru_ze_souboru(jmeno_souboru)
	else:
		hra = pexeso.zamichej_karty()
	print (hra)
	
hrej()