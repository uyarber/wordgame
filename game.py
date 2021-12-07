
import random

def removePunctuation(s):
  # given a string, remove all special characters
  import string
  for c in string.punctuation:
    s= s.replace(c,"")
  return s





def loadStopList():
  # Load stopwords into a list, return list
  stopfile=open("StopWords.txt")
  stopWords=[]
  for item in stopfile:
    item=item.strip()
    stopWords.append(item)
    #takes out the lines and adds them to a list
  return stopWords






# Finish and test this function
def isStopWord(aWord,stopWords):
  # return true if aWord in the stopWords list
  stopList= True
  noList = False
  #searching for word in stopwords list
  for word in stopWords:
  #comparing each word to stopwords
    if aWord == word:
      return stopList
  #finding no stopwords its false
  return noList





#analyzes each word in the speech to see if they match stop words and put the right words in the list called words
def loadWords(speech, stopWords):
  words=[]
  for element in speech:
    result=isStopWord(element, stopWords)
    if result == False:
    #   # print(element)
      words.append(element)
  return words



#   #read all words into a list, ignoring words in stopList
#   use isStopWord to check if word is a stopword
#   Each word should be converted to lowercase so it matches the stop words

# # Test code - should pring a list of all stop words.
stopWords=loadStopList()
#creating the file into a list
def speechEdit(filename):
  speech=[]
  aline= filename.readline()
  for aline in filename:
#going into every line, then every word and making it lower case and taking out punctuation
    for item in aline.split():
      aline.split('\n')
      item=item.lower()
      for x in item:
        # print(x)
        punc = x.isalpha()
        #take out punctuation
        if punc == False:
          # print(item)
          # print(x)
          item = item.strip(x)
          # print(item)
      speech.append(item)
  return speech
#activates the function

#  for item in stopfile:
#     item=item.strip()
#     stopWords.append(item)
#   return stopWords



#puts the right lists
#prints all the words that are not on the stoplist


def countWord(aWord, speech):
#counter so that everytime the word entered is the same as a word on the list it will count one interation. If it does not match, it will see if the next word matches.
  numberOfWord = 0
  for word in speech:
    if word == aWord:
      numberOfWord = numberOfWord + 1
  return numberOfWord



# Finish this function
def pickRandomWord(speech):
  theRange = len(speech)
  x = theRange-2
  randomIndex = random.randint(0, x)
  # print(randomIndex)
  return speech[randomIndex]




print("In this game you choose the more popular word\nin President Kennedy's 1961 presidential\ninauguration speech.")
games=0
wins=0

def playerInput(word1,word2):
  # Given two words, show the user the two words
  # and ask the user which word is more common
  # The user types in a 1 for word1, a 2 for word 2
  # and a 0 if both words occur the same number of times
  # The function should check that they make a valid
  # and keep asking until they do


  print("The words are: 1.",word1,"  2.",word2)
  ans=int(input("Enter number of more common word, or 0 if the same. "))
  while (ans != 0 and ans != 1 and ans != 2):
    print("You must enter 0, 1 or 2!")
    ans=int(input("Enter number of more common word, or 0 if the same. "))
  return ans




def game(gamefilename):
  gameinfo=[]
  games=0
  wins=0
  loadStopList()
  filename= gamefilename
  speech =speechEdit(filename)
  speech = loadWords(speech, stopWords)
  word1 = pickRandomWord(speech)
  word2 = pickRandomWord(speech)
  gameinfo.append(word1)
  gameinfo.append(word2)
  ans = playerInput(word1, word2)
  aWord = word1
  word1num = countWord(aWord, speech)
  gameinfo.append(word1num)
  aWord = word2
  word2num = countWord(aWord, speech)
  gameinfo.append(word2num)
  num= decision(word1num, word2num)
  playerOutput(ans, num, gameinfo, speech, games, wins)

def gameagain(speech, games, wins):
  gameinfo=[]
  word1 = pickRandomWord(speech)
  word2 = pickRandomWord(speech)
  gameinfo.append(word1)
  gameinfo.append(word2)
  ans = playerInput(word1, word2)
  aWord = word1
  word1num = countWord(aWord, speech)
  gameinfo.append(word1num)
  aWord = word2
  word2num = countWord(aWord, speech)
  gameinfo.append(word2num)
  num= decision(word1num, word2num)
  playerOutput(ans, num, gameinfo, speech, games, wins)


def decision(word1num, word2num):

  if word1num == word2num:

    num=0
  if word1num > word2num:

    num=1
  if word1num < word2num:

    num=2
  return(num)



def playerOutput(ans, num, gameinfo, speech, games, wins):
  print(gameinfo[0], "occurs", gameinfo[2], "times")
  print(gameinfo[1], "occurs", gameinfo[3], "times")
  if ans == num:
    print("You got it right!")
    wins = wins+1
  else:
    print("Better luck next time!")
  games = games+1
  print("Score:", wins, "/", games)
  cont=input("Go again? ('y' or 'n'):")
  while cont=="y":
    gameagain(speech, games, wins)


  # 1. Load stop words file using loadx

  # 2. Load words from speech using loadWords function

  # cont="y"
  # games=0
  # wins=0
  # while cont=="y":
    # 3. Pick two random words from from the wordlist

    # 4. Count the number of occurances of each word

    # 5. show the two words and ask which is more common

    # 6. Show how how many times each word occurs

    # 7. check if they got it right or not,

    # 8. Give feed back and update score

    # 6.show the score

# speechWords= loadWords(speech, stopWords)


gamefilename=open("Kennedy1961.txt")
game(gamefilename)
