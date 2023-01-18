from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    formData = request.form.get('date')
    formData = str(formData)
    birthDate = requests.post('http://converter:5001/date/' + formData)

    prime = requests.post('http://prime:5002/date/' + formData)
  
    return render_template('convertPrime.html', formData=formData, birthDate=birthDate.text, prime=prime.text)

