#Luvun kolmas tehtävä käsittelee oman moduulin tekemistä. Tämä tehtävä on siitä poikkeuksellinen, että tarkoitus ei olekaan kirjoittaa kokonaista ohjelmaa, vaan ainoastaan toteuttaa moduuli olemassaolevalle ohjelmalle.

#Meillä on valmiina ohjelman pääfunktion sisältävä moduuli, jonka sisältö näyttää tältä:

# -*- coding: cp1252 -*-
#import moduuli
#moduuli.tulosta("Esimerkkirivi")

#Tehtäväsi onkin nyt tuottaa ohjelmassa sisällytetty moduuli; luo koodi, jossa on tulosta-niminen funktio, joka tulostaa sille annetun parametrin ja parametrin pituuden muodossa "Saatiin syöte: [parametri].\n Syötteen pituus on [pituus] merkkiä.". Toimiessaan ohjelma tulostaa seuraavaa:

#Saatiin syöte: Esimerkkirivi
#Syötteen pituus on 13 merkkiä.

#Example output:
#Saatiin syöte: Esimerkkirivi
#Syötteen pituus on 13 merkkiä.

def tulosta(syote):
	print("Saatiin syöte:", syote)
	print("Syötteen pituus on", len(syote), "merkkiä.")
