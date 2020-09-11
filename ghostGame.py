

def LoadWords(scrabbleDictPath):
	scrabbleFile = open(scrabbleDictPath, "r")
	wordList = []
	for line in scrabbleFile:
		wordList.append(line)
	return wordList

def doPlayerTurn(gameString, wordList, playerOne, playerTwo):
    done = False
    while not done:
        commandString = input("Enter a letter, or #c for challenge: \n").lower()
        if commandString == "#c":
            if doChallenge(gameString, wordList):
                doLoseGame(playerTwo)
            else:
                doLoseGame(playerOne)
        elif commandString.length() == 1:
            gameString+=commandString
            if gameString in wordList:
                doLoseGame(playerOne)
                done = True
        else:
            print("Invalid Input, Try Again")
        print(gameString.upper())

def doLoseGame(playerId):
    print("Game Over, Player " + playerId + " loses")

def doChallenge(gameString, wordList):
    for word in wordList:
        if word[:(gameString.length())] == gameString:
            return False
        else:
            return True
##############################################################################
scrabbleDictPath = "Scrabble.txt"
gameString = ""
wordList = LoadWords(scrabbleDictPath)
playerOne, playerTwo = doSetup()
doPlayerTurn(gameString, wordList, )
