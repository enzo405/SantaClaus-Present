import random
import re

## nombre x de personne
try:
	nbr_personne = int(input("Choisir le nombre de personne : "))
except: 
	print('You must enter a number')
	nbr_personne = "1"
while type(nbr_personne) != int:
	try:
		nbr_personne = int(input("Choisir le nombre de personne : "))
	except: 
		print('You must enter a number')


## définir le nom de toute les personnes
dictPerson = {}
allName = []
contrainteDict = {}

for i in range(nbr_personne):
	name = input(f"Rentrez le nom n°{i+1}: ")
	while name in allName or name == "":
		name = input(f"Rentrez le nom n°{i+1}: ")
	email = input(f"Rentrez l'adresse E-mail de {name} (say no if you don't want to put an email): ")
	email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
	while True:
		if email_pattern.match(email):
			break
		elif email == "no":
			break
		else:
			email = input(f"Rentrez l'adresse E-mail de {name}: ")
	dictPerson.update({i:f"{name} {email}"})
	allName.append(name)
print(dictPerson)


## définir les contraintes qu'aura cette personne
for i in range(nbr_personne):
	nameContrainte = input(f"Enter a list (separate with ',') that {dictPerson[i]} won't be abble to send: ").replace(' ','').split(",")
	for y in nameContrainte:
		if y == "":
			indexList = nameContrainte.index(y)
			nameContrainte[indexList] = 'aucune'
		else:
			if y not in allName:
				nameContrainte = input(f"RE Enter a list (separate with ',') that {dictPerson[i]} won't be abble to send: ").replace(' ','').split(",")
	while dictPerson[i] in nameContrainte:
		nameContrainte = input(f"Enter a list (separate with ',') that {dictPerson[i]} won't be abble to send: ").replace(' ','').split(",")
	contrainteDict.update({dictPerson[i]:nameContrainte})


## relier les personnes entre elles pour connaitre son SantaClaus
def ChooseSantaClaus(dictPerson:dict,allName:list,contrainteDict:dict):
	alreadyUsedPerson = ""
	kdo = {}
	for i in allName:
		availableName = list(dictPerson.keys())
		try:
			availableName.remove(alreadyUsedPerson)
		except ValueError as ee:
			print(ee,availableName,alreadyUsedPerson)
		for x in availableName:
			if dictPerson[x] == i:
				availableName.remove(x)
		for y in contrainteDict[i]:
			value = list(dictPerson.values())
			indexPersonContraint = ''
			try:
				indexPersonContraint = value.index(y)
				availableName.remove(indexPersonContraint)
			except ValueError as e:
				print(e,availableName,indexPersonContraint)
		toName = random.choice(availableName)
		alreadyUsedPerson = toName
		kdo.update({i:dictPerson[toName]})
	return kdo


print(ChooseSantaClaus(dictPerson, allName, contrainteDict))