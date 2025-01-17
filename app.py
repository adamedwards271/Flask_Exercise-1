from datetime import date
from unicodedata import name
from urllib import request
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
global studentOrganisationDetails 
# Assign default 5 values to studentOrganisationDetails for Application  3.

studentOrganisationDetails = {'Name': 'Organisation',}


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html

    return render_template('index.html', currentDate = datetime.utcnow().replace(microsecond=0).isoformat(' '))


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display calculateHome.html page
    
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    number = str(number)
    if len(number) == 0:
        evenOdd = 'No number provided'
    elif int(number)%2 != 0:
        evenOdd = 'Number ' + number + ' is odd'
    elif int(number)%2 == 0:
        evenOdd = 'Number ' + number + ' is even'
    else:
        evenOdd = 'Provided input is not an integer!'

    # Write your to code here to check whether number is even or odd and render result.html page
    return render_template('result.html', evenOdd = evenOdd)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrganisation = request.form['organisation']
    
    studentOrganisationDetails[studentName] = studentOrganisation
    
    return render_template('StudentDetails.html', studentOrganisationDetails = studentOrganisationDetails)

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
