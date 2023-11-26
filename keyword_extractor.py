import re
from symptoms_and_diagnoses import *
from search_function import *


def keyword_list_generator(keyword_string):
    sublist = []
    for symptom in symptom_dictionary:
        if re.findall(symptom_dictionary[symptom], keyword_string.lower()):
            sublist.append(symptom)
    return sublist


def spacy_extractor(sample_text):
    sample_text = sample_text.lower()
    doc = nlp(sample_text)
    non_stop_words = []

    for token in doc:
        if (not token.is_stop) and token.is_alpha:
            non_stop_words.append(token)

    found_word_list = []
    for token in non_stop_words:
        found_word_list.append(token.text)
    
    symptom_set = search_function(found_word_list)
    return_list = list(symptom_set)
    return return_list
