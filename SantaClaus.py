import random
import re

# nombre x de personne
try:
	nbr_personne = int(input("Choisir le nombre de personne : "))
except:
	print('You must enter a number')
	nbr_personne = "1"
while type(nbr_personne) != int or nbr_personne < 2:
	try:
		nbr_personne = int(input("Choisir le nombre de personne : "))
	except: 
		print('You must enter a number')

## définir le nom de toute les personnes
dictPerson = {}
dictEmail = {}
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
			email = "none"
			break
		else:
			email = input(f"Rentrez l'adresse E-mail de {name}: ")
	dictPerson.update({i:name})
	dictEmail.update({i:email})
	allName.append(name)


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
	contrainteDict.update({dictPerson[i][0]:nameContrainte})


# dictPerson = {0: 'jean', 1: 'marc', 2: 'jim', 3: 'alex'}
# dictEmail = {0: '****', 1: '*****', 2:'****', 3:'******'}
# allName = ['jean','marc','jim', 'alex']
# contrainteDict = {'jean': ['marc'], 'marc': ['enzo', 'jim'], 'jim': ['alex'], 'alex': ['jim']}


## relier les personnes entre elles pour connaitre son SantaClaus
def ChooseSantaClaus(selfDictPerson:dict,selfAllName:list,selfContrainteDict:dict):
	global dictPerson
	global allName
	global contrainteDict
	kdo = {}
	global_availableName = list(selfDictPerson.keys())
	for i in selfAllName:
		selfAvailableName = global_availableName.copy()
		for x in selfAvailableName:
			if selfDictPerson[x] == i:
				selfAvailableName.remove(x)
		for y in selfContrainteDict[i]:
			value = list(selfDictPerson.values())
			indexPersonContraint = ''
			try:
				indexPersonContraint = value.index(y)
				selfAvailableName.remove(indexPersonContraint)
			except ValueError as e:
				a=1 ##pour faire rien (je sais pas si le pass ou break fonctionne à la place)
		if len(selfAvailableName) == 0:
			ChooseSantaClaus(dictPerson, allName, contrainteDict)
		else:
			toName = random.choice(selfAvailableName)
			global_availableName.remove(toName)
			kdo.update({i:selfDictPerson[toName]})
	return kdo


print(ChooseSantaClaus(dictPerson, allName, contrainteDict))