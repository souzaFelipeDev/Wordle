import random
def creat_word_list():
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
def pick_word(list):
    return list [random.randint(0,len(list)-1)]
class keyboard:
    def __init__(self):
        self.letters = "q w e r t y u i o p\na s d f g h j k l\nz x c v b n m\n"
        self.lKeyboard = list(self.letters)
    def out_letter(self,letter):
        for x in range(len(self.lKeyboard)-1):
            if self.lKeyboard[x] == letter:
                self.lKeyboard[x] = " "
                break
        self.letters = "".join(str(e) for e in self.lKeyboard)
    def print_keyboard(self):
        print(self.letters)
class game_try:
    def __init__(self):
        self.word = pick_word(creat_word_list()).lower()
        self.word_list = list(self.word)
        self.word_check = self.word_list[:]
        self.check_list = [0,0,0,0,0]
        self.key = keyboard()
        self.try_cont = 0
    def try_word(self,word_try):
        check_list = [0, 0, 0, 0, 0]
        word_check = self.word_list[:]
        if word_try == self.word:
            return [2,2,2,2,2]
        else:
            ind = True
            word_try_list = list(word_try)
            for x in range(5):
                for y in range(5):
                    if word_try_list[x] == word_check[y]:
                        if y == x:
                            check_list[y] = 2
                            word_check[y] = ''
                            break
            for x in range(5):
                for z in range(5):
                    if word_try_list[x] == word_check[z]:
                        check_list[x] = 1
                        word_check[z] = ''
                    if word_try_list[x] == self.word_list[z]:
                        ind = False
                if ind:
                    self.key.out_letter(word_try_list[x])
                else:
                    ind = True
            return check_list
def word_test(word):
    test = True
    if len(word) != 5:
        test = False
    return test


def main():
    match = general_game  = True
    while general_game:
        game = game_try()
        test = continue_option = True
        print(game.word)
        while match:
            if game.try_cont > 5:
                print("you lose")
                break
            print("Type a 5 letter word\n")
            game.key.print_keyboard()
            while test:
                user_try = input().lower()
                if word_test(user_try):
                    test = False
                else:
                    print("This is not a 5-letter word, type again\n")
                    game.key.print_keyboard()
            test = True
            result = game.try_word(user_try)
            if result  == [2,2,2,2,2]:
                print("you win")
                break
            print(result)
            game.try_cont += 1
        while continue_option:
            print("You want to play again? Y/N")
            game_continue = input().upper()
            if game_continue == "N":
                continue_option = general_game = False
            elif game_continue == "Y":
                continue_option = False
            else:
                print("Type a valid answer")

main()


