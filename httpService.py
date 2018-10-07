import httpCalls

protocol='https'
apiDomain='api.royaleapi.com'
baseUrl=protocol + '://' + apiDomain + '/'

def getPlayer(tag):
	return httpCalls.get(baseUrl + 'player/' + tag)
	
def getClan(tag):
	return httpCalls.get(baseUrl + 'clan/' + tag)
	
def searchTournaments(searchString):
	return httpCalls.get(baseUrl + 'tournaments/search?name=' + searchString)
	
	
