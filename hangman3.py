from hangman2 import PHOTO1,PHOTO2,PHOTO3,PHOTO4,PHOTO5,PHOTO6,PHOTO7
old_letters = []
HANGMAN_PHOTOS = {1: PHOTO1,2: PHOTO2, 3:PHOTO3, 4: PHOTO4, 5: PHOTO5, 6: PHOTO6, 7: PHOTO7 }

def start():
    """this function starts the sequence of the game presenting the logo and starting data"""
    HANGMAN_ASCII_ART = """Welcome to the game hangman \n
    | |  | |                                       
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/ """
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


def check_valid_input(letter_guessed, old_letter_guessed):
    """This function validates the input the user enters for the character he wants to say,if the input meets the criteria then
    the function returns true,and if it doesnt then the function returns false
    :param letter_guessed: is the character the user enters
    :type letter_guessed: str
    :param old_letter_guessed: is the list that is of old guesses
    :type old_letter_guessed: list
    :return this function returns whether the input is correct or not
    :rtype bool"""
    
    if len(letter_guessed) >= 2 or letter_guessed.isalpha() == False or letter_guessed in old_letter_guessed:
        try_update_letter_guessed(letter_guessed, old_letter_guessed)
        return False 
    if len(letter_guessed) == 1 and letter_guessed.isalpha() == True and letter_guessed not in old_letter_guessed:
        try_update_letter_guessed(letter_guessed, old_letter_guessed)
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function updates the list old_letters with the letters that the user enters
    : param letter_guessed: the letter the user enters that is being added to the old_letters list
    : type letter_guessed: str
    : param old_letters_guessed: the list that the onput is being added to 
    : type old_letters_guessed: list"""
    if letter_guessed not in old_letters_guessed:
        old_letters.append(letter_guessed.lower())
        print(old_letters_guessed)    
    elif letter_guessed in old_letters_guessed:    
        print('X')
        print('->'.join(old_letters))
    
def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the hidden word, before the user discovers the letters it shows blank lines
    : type secret word: str
    : param old_letters_guessed: the list where it checks if the letters are in 
    : type old_letters_guessed: list"""
    blank =[" _"]*len(secret_word)
    i=0
    while (i<len(secret_word)):
        for letter in old_letters_guessed:
            for x in range(len(secret_word)):
                if(secret_word[x]==letter):
                    blank[x]=letter
        i += 1
    the_word = ''.join(blank)
    print(the_word)
    return the_word

def check_win(secret_word, old_letters_guessed):
    """this function checks if the user has won
    : param secret_word: the word that the user chose
    : type secret_word: str
    : param old_letters_guessed: the list
    : type old_letters_guessed: list
    :return: if the user has won or not
    :rtype: bool"""
    i = 0
    a = 0
    while (i<len(secret_word)):
            for letter in old_letters_guessed:
                if letter in secret_word:
                    a += 1
                i += 1

    if a == len(secret_word):
        return True
    else:
        return False

def print_hangman(num_of_tries):
    """this function shows the state of the hangman according to the number of tries left
    : param num_of_tries: shows how many tries are left for the user
    : type num_of_tries: int"""
    if num_of_tries == 0:
        print(HANGMAN_PHOTOS[7])
    if num_of_tries == 1:
        print(HANGMAN_PHOTOS[6])
    if num_of_tries == 2:
        print(HANGMAN_PHOTOS[5])
    if num_of_tries == 3:
        print(HANGMAN_PHOTOS[4])
    if num_of_tries == 4:
        print(HANGMAN_PHOTOS[3])
    if num_of_tries == 5:
        print(HANGMAN_PHOTOS[2])
    if num_of_tries == 6:
        print(HANGMAN_PHOTOS[1])

def choose_word(file_path, index):
    """this function lets the user select whih file the word is taken from and what index the word is in
    : param file_path: the file path in which the word list is in
    : type file_path: str
    : param index: the index of the word in the file
    : type index :int
    : return: the tuple of length the the word"""
    f1 = open(file_path, 'r')
    content = f1.read().split()
    new_list = []
    [new_list.append(x) for x in content if x not in new_list]
    length = len(new_list)
    if (index - 1) > length:
        new_index = 0 
    else:
        new_index = index - 1
    new_tuple = (length, new_list[new_index])
    return new_tuple


def main():
    start()
    num_of_tries = 6
    i = 0 
    file_path = input('please enter the file path for the secret word list: ')
    index = int(input('please enter the index for the secret word'))
    user_word_length , user_word = choose_word(file_path, index)
    print('_ '*len(str(user_word)))
    print(HANGMAN_PHOTOS[1])
    while i < 6:
        user_input = input('Please type in a character: ')
        output = check_valid_input(user_input.lower(),old_letters)
        print(output)
        test = show_hidden_word(user_word,old_letters)
        if user_input not in user_word:
            i += 1
            num_of_tries -= 1
            print_hangman(num_of_tries)
        print('you have {} tries left'.format(num_of_tries))
        if test == user_word:
            print('WIN')
            break
        elif num_of_tries == 0 and check_win(user_word, old_letters) == False:
            print('lose')
            break
if __name__ == '__main__':
    main()