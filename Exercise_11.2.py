#Toisessa tehtävässä luodaan ohjelma, joka osaa selviytyä useammasta virhetyypistä. Tee ohjelma, joka pyytää käyttäjältä tiedoston nimen, sekä avaa ja lukee tiedoston sisällön. Tämän jälkeen ohjelma yrittää muuttaa tiedostosta luetun arvon kokonaisluvuksi, sekä lisätä siihen arvon 313. Jos kaikki menee oikein, ohjelma tulostaa vastauksen "Saatiin tulos [tulos]". Jos annettu tiedoston nimi on virheellinen, tulostetaan "Virheellinen tiedostonnimi". Jos taas tiedoston sisältö on virheellinen eikä käänny kokonaisluvuksi, tulostetaan "Tiedoston sisältö virheellinen!". Toimiessaan ohjelma tulostaakin seuraavaa:

#Anna tiedoston nimi: hu
#Virheellinen tiedostonnimi
#>>> 
#Anna tiedoston nimi: muistio.txt
#Tiedoston sisältö virheellinen!
#>>> 
#Anna tiedoston nimi: luku.txt
#Saatiin tulos 626

#Ohjelma on järkevintä toteuttaa yhdellä virheenkäsittelyrakenteella, jolla on omat käsittelijät IOError ja ValueError-virheille.
#Example output:
#Anna tiedoston nimi: luku.txt
#Saatiin tulos 413

syote = input("Anna tiedoston nimi:")
try:
    syote = open(syote,"r")
    luku = int(syote.read())
    syote.close()
    luku = luku + 313
    print("Saatiin tulos",luku)
except IOError:
    print("Virheellinen tiedostonnimi")
except ValueError:
    print("Tiedoston sisältö virheellinen!")
