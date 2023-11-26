from keyword_extractor import *
from working_utilities import *
import matplotlib.pyplot as plt
import math


class DiagnosisClass:
    def __init__(self, description, symptom_list, max_support):
        self.description = description
        self.symptom_list = symptom_list
        self.max_support = max_support


def output_generator_function(input_symptoms_parameter, result_dictionary_parameter):
    input_symptom_list = spacy_extractor(input_symptoms_parameter)
    input_symptom_set = set(input_symptom_list)
    match_list = []
    match_count_list = []
    return_list = []
    for key in result_dictionary_parameter:
        key_set = set(key)
        check_flag = 0
        for diagnosis in diagnosis_list:
            if diagnosis in key_set:
                check_flag = 1
                break
        if check_flag:
            match_count = 0
            for element in key_set:
                if element in input_symptom_set:
                    match_count = match_count + 1
            if match_count:
                match_count_list.append(match_count)
                match_list.append([key_set, match_count, result_dictionary_parameter[key][0]])
    for match_item in match_list:
        if match_item[1] == max(match_count_list):
            return_list.append(match_item)
    return return_list


def printing_and_plotting_list_generator(item_list, total_records):
    diagnosis_collector = []
    diagnosis_objects = []
    for item_object in item_list:
        for string_item in item_object[0]:
            if string_item in diagnosis_list:
                diagnosis_collector.append(string_item)
    diagnosis_set = set(diagnosis_collector)
    diagnoses_with_symptoms = []
    for diagnosis in diagnosis_set:
        symptom_collector = []
        support_count_collector = []
        found_count = 0
        for item_object in item_list:
            if diagnosis in item_object[0]:
                for string_item in item_object[0]:
                    if string_item != diagnosis:
                        symptom_collector.append(string_item)
                support_count_collector.append(item_object[2])
                found_count = found_count + 1
        support_max = math.ceil((float(max(support_count_collector))/total_records)*100)
        diagnosis_object_item = DiagnosisClass(diagnosis, set(symptom_collector), support_max)
        diagnoses_with_symptoms.append([diagnosis, set(symptom_collector), support_max])
        diagnosis_objects.append(diagnosis_object_item)
    diagnosis_objects.sort(key=lambda x: x.max_support, reverse=True)
    return [diagnoses_with_symptoms, diagnosis_objects]


def print_statement_generator(print_list, total_records):
    counter = 0
    print_return_list = []
    print("The following diagnoses are possible:\n")
    print_return_list.append("The following diagnoses are possible:\n")
    for diagnosis_item in print_list:
        counter = counter + 1
        print("Diagnosis " + str(counter) + ": \n")
        print_return_list.append("Diagnosis " + str(counter) + ": \n")
        print(diagnosis_item[0] + " associated with the following symptoms:\n")
        print_return_list.append(diagnosis_item[0] + " associated with the following symptoms:\n")
        for symptom in diagnosis_item[1]:
            print(symptom)
            print_return_list.append(symptom)
        print("\nMaximum support: " + str(diagnosis_item[2]) + "% of all patients surveyed\n")
        print_return_list.append("\nMaximum support: " + str(diagnosis_item[2]) + "% of all patients surveyed\n")
    print("A total of " + str(total_records) + " patients have been surveyed.\n")
    print_return_list.append(("A total of " + str(total_records) + " patients have been surveyed.\n"))
    if len(print_return_list) == 2:
        print("No results found.\n")
        print_return_list.append("No results found.\n")
    return print_return_list


def plot_generator(plot_list, path_to_save=0):
    plt.rc('font', size=5)
    key_list = []
    value_list = []
    for list_item in plot_list:
        key_list.append(list_item[0])
        value_list.append(list_item[2])
    fig = plt.figure(figsize=(10, 5))
    plt.bar(key_list, value_list, color='maroon', width=0.1)
    plt.xlabel("Diagnoses")
    plt.ylabel("Maximum support")
    plt.title("Diagnoses and the corresponding maximum support of each")
    if not path_to_save:
        plt.show()
    else:
        fig.savefig(path_to_save)
