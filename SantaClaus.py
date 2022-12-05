import random
import re
import traceback

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
dictPerson = {0: 'enzo', 1: 'raphael', 2: 'sam', 3: 'rossella'}
dictEmail = {0: 'enzo.chaboisseau@gmail.com', 1: 'raphael.chaboisseau@gmail.com', 2:'sam@chaboisseau.net', 3:'none'}
allName = ['enzo','raphael','sam', 'rossella']
contrainteDict = {'enzo': ['raphael'], 'raphael': ['enzo', 'sam'], 'sam': ['rossella'], 'rossella': ['sam']}

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


## relier les personnes entre elles pour connaitre son SantaClaus
def ChooseSantaClaus(fDictPerson:dict,fAllName:list,fContrainteDict:dict):
	global dictPerson
	global allName
	global contrainteDict
	kdo = {}
	global_availableName = list(fDictPerson.keys())
	for i in fAllName:
		selfAvailableName = global_availableName.copy()
		for x in selfAvailableName:
			if fDictPerson[x] == i:
				selfAvailableName.remove(x)
		for y in fContrainteDict[i]:
			value = list(fDictPerson.values())
			indexPersonContraint = ''
			try:
				indexPersonContraint = value.index(y)
				selfAvailableName.remove(indexPersonContraint)
			except ValueError as e:
				print(f"{selfAvailableName}.remove({indexPersonContraint})")
		if len(selfAvailableName) == 0:
			ChooseSantaClaus(dictPerson, allName, contrainteDict)
		else:
			toName = random.choice(selfAvailableName)
			global_availableName.remove(toName)
			kdo.update({i:fDictPerson[toName]})
	return kdo


print(ChooseSantaClaus(dictPerson, allName, contrainteDict))