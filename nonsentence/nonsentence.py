import string
import random

def newSentence(sentenceMinLength, sentenceMaxLength, wordMinLength, wordMaxLength):
    letters = string.ascii_letters

    # Create consonant and vowel list
    vowels = [letter for letter in string.ascii_lowercase if letter in "aeiou"]
    conson = [letter for letter in string.ascii_lowercase if letter not in "aeiou"]

    while True:
        word = []
        sentence = []
        sentenceStr = ""

        for i in range(random.randint(sentenceMinLength, sentenceMaxLength)):
            for n in range(random.randint(wordMinLength,wordMaxLength)):
                if n % 2 == 0:
                    word.append(random.choice(conson))
                else:
                    word.append(random.choice(vowels))
            
            sentence.append("".join(word))
            word = []
            
        sentenceStr = ' '.join(sentence) + "."
        return(sentenceStr)