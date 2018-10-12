import json
import service
import httpService

#Input is a playerTag
#Output is a json consisting of "cardsHaving", "cardsNotUnlocked" and "cardsWhichAreDonatable" by the player
def getCardDetails(playerTag):
	
	allCardsNames = service.getAllCardsNamesAsList()
	playerJsonData = httpService.getPlayer(playerTag)
	
	cardsHaving = service.getCardsDetailsFromPlayerJsonAsArray(playerJsonData)
	cardsWhichAreDonatable = service.filterCardsBasedOnAvailabilityForTrade(cardsHaving)
	
	cardsNamesHaving = service.getCardsNamesFromcardJsonArray(cardsHaving)
	cardsNamesWhichAreDonatable = service.getCardsNamesFromcardJsonArray(cardsWhichAreDonatable)
	cardsNamesNotUnlocked = service.cardsWhichAreNotUnlocked(cardsNamesHaving, allCardsNames)
	
	cardDetails = {	
					"cardsHaving": cardsNamesHaving, 
					"cardsNotUnlocked": cardsNamesNotUnlocked, 
					"cardsWhichAreDonatable": cardsNamesWhichAreDonatable
				}

	cardDetailsJson = json.dumps(cardDetails)
	return cardDetailsJson
	

#Input 1 is a playerTag
#Input 2 is a json consisting of "cardsNeeded" and "cardsWillingToDonate" by the player
#Storing the cards needed and donatable by a particular player
def setCardsTradeDetails(playerTag, cardTradeDetails):
	cardsNeeded = cardTradeDetails['cardsNeeded']
	cardsWillingToDonate = cardTradeDetails['cardsWillingToDonate']
	service.saveCardsNeededForParticularPlayer(playerTag,cardsNeeded)
	service.saveCardsWhichAreDonatableByParticularPlayer(playerTag,cardsWillingToDonate)
	
	
#Returning the output cardsNeededBy JsonArray
def getCardsNeededBy():
	return cardsNeededBy
	

#Returning the output cardsDonatableBy JsonArray
def getCardsDonatableBy():
	return cardsDonatableBy
	

