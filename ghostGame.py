import string
def LoadWords(scrabbleDictPath):
	scrabbleFile = open(scrabbleDictPath, "r")
	wordList = []
	for line in scrabbleFile:
		wordList.append(line.strip('\n'))
	return wordList

def doPlayerTurn(gameString, wordList, playerOne, playerTwo):
	commandString = input("Player "+ playerOne + " Enter a letter, or #c for challenge: \n").lower()
	if commandString == "#c":
		if doChallenge(gameString, wordList):
			doLoseGame(playerTwo)
			return ""
		else:
			doLoseGame(playerOne)
			return ""
	elif len(commandString) == 1:
		gameString = doTurn(gameString,wordList,playerOne,playerTwo,commandString.upper())
	else:
		print("Invalid Input, Try Again")
	print(gameString)
	return gameString

def doLoseGame(playerId):
	print("Game Over, Player " + playerId + " loses")

def doChallenge(gameString, wordList):
	for word in wordList:
		print("Challenge checking " + word)
		if word[0:(len(gameString))] == gameString:
			return False
		else:
			print(word[0:(len(gameString))])
	return True

def doSetup():
	return input("Enter Player 1 Name: "), input("Enter Player 2 Name: ")

def checkWord(word):
	for testWord in wordList:
		if testWord==word:
			return True
	return False

def doBotTurn(gameString, wordList, playerOne, playerTwo):
	print("Bot Turn Start")
	possWords = []
	letterScores = dict()
	if doChallenge(gameString,wordList):
		doLoseGame(playerTwo)
		return ""
	print("Challenge Complete")
	for word in wordList:
		if len(gameString) != 0 and word[:(len(gameString))] == gameString:
			possWords.append(word)
			print(word + " is a possibility")
	for word in possWords:
		if len(word)>len(gameString):
			found = word[len(gameString)]
			print(found + " being checked")
			if found in letterScores:
				letterScores[found] += getWordValue(word, gameString, possWords)
			else:
				letterScores[found] = getWordValue(word, gameString, possWords)

	for letter in list(string.ascii_uppercase):
		currentMaxLetter = "D"
		if currentMaxLetter not in letterScores or (letter in letterScores and letterScores[letter] > letterScores[currentMaxLetter]):
			currentMaxLetter = letter
	print (letterScores)
	gameString = doTurn(gameString, word, playerOne, playerTwo, currentMaxLetter.upper())
	print(gameString)
	return gameString



def getWordValue(word, gameString, wordList):
	turn = len(gameString)%2
	score = 0
	for testWord in wordList:
		if len(testWord)%2 == turn:
			score+=1
		else:
			score-=1
	return score

def doTurn(gameString, wordList, playerOne, playerTwo, letter):
	gameString+=letter
	if len(gameString)>3 and checkWord(gameString):
		doLoseGame(playerOne)
		return ""
	return gameString
##########################	####################################################
scrabbleDictPath = "Scrabble.txt"
gameString = ""
wordList = LoadWords(scrabbleDictPath)
playerOne, playerTwo = doSetup()
done = False
while not done:
	gameString = doPlayerTurn(gameString, wordList, playerOne, playerTwo)
	if gameString =="":
		quit()
	gameString = doBotTurn(gameString, wordList, playerTwo, playerOne)
	if gameString =="":
		quit()
