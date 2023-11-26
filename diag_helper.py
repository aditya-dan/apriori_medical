import pickle
from data_preparation import *
from output_generator import *
from keyword_extractor import *
import time
import os
from flask import Flask

app = Flask(__name__)


def diagnose(symptoms):
    print(app.root_path)
    file_handle_1 = os.path.join(app.root_path, 'encounter.csv')
    file_handle_2 = os.path.join(app.root_path, 'encounter_dx.csv')
    apriori_result_handle = os.path.join(app.root_path, 'apriori_result')
    plot_path = os.path.join(app.root_path, 'static', 'plot.png')
    data_list = create_input_list(file_handle_1, file_handle_2)
    try:
        apriori_function_file = open(apriori_result_handle, 'rb')
    except:
        raise Exception("Model not found")
    result_dictionary = pickle.load(apriori_function_file)
    graph_img_src = "static/plot.png?" + str(time.time())
    output_list_initial = output_generator_function(symptoms, result_dictionary)
    output_list_final = printing_and_plotting_list_generator(output_list_initial, len(data_list))
    symptom_list = spacy_extractor(symptoms)
    plot_generator(output_list_final[0], plot_path)
    return [output_list_final[1], graph_img_src, ", ".join(symptom_list), symptoms]
