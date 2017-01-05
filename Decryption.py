#! /usr/bin/python

def chiffrer(lignesChiffrees, indiceRotation):
	resultat = ""

	for motChiffre in lignesChiffrees:
		for charChiffre in motChiffre:
			if ('a' <= charChiffre) and (charChiffre <= 'z'):
            			resultat += chr((ord(charChiffre) - ord('a') + indiceRotation) % 26 + ord('a'))
        		elif ('A' <= charChiffre) and (charChiffre <= 'Z'):
            			resultat += chr((ord(charChiffre) - ord('A') + indiceRotation) % 26 + ord('A'))
        		else:
            			resultat += charChiffre;
    	return resultat;




if __name__ == "__main__":
	contenuEntree = open("TestInputDecryption.txt");
	contenuSortie = open("TestOutputDecryption.txt", "w");
	
	toutesLesLignesEntree = contenuEntree.readlines();

	indice = [24, 5, 13, 18];
	toutesLesLignesSortie = ["", "", "", ""];
	
	for i in range(0, 4):
		toutesLesLignesSortie[i] = chiffrer(toutesLesLignesEntree[i], indice[i]);
	
	for i in range(0, 4):
		contenuSortie.write(toutesLesLignesSortie[i]);
		
	contenuEntree.close();
	contenuSortie.close();
