#Tästä luvusta eteenpäin ohjelmissa, joissa on erillisiä alifunktioita, tulisi olla myös erillinen pääfunktio.
#Ensimmäinen tehtävä on yksinkertaisen funktiorakenteen toteuttaminen. Tee ohjelma, jossa on pääfunktio main ja yksi alifunktio nimeltään tulostaja. Kutsuttaessa alifunktio ei vastaanota parametreja eikä palauta mitään, mutta tulostaa tekstin "Tulostusfunktio!". Pääohjelman ainoa toiminto on kutsua alifunktiota. Ohjelma tulostaa siis tekstin

#Tulostusfunktio!

#Muista myös laittaa ohjelmaan pääfunktiokutsu
#if __name__ == "__main__":
#main()

#Example output:
#Tulostusfunktio!

def tulostaja():
	print("Tulostusfunktio!")
	
def main():
	tulostaja()

if __name__ == "__main__":
	main()
	
