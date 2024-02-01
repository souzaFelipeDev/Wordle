import random
def main():
    word = list("Breed")#list(pickWord(genWords()))
    wordCheck = word[:]
    keybord = "q w e r t y u i o p\na s d f g h j k l\nz x c v b n m"
    lKeyboard = list(keybord)
    userTryList = ["aaaaa"]
    checkList = [0,0,0,0,0]
    ind = 0
    x = True
    print("Type a 5 letter word")
    while x:
        userTry = input()
        if userTry.__len__() != 5:
            print("This is not a 5 letter word, type again")
        elif userTry in userTryList:
            print("Have you already typed this word")
        else:
            x = False
    userTryList.append(userTry)
    wordTry = list(userTryList[-1])
    for x in range(5):
        for y in range(5):
            if wordTry[x] == wordCheck[y]:
                if y == x:
                    checkList[y] = 2
                    wordCheck[y] = ''
                    break
        for z in range(5):
            if wordTry[x] == wordCheck[z]:
                checkList[z] = 1
                wordCheck[z] = ''
    print(checkList)
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
        if wordFlist.__len__() == 5:
            for j in wordFlist:
                word = word + j
            wordList.append(word)
            word = ""
            wordFlist = []
    return wordList
def pickWord(list):
    return list [random.randint(0,list.__len__()-1)]
main()


