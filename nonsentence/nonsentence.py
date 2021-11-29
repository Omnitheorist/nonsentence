import string
import random


# Create consonant and vowel list
vowels = [letter for letter in string.ascii_lowercase if letter in "aeiou"]
consonants = [letter for letter in string.ascii_lowercase if letter not in "aeiou"]


def new_sentence(sentence_length, word_min_length, word_max_length):
    word = []
    sentence = []

    for _ in range(sentence_length):
        for n in range(random.randint(word_min_length, word_max_length)):
            if n % 2 == 0:
                word.append(random.choice(consonants))
            else:
                word.append(random.choice(vowels))

        sentence.append("".join(word))
        word = []

    return " ".join(sentence).capitalize() + "."
