import nltk
from nltk.corpus import stopwords
import string


def count_cleaned_words(text):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_text = "".join(char for char in text if char not in string.punctuation).lower()
    # Tokenize the cleaned text into words
    words = nltk.word_tokenize(cleaned_text)
    # Remove stop words from the list of words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Count the number of unique cleaned words
    unique_cleaned_words = set(words)
    cleaned_word_count = len(unique_cleaned_words)
    return cleaned_word_count
