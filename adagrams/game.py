import random

def build_letter_pool():
    
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }

    letter_pool = []

    for letter, frequency in LETTER_POOL.items():
        for num in range(frequency):
            letter_pool.append(letter)
    # print(letter_pool)
    return letter_pool
    

def draw_letters():
    letter_pool = build_letter_pool()
    letters = random.sample(letter_pool, 10)
    # print(letters)
    return letters
    # pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


draw_letters()