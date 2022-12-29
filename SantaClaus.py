import random
import re
import os 
from name import prenom


## relier les personnes entre elles pour connaitre son SantaClaus
def ChooseSantaClaus(selfDictPerson:dict,selfAllName:list,selfContrainteDict:dict, selfnbrtry:int):
	global dictPerson
	global allName
	global contrainteDict
	global choix_version
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
			ChooseSantaClaus(dictPerson, allName, contrainteDict, selfnbrtry)
		elif selfnbrtry >= 10:
			if choix_version == True:
				os.system('cls')
				print(f"Vos choix ne sont pas possible, veuillez changer la contrainte de {i} :")
				print(allName)
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
			elif choix_version == False:
				for o in range(len(allName)):
					rangefor = random.randint(0,len(allName)%2)
					for k in range(rangefor):
						random_number2 = random.randint(0,len(allName)-1)
						while random_number2 == random_number:
							random_number2 = random.randint(0,len(allName)-1)
						icontrainte.append(allName[random_number2])
					contrainteDict.update({allName[o]:icontrainte})
				ChooseSantaClaus(dictPerson, allName, contrainteDict, 0)
	if len(kdo) != len(allName):
		for i in allName:
			if i not in kdo:
				kdo.update({i:'personne'})
	return kdo


choix = int(input("Vous préférez :\n\t1 - Version anonymes\n\t2 - Versions avec vos propres nom, e-mail, contraintes ...etc\n"))
if choix == 1:
	nbr_personne = int(input("Combien de personnes participent ?\n"))
	dictPerson = {}
	dictEmail = {}
	allName = []
	contrainteDict = {}
	for i in range(nbr_personne):
		random_number = random.randint(1,len(prenom))
		dictPerson.update({i:prenom[random_number]})
		dictEmail.update({prenom[random_number]:f"{prenom[random_number]}@gmail.com"})
		allName.append(prenom[random_number])
	for j in range(nbr_personne):
		endrangefor = int(len(allName)**0.5)
		rangefor = random.randint(0,endrangefor)
		print(rangefor)
		icontrainte = []
		for x in range(rangefor):
			random_number2 = random.randint(0,len(allName)-1)
			while random_number2 == random_number:
				random_number2 = random.randint(0,len(allName)-1)
			icontrainte.append(allName[random_number2])
		contrainteDict.update({allName[j]:icontrainte})
	choix_version = False
	kdo = ChooseSantaClaus(dictPerson, allName, contrainteDict,0)
	
else:
	#nombre x de personne
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
	choix_version = True

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

	kdo = ChooseSantaClaus(dictPerson, allName, contrainteDict,0)


try:
	result_file = open('result-email.txt','x', encoding='utf-8')
except:
	result_file = open('result-email.txt','w', encoding='utf-8')

for i in allName:
	templateMail = f"Bonjour {i} 👋\n\tVoici le jeux SantaClaus, une personne de votre entourage à été tiré au hasard, vous allé devoir acheter un cadeau à {kdo[i]}"
	result_file.write(f"{dictEmail[i]} {templateMail}\n\n")

result_file.write(f"\nAll name: {allName}\nParticipant: {dictPerson}\nEmail Participant: {dictEmail}\nContrainte: {contrainteDict}\n")