#Tässä tehtävässä otetaan ensikertaa käyttäjältä vastaan syöte, ja toteutamme yksinkertaisen ohjelman, joka suorittaa yhteenlaskuoperaation.
#Tee ohjelma, joka pyytää käyttäjältä kaksi lukua ja tallentaa ne kahteen eri muuttujaan. Tämän jälkeen laske luvut yhteen, ja tulosta vastaus. Ohjelman pitäisi toimiessaan antaa seuraanvanlainen tuloste:
#Laskin
#Anna ensimmäinen luku: 100
#Anna toinen luku: 25
#Tulos on: 125


#Tälläerää virheellisistä syötteistä, kuten merkkijonoista tai vastaavasta ei tarvitse välittää. Tämä on samalla ensimmäinen kahdesta "jatkuvasta tehtävästä", ja jatkammekin ohjelman laajentamista seuraavassa luvussa. Tämän vuoksi on myös suositeltavaa, että alat jatkossa kommentoimaan koodeja, koska myöhemmin palaamme aiemmin tehtyyn koodiin.
#Example output:
#Laskin
#Anna ensimmäinen luku: 10
#Anna toinen luku: 11
#Tulos on: 21

print("Laskin")
luku1 = int(input("Anna ensimmäinen luku:"))
luku2 = int(input("Anna toinen luku:"))

Tulos = luku1+luku2
print("Tulos on:",Tulos)
