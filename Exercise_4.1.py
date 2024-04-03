#Kolmas tehtävä käsittelee tyyppimuunnoksia. Luodaan kaksi muuttujaa, joille annetaan arvoiksi 10.6411 ja "Merkkijono".
#Tee numeroarvon sisältävälle muuttujalle int()-tyyppimuunnos, ja kerro merkkijono kahdella. Tämän jälkeen laita ohjelmasi tulostamaan saamasi vastaukset muodossa

#Kokonaislukumuunnos ei osaa pyöristää: 10
#Merkkijonon kertominen tuottaa toistoa: MerkkijonoMerkkijono

#Example output:
#Kokonaislukumuunnos ei osaa pyöristää: 10
#Merkkijonon kertominen tuottaa toistoa: MerkkijonoMerkkijono

muuttuja_1 = 10.6411
muuttuja_2 = "Merkkijono"

muuttuja_1 = int(muuttuja_1)
muuttuja_2 = muuttuja_2*2

print("Kokonaislukumuunnos ei osaa pyöristää:",muuttuja_1)
print("Merkkijonon kertominen tuottaa toistoa:",muuttuja_2)
