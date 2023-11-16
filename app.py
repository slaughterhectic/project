import csv
from flask import Flask, render_template, request
from IPython.display import display, HTML

app = Flask(__name__)

# Function to perform search by name
def searchByName(name):
    with open('faculty_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result = []
        for row in csv_reader:
            if name.lower() in row['Name'].lower():
                result.append(row)
        return result

# Function to perform search by subject
def searchBySubject(subject):
    with open('faculty_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result = []
        for row in csv_reader:
            if subject.lower() in [subj.strip().lower() for subj in row['Subject'].split(',')]:
                result.append(row)
        return result

# Function to perform search by department
def searchByDepartment(department):
    with open('faculty_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result = []
        for row in csv_reader:
            if department.lower() == row['Department'].lower():
                result.append(row)
        return result

# Main route to display the search form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display search results
@app.route('/search', methods=['POST'])
def search():
    option = request.form['option']
    query = request.form['query']
    result = perform_search(option, query)
    return render_template('result.html', result=result)

# Function to dispatch the appropriate search function based on the selected option
def perform_search(option, query):
    if option == 'name':
        return searchByName(query)
    elif option == 'subject':
        return searchBySubject(query)
    elif option == 'department':
        return searchByDepartment(query)
    else:
        return []

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
