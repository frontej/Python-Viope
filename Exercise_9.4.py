#Neljäs tehtävä lisää ohjelmaan paluuarvon. Tee ohjelma, jossa on pääfunktio main ja alifunktio pituusmitta. pituusmitta saa syötteenä parametrin ja mittaa tämän parametrin pituuden, palauttaen sen integer-arvona pääohjelmalle.

#Pääohjelma pyytää käyttäjältä syötettä "Anna syote (Lopeta lopettaa): " ja lähettää syötteen mitattavaksi. Jos tulos on 0, ohjelma vastaa "Et antanut syötettä", muuten "Antamasi syöte oli [pituus] merkkiä pitkä.". Jos käyttäjä antaa arvon Lopeta, ohjelma sammuu. Ohjelma tulostaa seuraavaa:

#Anna syöte (Lopeta lopettaa): sihijuomaa
#Antamasi syöte oli 10 merkkiä pitkä.
#Anna syöte (Lopeta lopettaa): nahkasaapasharja
#Antamasi syöte oli 16 merkkiä pitkä.
#Anna syöte (Lopeta lopettaa): 
#Et antanut syötettä
#Anna syöte (Lopeta lopettaa): Lopeta

#Example output:
#Anna syöte (Lopeta lopettaa): testi
#Antamasi syöte oli 5 merkkiä pitkä.
#Anna syöte (Lopeta lopettaa): 
#Et antanut syötettä
#Anna syöte (Lopeta lopettaa): sana
#Antamasi syöte oli 4 merkkiä pitkä.
#Anna syöte (Lopeta lopettaa): Lopeta

def pituusmitta(sana):
    mitta=len(sana)
    mitta=int(mitta)
    return mitta
    
def main():
    jatka = True
    while jatka:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if sana == "Lopeta":
                jatka = False
                break
        else:
            pituusmitta(sana)
        pituus=pituusmitta(sana)

        if pituus==0:
            print("Et antanut syötettä")
        else:    
            print("Antamasi syöte oli", pituus,"merkkiä pitkä.")


if __name__ == "__main__":
    main()
