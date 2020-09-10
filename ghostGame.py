scrabbleDictPath = "Scrabble.txt"

def LoadWords():
	scrabbleFile = open(scrabble, "r")
	wordList = []
	for line in scrabbleFile:
		wordList.append(line)
	return wordList

def doPlayerTurn(gameString, wordList, playerId):
    commandString = input("").lower()
    if commandString == "challenge":
        doChallenge(gameString, wordList)
    if gameString in wordList:
        doLoseGame(playerId)

def doLoseGame(playerId):
    print("Game Over, Player " + playerId + " loses")

def doChallenge(gameString, wordList, playerId):
    for word in wordList:
        if word[0:(gameString.length())] == gameString:
            print("Challenge Failed")
            doLoseGame(playerId)
