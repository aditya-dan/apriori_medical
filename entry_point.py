from flask import render_template
from flask import request
from diag_helper import *
app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('index.html')


@app.route('/diagnose', methods=['POST'])
def show_diagnosis():
    f_name = request.form['firstname']
    l_name = request.form['lastname']
    gender = request.form['gender']
    result_string = diagnose(request.form['symptoms'])
    return render_template('results_enhanced.html', results=result_string,
                           fname=f_name, lname=l_name, gender=gender)
