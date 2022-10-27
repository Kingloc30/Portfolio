"""
Flask site that hosts a webpage with working contact form and database
"""
# hekki
import email
from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    this_dir = os.path.dirname(os.path.realpath(__file__)) # these lines needed for windows. my linux machine worked without them
    file_path = os.path.join(this_dir, 'database.txt')
    with open(file_path, mode ='a', encoding='UTF-8') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    this_dir = os.path.dirname(os.path.realpath(__file__)) # these lines needed for windows. my linux machine worked without them
    file_path = os.path.join(this_dir, 'database.csv')
    with open(file_path, mode ='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again'



