from advanced_apriori import *
from data_preparation import *
from output_generator import *
import pickle
import os

data_list = create_input_list('encounter.csv', 'encounter_dx.csv')
result_dictionary = {}

if not os.path.exists('apriori_result'):
    result_dictionary = apriori_function(data_list, 10)
    with open('apriori_result', 'wb') as apriori_result_file:
        pickle.dump(result_dictionary, apriori_result_file)

else:
    with open('apriori_result', 'rb') as apriori_function_file:
        result_dictionary = pickle.load(apriori_function_file)

input_symptoms = input("Please enter a description of your symptoms: ")
output_list_initial = output_generator_function(input_symptoms, result_dictionary)
output_list_final = printing_and_plotting_list_generator(output_list_initial, len(data_list))

print("\n")

print_statement_generator(output_list_final[0], len(data_list))
plot_generator(output_list_final[0])
