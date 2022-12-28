import random
import re
import os 


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
nbrtry = 0 

for i in range(nbr_personne):
	name = input(f"Rentrez le nom n°{i+1}: ")
	while name in allName or name == "":
		name = input(f"Rentrez le nom n°{i+1}: ")
	email = input(f"Rentrez l'adresse E-mail de {name}: ")
	email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
	while True:
		if email_pattern.match(email):
			break
		elif email == "no" or email == "":
			email = name + "@gmail.com" 
			break
		else:
			email = input(f"Rentrez l'adresse E-mail de {name}: ")
	dictPerson.update({i:name})
	dictEmail.update({name:email})
	allName.append(name)


## définir les contraintes qu'aura cette personne
for i in range(nbr_personne):
	nameContrainte = input(f"Enter a list (separate with ',') that {dictPerson[i]} won't be abble to send: ").replace(' ','').split(",")
	for y in nameContrainte:
		if y not in allName and y != "":
			nameContrainte = input(f"{y} is not in {allName}, please Enter again: ").replace(' ','').split(",")
	while dictPerson[i] in nameContrainte or len(nameContrainte) == nbr_personne-1 :
		nameContrainte = input(f"Enter a list (separate with ',') that {dictPerson[i]} won't be abble to send: ").replace(' ','').split(",")
	contrainteDict.update({dictPerson[i]:nameContrainte})



## relier les personnes entre elles pour connaitre son SantaClaus
def ChooseSantaClaus(selfDictPerson:dict,selfAllName:list,selfContrainteDict:dict, selfnbrtry:int):
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
			except Exception as e:
				print(e)
		if len(selfAvailableName) != 0:
			toName = random.choice(selfAvailableName)
			global_availableName.remove(toName)
			kdo.update({i:selfDictPerson[toName]})
		elif len(selfAvailableName) == 0 and selfnbrtry < 10:
			selfnbrtry = selfnbrtry + 1
			ChooseSantaClaus(dictPerson, allName, contrainteDict,selfnbrtry)
			break
		elif selfnbrtry >= 10:
			os.system('cls')
			print(f"Vos choix ne sont pas possible, veuillez changer la contrainte de {i} :")
			nameContrainte = input(f"Enter a list (separate with ',') that {i} won't be abble to send: ").replace(' ','').split(",")
			for y in nameContrainte:
				if y == "":
					indexList = nameContrainte.index(y)
					nameContrainte[indexList] = 'aucune'
				else:
					if y not in allName:
						nameContrainte = input(f"{y} is not in {allName}, please Enter again: ").replace(' ','').split(",")
			while i in nameContrainte or len(nameContrainte) == len(allName)-1 :
				nameContrainte = input(f"Enter a list (separate with ',') that {i} won't be abble to send: ").replace(' ','').split(",")
			contrainteDict.update({i:nameContrainte})
			ChooseSantaClaus(dictPerson, allName, contrainteDict,0)
	if len(kdo) != len(allName):
		for i in allName:
			if i not in kdo:
				kdo.update({i:'personne'})
	return kdo


kdo = ChooseSantaClaus(dictPerson, allName, contrainteDict,nbrtry)
for i in allName:
	templateMail = f"Bonjour {i} 👋\n\tVoici le jeux SantaClaus, une personne de votre entourage à été tiré au hasard, vous allé devoir acheter un cadeau à {kdo[i]}"
	print(dictEmail[i],templateMail)












# Pour les test : 
# dictPerson = {0:'Olivia',1:'Noah', 2:'Alice', 3:'Léa', 4:'Thomas', 5:'Mia', 6:'Jacob', 7:'Charlie', 8:'Nathan', 9:'Florence', 10:'Léo', 11:'Charlotte'}
# dictEmail = {0:'Olivia@gmail.com',1:'Noah@gmail.com', 2:'Alice@gmail.com', 3:'Léa@gmail.com', 4:'Thomas@gmail.com', 5:'Mia@gmail.com', 6:'Jacob@gmail.com', 7:'Charlie@gmail.com', 8:'Nathan@gmail.com', 9:'Florence@gmail.com', 10:'Léo@gmail.com', 11:'Charlotte@gmail.com'}
# allName = ['Olivia','Noah','Alice','Léa','Thomas','Mia','Jacob','Charlie','Nathan','Florence','Léo','Charlotte']
# contrainteDict = {'Olivia':['Olivia'],'Noah':['Noah'], 'Alice':['Alice'], 'Léa':['Léa'], 'Thomas':['Thomas'], 'Mia':['Mia'], 'Jacob':['Jacob'], 'Charlie':['Charlie'], 'Nathan':['Nathan'], 'Florence':['Florence'], 'Léo':['Léo'], 'Charlotte':['Charlotte']}
