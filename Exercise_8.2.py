#Kolmas tehtävä on taas hieman vaikeampi aiempiin verrattuna. Lähdekooditiedoston kanssa samaan hakemistoon on tallennettuna tiedosto "merkkijonoja.txt". Tämä tiedosto sisältää satunnaisesti luotuja merkkijonoja, joissa esiintyy kahdenlaisia merkkijonoja: sellaisia, joissa on kirjaimia ja mahdollisesti numeroita, sekä sellaisia, joissa on kirjaimia, numeroita ja erikoismerkkejä (€,#,{, §, jne). Tehtävänäsi on tehdä ohjelma, joka lukee tiedostosta rivin, testaa onko merkkijono sellainen, joka sisältää vain kirjaimia ja numeroita, ja sen mukaan tulostaa joko "[merkkijono] kelpaa salasanaksi" jos on, tai "[merkkijono] sisältää virheellisiä merkkejä." mikäli siinä on ei-alfanumeerisia merkkejä. Toimiessaan ohjelma tulostaa seuraavaa:

#5345m345ö34l kelpaa salasanaksi.
no2no123non4 kelpaa salasanaksi.
noq234n5ioqw#% sisältää virheellisiä merkkejä.
%#""SGMSGSER sisältää virheellisiä merkkejä.
doghdp5234 kelpaa salasanaksi.
sg,dermoepm sisältää virheellisiä merkkejä.
43453-frgsd sisältää virheellisiä merkkejä.
hsth())) sisältää virheellisiä merkkejä.
bmepm35wae kelpaa salasanaksi.
vmopaem2234+0+ sisältää virheellisiä merkkejä.
gsdm12313 kelpaa salasanaksi.

#Tehtävässä kannattaa rivit lukea yksi kerrallaan ja testata .isalnum()-merkkijonometodilla. Lisäksi muista poistaa lopussa oleva rivinvaihtomerkki, se ei ole kirjain eikä numero!

#Example output:
111m345a34l kelpaa salasanaksi.
ddno123non4 kelpaa salasanaksi.
asdf34n5ioqw#% sisältää virheellisiä merkkejä.
%#""SGMSGSER sisältää virheellisiä merkkejä.
doghdp5234 kelpaa salasanaksi.
2253-frgsd sisältää virheellisiä merkkejä.
hsth())) sisältää virheellisiä merkkejä.
addm35wae kelpaa salasanaksi.
vmopaem2234+0+ sisältää virheellisiä merkkejä.
gsdm123 kelpaa salasanaksi.

tiedosto = open("merkkijonoja.txt","r")
sisalto = tiedosto.readlines()

for i in sisalto:
	i = i.rstrip()
	if i.isalnum() == True:
		print(i, "kelpaa salasanaksi.")
	else:
		print(i,"sisältää virheellisiä merkkejä.")
	tiedosto.close()
	
