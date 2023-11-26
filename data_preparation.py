import csv
from keyword_extractor import *
from symptoms_and_diagnoses import *


def file_to_list(file_handle):
    table = []
    reader = csv.reader(file_handle)
    for row in reader:
        table.append(row)
    return table


def create_input_list(symptom_data_filename, diagnosis_data_filename):

    file1 = open(symptom_data_filename)
    file2 = open(diagnosis_data_filename)
    table1 = file_to_list(file1)
    table2 = file_to_list(file2)
    combined_table = []
    final_list = []

    for row1 in table1:
        for row2 in table2:
            if row1[1] == row2[5]:
                new_row = [row1[25], row2[3]]
                combined_table.append(new_row)

    for row in combined_table:
        sublist = keyword_list_generator(row[0])
        if row[1] in diagnosis_list:
            sublist.append(row[1])
        sublist_set = set(sublist)
        final_list.append(sublist_set)

    new_final_list = []

    for item_set in final_list:
        if len(item_set) >= 2:
            new_final_list.append(item_set)

    return new_final_list
