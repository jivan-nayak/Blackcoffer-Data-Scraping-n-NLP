import nltk
import re


def analyse_pronoun(text):
    # Define a regex pattern to match personal pronouns
    pattern = r"\b(I|me|my|we|us|our|ours)\b"

    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Count the number of personal pronouns in the text
    pronoun_count = 0
    for word in words:
        # Check if the word matches the regex pattern
        if re.match(pattern, word, flags=re.IGNORECASE) and word.lower() != "us":
            pronoun_count += 1

    # # Print the result
    # print("Personal Pronoun Count:", pronoun_count)
    return pronoun_count
