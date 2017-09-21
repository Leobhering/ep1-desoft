with open("nomes.txt", "r") as arquivo:
 	lista_de_nomes = []
 	for linha in arquivo:
 		lista_de_nomes.append(linha)
for nome in range(0,len(lista_de_nomes)):
	lista_de_nomes[nome] = lista_de_nomes[nome].title()
	lista_de_nomes[nome] = lista_de_nomes[nome].lstrip()
	lista_de_nomes[nome] = lista_de_nomes[nome].rstrip()
	lista_de_nomes[nome] = lista_de_nomes[nome].split()
	for nomer in range(0,len(lista_de_nomes[nome])-1):
		if lista_de_nomes[nome][nomer]==lista_de_nomes[nome][nomer+1]:
			lista_de_nomes[nome][nomer]=lista_de_nomes[nome][nomer].replace(lista_de_nomes[nome][nomer],"")
	lista_de_nomes[nome] = " ".join(lista_de_nomes[nome])
	lista_de_nomes[nome] = lista_de_nomes[nome].split()
	lista_de_nomes[nome] = " ".join(lista_de_nomes[nome])
	lista_de_nomes[nome]=lista_de_nomes[nome].replace(" De "," de ")
	lista_de_nomes[nome]=lista_de_nomes[nome].replace(" Do "," do ")
	lista_de_nomes[nome]=lista_de_nomes[nome].replace(" Da "," da ")
print(set(lista_de_nomes))