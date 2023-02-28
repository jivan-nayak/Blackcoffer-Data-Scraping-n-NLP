import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def analyse_readability(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]

    # Calculate the number of words and sentences
    num_words = len(words)
    num_sentences = len(sentences)

    # Calculate the average sentence length
    avg_sentence_length = num_words / num_sentences




    # print("Gunning Fox Index:", gunning_fox_index)

    # Calculate the total number of words and sentences
    total_words = sum(len(sentence) for sentence in words)
    total_sentences = len(sentences)

    # Calculate the average number of words per sentence
    avg_words_per_sentence = total_words / total_sentences



    return avg_sentence_length, avg_words_per_sentence
