import nltk
from nltk.tokenize import word_tokenize


def clean_text(text):
    with open('stop-words/StopWords_Auditor.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_Currencies.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_DatesandNumbers.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_Generic.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_GenericLong.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_Geographic.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    with open('stop-words/StopWords_Names.txt', 'r') as file:
        content = file.read().strip()
        # Remove the content of the file from the current paragraph text
        updated_paragraph = text.replace(content, '')

    return updated_paragraph


def analyse(text):
    positive_content = ""
    negative_content = ""
    positive_score = 0
    negative_score = 0
    updated_paragraph = clean_text(text)
    tokens = word_tokenize(updated_paragraph)

    with open('master-dictionary/positive-words.txt', 'r') as file:
        positive_content = file.read()

    with open('master-dictionary/negative-words.txt', 'r') as file:
        negative_content = file.read()

    for word in tokens:
        if word in positive_content:
            positive_score += 1
        elif word in negative_content:
            negative_score += 1

    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(updated_paragraph) + 0.000001)

    return polarity_score, subjectivity_score, positive_score, negative_score
