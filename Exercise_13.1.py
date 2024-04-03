#Määritellään luokkaa nimeltä Kilpailija, jolle annettaan kaksi jäsenmuuttujaa, pisteet ja vari. Tämän jälkeen luo luokasta olio "eka", jolle annetaan muuttujan vari arvoksi sininen ja pisteet arvoksi 10. Lopuksi laita ohjelmasi vielä tulostamaan olion tiedot muodossa "Kilpailijalla [väri] on [pisteet] pistettä!", eli näin:

#Kilpailijalla sininen on 10 pistettä!
#Example output:
#Kilpailijalla sininen on 10 pistettä!

class Kilpailija:
     def __init__(self, pisteet = 0, vari = ""):
         self.pisteet = pisteet
         self.vari = vari

eka = Kilpailija(10, "sininen")
print("Kilpailijalla " + str(eka.vari) + " on " + str(eka.pisteet) + " pistettä!")
