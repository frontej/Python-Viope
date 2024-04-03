#Kolmas tehtävä käyttää for-toistorakennetta ja se on hieman aiempia monimutkaisempi. Tee ohjelma, joka pyytää käyttäjältä kierrosmäärän. Tämän jälkeen tee ohjelma, joka laskee kierroslukujen kertymän. Eli jos käyttäjä antaa syötteen 3, laskee ohjelma 0+1+2, jos 5 niin 0+1+2+3+4. Lopuksi ohjelma tulostaa käyttäjälle lopputuloksen muodossa "Kertymäksi saatiin:" ja vastaus.

#Toimiessaan oikein ohjelma tulostaa seuraavaa:

#Kuinka monta kierrosta?: 3
#Kertymäksi saatiin: 3

#Tehtävässä kannattaa kokeilla kuinka kierrosluvun lisääminen muuttujaan toimii, eli vaikkapa tulos = tulos + kierrosluku.
#Example output:
#Kuinka monta kierrosta?: 5
#Kertymäksi saatiin: 10

kierroksia = int(input("Kuinka monta kierrosta?: "))
summa = 0
for i in range(1,kierroksia):
    summa = summa + i

print("Kertymäksi saatiin:",summa)
	
