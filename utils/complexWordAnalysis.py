import nltk
from nltk.corpus import cmudict

nltk.download('cmudict')
cmu_dict = cmudict.dict()

def count_syllables(word):
    try:
        # Get the pronunciation of the word from the dictionary
        pronunciation = cmu_dict[word.lower()][0]
        # Count the number of syllables in the pronunciation
        syllable_count = len(list(filter(lambda x: x[-1].isdigit(), pronunciation)))
        return syllable_count
    except KeyError:
        # Return 0 if the word is not in the dictionary
        return 0

def count_complex_words(text):
    words = nltk.word_tokenize(text)
    syllable_counts = list(map(count_syllables, words))
    complex_word_count = 0
    complex_syllable_count = 0
    for i, count in enumerate(syllable_counts):
        if count >= 2:
            complex_word_count += 1
            complex_syllable_count += count
    return complex_word_count, len(words), syllable_counts, complex_syllable_count

def calculate_complex_word_percentage(text):
    complex_word_count, total_word_count, syllable_counts, complex_syllable_count = count_complex_words(text)
    complex_word_percentage = (complex_word_count / total_word_count) * 100
    average_syllables_per_word = complex_syllable_count / complex_word_count
    return complex_word_percentage, complex_word_count, average_syllables_per_word
