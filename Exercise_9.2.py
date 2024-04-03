#Toinen tehtävä liittyy alifunktion parametrien välitykseen. Tee tehtävä, jossa on pääfunktio main ja alifunktio "toinenpotenssi". Alifunktio ottaa vastaan yhden parametrin, laskee sille toisen potenssin ja tulostaa vastauksen muodossa "Toinen potenssi on [vastaus]". Pääohjelma vastaavasti pyytää käyttäjältä lukua "Anna lukuarvo: " ja lähettää sen eteenpäin alifunktiolle. Toimiessaan oikein ohjelma toimii seuraavalla tavalla:

#Anna lukuarvo: 10
#Toinen potenssi on 100

#Tai vaikkapa

#Anna lukuarvo: 123123
#Toinen potenssi on 15159273129

#Muista myös laittaa ohjelmaan pääfunktiokutsu

#if __name__ == "__main__":
    main()
#Example output:
#Anna lukuarvo: 123123
#Toinen potenssi on 15159273129

def toinenpotenssi(luku):
	print("Toinen potenssi on",luku**2)
	
def main():
	syote = int(input("Anna lukuarvo:"))
	toinenpotenssi(syote)
	
if __name__ == "__main__":
	main()
		  
