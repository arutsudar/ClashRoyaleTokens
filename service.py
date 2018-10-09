import json
from cardTradableDetails import cardsNeededBy
from cardTradableDetails import cardsDonatableBy
import constants
import util

#Input is the full Player Json endpoint
#Output is an array of Jsons
#Filtering the card details array
def getCardsDetailsFromPlayerJsonAsArray(playerJson):
	return playerJson['cards']

	
#Input is a list of Jsons as an array
#Output is a filtered list of Jsons as an array
#Filtering is based on the card availability for the trade	
def filterCardsBasedOnAvailabilityForTrade(cardsJsonArray):
	resultArray=[]
	for i in cardsJsonArray:
		if i['count']>=250 and i['rarity']=='Common':
			if not(i['level']==1 and i['count']==250):
				resultArray.append(i)
		if i['count']>=50 and i['rarity']=='Rare':
			if not(i['level']==1 and i['count']==50):
				resultArray.append(i)
		if i['count']>=10 and i['rarity']=='Epic':
			if not(i['level']==1 and i['count']==10):
				resultArray.append(i)
		if i['count']>=1 and i['rarity']=='Legendary':
			if not(i['level']==1 and i['count']==1): #This is case is - when you have just unlocked the card and you don't have enough cards to donate
				resultArray.append(i)
	return resultArray
	

#Inputs are playerTag and the list of cards names
#Storing the cards needed by a particular playerJson
def saveCardsNeededForParticularPlayer(playerTag,cardsList):
	for i in cardsList:
		flag=0
		for j in cardsNeededBy:
			if i == j.keys()[0]:
				flag=1
				j.get(i).append(playerTag)
		if flag==0:
			cardsNeededBy.append({i: [playerTag]})

			
#Input 1 is a list of Jsons as an array 
#Input 2 is list of card names which the player needs
#Output is a filtered list of Jsons as an array
#Filtering is based on the player need (If the player needs the card, it is not added in resultArray)		
def filterCardsByExcludingCardsNeededByPlayer(cardsJsonArray,cardsList): #Might be able to optimize this function
	resultArray=[]
	for i in cardsJsonArray:
		flag=0
		for j in cardsList:
			if i['name']==j:
				flag=1
				break
		if flag==0:
			resultArray.append(i)
	return resultArray
	

#Input is cardJsonArray
#Output is cardsNameList	
def getCardsNamesFromcardJsonArray(cardJsonArray):
	resultList=[]
	for i in cardJsonArray:
		resultList.append(i['name'])
	return resultList
	
	
#Inputs are playerTag and the list of cards names
#Storing the cards which can be donated by a particular player
def saveCardsWhichAreDonatableByParticularPlayer(playerTag,cardsNamesList):	
	for i in cardsNamesList:
		flag=0
		for j in cardsDonatableBy:
			if i == j.keys()[0]:
				flag=1
				j.get(i).append(playerTag)
		if flag==0:
			cardsDonatableBy.append({i: [playerTag]})

		
#Input 1 is a list of Jsons as an array 
#Input 2 is rarity name
#Output is a filtered list of Jsons as an array
#Filtering is based on rarity
def filterCardsBasedOnRarity(cardsJsonArray,rarity):
	resultArray=[]
	for i in cardsJsonArray:
		if i['rarity']==rarity:
			print i['name']
			resultArray.append(i)
	return resultArray


#Return a string list of names of all cards in clash royale	
def getAllCardsNamesAsList():
    return constants.cardNamesList
	

#Input is the unlockedCards names and allCards names in order
#Return the cards which are not unlocked yet
def cardsWhichAreNotUnlocked(unlockedCards, allCards):
	return util.differenceOfListTwoToListOne(unlockedCards, allCards)	


#Input is the availableCards names and allCards names in order
#Return the cards which are unlocked 
def cardsWhichAreUnlocked(cards, allCards):
	return util.intersectionOfTwoLists(cards, allCards)	#Right now the input 'cards' listis the same as the unlocked cards list

	
