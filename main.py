import pandas as pd
from bs4 import BeautifulSoup
import requests
import string
from utils.sentimentAnalysis import analyse
from utils.readabiityAnalysis import analyse_readability
from utils.pronounAnalysis import analyse_pronoun
from utils.complexWordAnalysis import calculate_complex_word_percentage
from utils.averageWordCount import count_avg_word_length
from utils.cleanedWords import count_cleaned_words
from utils.outputData import write_to_excel

# Open the Excel file
excel_file = pd.read_excel('Input.xlsx')

# List of all URLS
url_list = []
url_id = []

# Loop through the columns and print their names and values
for data in excel_file.URL:
    url_list.append(data)

for id_ in excel_file.URL_ID:
    url_id.append(str(id_))

for i in range(len(url_list)):
    # Make a request to the web page
    url = url_list[i]
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for 4xx and 5xx status codes
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("Page not found:", url)
        else:
            print("HTTP error:", e)
        continue  # Skip to the next iteration of the loop if an error occurs

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find a specific tag and extract its text
    # title = soup.find('title').text
    # print(title)

    # Find the `h1` tag with `class="entry-title"`
    h1_entry_title = soup.find('h1', class_='entry-title')

    # Extract the text content of the `h1` tag
    if type(h1_entry_title) is not None:
        print(h1_entry_title)
        h1_text = h1_entry_title.text

        # Find the `div` tag with `class="td-post-content"`
        div_td_post_content = soup.find('div', class_='td-post-content')

        # Find all `p` tags inside the `div` tag
        p_tags = div_td_post_content.find_all('p')

        # Extract the text content of each `p` tag and concatenate them
        all_text = ""
        for p_tag in p_tags:
            all_text += p_tag.text.strip() + " "

        # Print the concatenated text
        # print(all_text)

        # Open a new file for writing
        path = "output-files/" + url_id[i] + ".txt"
        with open(path, 'w', encoding='utf-8') as file:
            # Write some text to the file
            file.write(all_text)

        # Processing the text
        polarity_score, subjectivity_score, positive_score, negative_score = analyse(all_text)
        avg_word_count = count_avg_word_length(all_text)
        cleaned_word_count = count_cleaned_words(all_text)
        avg_sentence_length, avg_words_per_sentence = analyse_readability(all_text)
        complex_words_percentage, complex_words_num, syllable_number = calculate_complex_word_percentage(all_text)
        fog_index = 0.4 * (avg_sentence_length + complex_words_percentage)
        pronoun_count = analyse_pronoun(all_text)

        print(polarity_score, subjectivity_score)

        print("Average Sentence length and average words per sentence", avg_sentence_length, avg_words_per_sentence)

        print("Pronoun Count: ", pronoun_count)

        print("Complex words and complex word percentage: ", complex_words_percentage, complex_words_num)

        print("Fog index: ", fog_index)

        print("Average word count: ", avg_word_count)

        print("Number of cleaned words: ", cleaned_word_count)

        print()

        data = [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
                complex_words_percentage, fog_index, avg_words_per_sentence, complex_words_num, cleaned_word_count,
                syllable_number, pronoun_count, avg_word_count]
        # Writing the data into the output file
        write_to_excel("Output Data Structure.xlsx", data, i)
