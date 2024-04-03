#Luvun viimeinen tehtävä on kurssin toisen jatkuvan tehtäväsarjan ensimmäinen tehtävä. Tässä tehtävässä teemme muistikirjan, joka tallennetaan erilliseen tiedostoon nimeltä "muistio.txt".


#Tee ohjelma, joka antaa käyttäjälle mahdollisuuden
#(1) lukea muistikirjan sisältö,
#(2) Lisätä muistikirjaan merkintä tai
#(3) Tyhjentää koko muistikirja
#Lisäksi lisää valinta (4), joka lopettaa ohjelman. Mikäli käyttäjä valitsee 1, tulostetaan tiedoston sisältö ruudulle, mikäli 2 niin ohjelma kysee "Kirjoita uusi merkintä: " ja tallentaa merkinnän muistioon, lisäten merkinnän loppuun rivinvaihtomerkin "\n" jotta merkinnät pysyvät eri riveillä. Jos käyttäjä valitsee 3 tyhjennetään tiedosto ja tulostetaan näytölle teksti "Muistio tyhjennetty." ja valinnalla 4 ohjelma ilmoittaa "Lopetetaan." ja sammuu. Muilla valinnoilla ohjelma ilmoittaa "Tuntematon valinta.". Toimiessaan ohjelma tulostaa seuraavaa:

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta maitoa
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 1
-Osta maitoa
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 4
Lopetetaan.

#Huomaa, että nopein tapa tiedoston tyhjentämiseen on avata se tilaan "w" ja sulkea samantien.

#Example output:
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 1
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta mehua
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 1
-Osta mehua
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 3
Muistio tyhjennetty.
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 1
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: 4
#Lopetetaan.


while True:
	print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")
	valinta = int(input("Mitä haluat tehdä?:"))
	if valinta == 1:
		tiedosto = open("muistio.txt","r")
		sisalto = tiedosto.readline()
		print(sisalto)
		tiedosto.close()
	elif valinta == 2:
		tiedosto = open("muistio.txt","a")
		lisays = input("Kirjoita uusi merkintä: ")
		lisays = lisays +"\n"
		tiedosto.write(lisays)
		tiedosto.close()
	elif valinta == 3:
		tiedosto = open("muistio.txt","w")
		print("Muistio tyhjennetty.")
		tiedosto.close()
	elif valinta == 4:
		print("Lopetetaan.")
		break
	else:
		print("Tuntematon valinta.")



