# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    Yes = False
    tmp = ''
    for i in range(0,len(letters_guessed)):
        tmp = tmp+letters_guessed[i]
    if tmp == secret_word:
        Yes = True
    return Yes
   



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    mychar = '_ '
    tmp = mychar*len(secret_word)
    Guess = tmp
    Final = ''
    for i in range(0,len(secret_word)):
        for j in range(0,len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                Guess = Guess[0:2*i+1] + letters_guessed[j] + Guess[2*i+2:len(tmp)]
    for i in range(0,len(secret_word)):
        if Guess[i*2:i*2+2] == '_ ':
            Final = Final + '_ '
        else:
            Final = Final + Guess[i*2+1]
                
    return Final




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    tmp = string.ascii_lowercase
    letters_notguessed = ''
    letters_guessed = sorted(letters_guessed)
    j = 0
    for i in range(0,len(letters_guessed)):
        flag = 0
        while flag == 0:
            if letters_guessed[i] != tmp[j]:
                 letters_notguessed = letters_notguessed + tmp[j]
            else:
                flag = 1
            j = j + 1
    letters_notguessed = letters_notguessed + tmp[j:len(tmp)]     
    return letters_notguessed
 
    
    

def hangman(secret_word):

    
   
    print('Welcome to the game Hangman!')
   
    ''
    print('I am thinking of a word that is ' + str(len(secret_word))+ ' letters long.')
    print('---------')
      
    m = 3
    n = 0 
    letters_guessed = []

    Available_letters = string.ascii_lowercase
    Old_guess = '_ '*len(secret_word)
    print('You have ' + str(m) +' warning left')
    while n < 6:
        
        
        print('You have ' + str(6 -n) +' guesses left')
        print('Available letters: ' + Available_letters)

        New_letter = input('please guess a letter:')
        New_letter = New_letter.lower()
        if New_letter.isalpha():
            letters_guessed.append(New_letter)
            New_guess = get_guessed_word(secret_word, letters_guessed)
            if Old_guess == New_guess: 
                print('Oops! That letter is not in my word: ' + New_guess)
                n = n + 1
            else:
                print('Good_guess: ' + New_guess)
                Old_guess = New_guess
            Available_letters = get_available_letters(letters_guessed)
            if is_word_guessed(secret_word, letters_guessed) == True:
                print('Congradulations! You won')
                break
            else is_word_guessed(secret_word, letters_guessed) == False and n == 6:
                print('Sorry! You Lost')
        else:
            m = m - 1
            print('Oops! That is not a valid input. You have ' + str(m) +' warning left')
            if m < 0:
                n = n + 1
                

        print('----------------')    
        

    return None
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = 'apple'#choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
