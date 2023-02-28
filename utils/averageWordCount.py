import nltk

def count_avg_word_length(text):
    words = nltk.word_tokenize(text)
    total_length = sum(len(word) for word in words)
    avg_word_length = total_length / len(words)
    return avg_word_length
