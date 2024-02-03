import random
def main():
    word = pickWord(genWords()).lower()
    wordList = list(word)
    print(word)
    wordCheck = wordList[:]
    userTryList = ["aaaaa"]
    checkList = [0,0,0,0,0]
    key = keyboard()
    A = B = ind = True
    while B:
        print("Type a 5 letter word\n")
        key.kPrint()
        while A:
            userTry = input().lower()
            if len(userTry) != 5:
                print("This is not a 5 letter word, type again\n")
                key.kPrint()
            elif userTry in userTryList:
                print("Have you already typed this word\n")
                key.kPrint()
            else:
                A = False
        userTryList.append(userTry)
        if userTry == word:
            print("you win")
            break
        A = True
        wordTry = list(userTryList[-1])
        for x in range(5):
            for y in range(5):
                if wordTry[x] == wordCheck[y]:
                    if y == x:
                        checkList[x] = 2
                        wordCheck[x] = ''
                        break
        for x in range(5):
            for z in range(5):
                if wordTry[x] == wordCheck[z]:
                    checkList[x] = 1
                    wordCheck[z] = ''
                if wordTry[x] == wordList[z]:
                    ind = False
            if ind:
                key.outLetter(wordTry[x])
            else:
                ind = True
        print(checkList)
        checkList = [0,0,0,0,0]
        wordCheck = wordList [:]
def genWords():
    file = open("Words.txt")
    words = file.read()
    file.close()
    wordFlist = []
    wordList = []
    word = ""
    for x in words:
        if x != " " and x != "\n" and x != "\t" or x == "":
            wordFlist.append(x)
        if len(wordFlist) == 5:
            for j in wordFlist:
                word = word + j
            wordList.append(word)
            word = ""
            wordFlist = []
    return wordList
def pickWord(list):
    return list [random.randint(0,len(list)-1)]
class keyboard:
    def __init__(self):
        self.letters = "q w e r t y u i o p\na s d f g h j k l\nz x c v b n m\n"
        self.lKeyboard = list(self.letters)
    def outLetter(self,letter):
        for x in range(len(self.lKeyboard)-1):
            if self.lKeyboard[x] == letter:
                self.lKeyboard[x] = " "
                break

        self.letters = "".join(str(e) for e in self.lKeyboard)
    def kPrint(self):
        print(self.letters)
main()


