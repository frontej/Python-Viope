#Kolmas esimerkki on ensimmäinen tehtävä, jossa luodaan käyttäjälle valikko. Käyttäjältä pyydetään luku väliltä 1-3, ja sen mukaan, mitä käyttäjä valitsee tulostetaan joko "Haukion kala Oy" valinnalla 1, "Metallipaja VasaraAika" valinnalla 2 tai "Balin palapelitehdas" valinnalla 3. Toimiessaan ohjelma tulostaa esimerkiksi seuraavaa:

#Valitse kohde (1-3): 1
#Haukion kala Oy

#Example output:
#Valitse kohde (1-3): 3
#Balin palapelitehdas

kohde = input("Valitse kohde (1-3):")
kohde = int(kohde)

if kohde ==1:
	print("Haukion kala Oy")
	
if kohde ==2:
	print("Metallipaja VasaraAika")
if kohde ==3:
	print("Balin palapelitehdas")
