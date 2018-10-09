from cardTradableDetails import cardsNeededBy
from cardTradableDetails import cardsDonatableBy
import httpService
import service
import json


if __name__ == "__main__":

    #the below is a temporary main function which will be edited later
    playerTag='22R9GYCR'
    json_data = httpService.getPlayer(playerTag)
    cardArray=service.getCardsDetailsFromPlayerJsonAsArray(json_data)
    service.saveCardsNeededForParticularPlayer(playerTag,['Three Musketeers','Mortar','Bats','Archers','Barbarians','Elixir Collector','P.E.K.K.A'])
    cardJsonArrayUpdated=service.filterCardsBasedOnAvailabilityForTrade(cardArray)
    cardJsonArrayUpdated=service.filterCardsByExcludingCardsNeededByPlayer(cardJsonArrayUpdated, ['Three Musketeers','Mortar','Bats','Archers','Barbarians','Elixir Collector','P.E.K.K.A'])
    cardNamesListOfDonatableCards = service.getCardsNamesFromcardJsonArray(cardJsonArrayUpdated)
    service.saveCardsWhichAreDonatableByParticularPlayer(playerTag,cardNamesListOfDonatableCards)

    print '\n\nAll the cards which someone needs:'
    for i in cardsNeededBy:
        print i
    print '-----------\n\n'
    print 'Displaying all the cards which someone can donate:'
    for i in cardsDonatableBy:
        print i

    print '-------------------\n\n'
    
    print 'Rare Cards:'	
    rareCards = service.filterCardsBasedOnRarity(cardArray,'Rare')
    for i in rareCards:
        print i['name']

    print '-------------------\n\n'

    print 'Displaying the cards which are not unlocked yet'
    cardNamesList = service.getAllCardsNamesAsList()
    x = service.getCardsNamesFromcardJsonArray(cardArray)
    lockedCards = service.cardsWhichAreNotUnlocked(x, cardNamesList)
    for i in lockedCards:
        print i
    
    print 'Displaying the cards which are unlocked'
    cardNamesList = service.getAllCardsNamesAsList()
    x = service.getCardsNamesFromcardJsonArray(cardArray)
    unLockedCards = service.cardsWhichAreUnlocked(x, cardNamesList)
    for i in unLockedCards:
        print i



