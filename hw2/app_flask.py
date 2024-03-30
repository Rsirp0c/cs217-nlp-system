from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import ner

# Initialize the Flask app & the SQLite database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Dependency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80), nullable=False)
    dependency = db.Column(db.String(120), nullable=False)
    head = db.Column(db.String(120), nullable=False)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('form2.html', input=open('input.txt').read())
    
@app.get('/get')
def index_get():
    return render_template('form2.html', input=open('input.txt').read())

@app.post('/post')
def index_post():
    text = request.form['text']
    doc = ner.SpacyDocument(text)
    entities_markup = doc.render_entities_HTML()
    dependencies_markup = doc.get_dependency()
    markup_paragraphed = ''
    for line in entities_markup.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line

    # Save to SQLite database
    for entity in dependencies_markup:
        db.session.add(Dependency(word=entity[0], dependency=entity[1], head=entity[2]))
    db.session.commit()

    # Read from SQLite database
    dependencies = Dependency.query.all()

    markup_paragraphed += '''
    <style>
        table {
            border-collapse: collapse;
            margin: auto; /* Center the table horizontally */
            width: 80%; /* Set the width of the table */
            height: 200px; /* Set the height of the table */
        }
        td, th {
            padding: 10px; /* Add padding to cells for better readability */
        }
        tr:first-child {
            background-color: #f0f0f0; /* Highlight the background color of the first row */
            font-weight: bold; /* Make the text bold for the first row */
        }
    </style>
<table >
    <tr>
        <th style="border: 1px solid black;">Word</th>
        <th style="border: 1px solid black;">Dependency</th>
        <th style="border: 1px solid black;">Head</th>
    </tr>
'''
    for dependency in dependencies:
        markup_paragraphed += f'''
        <tr>
            <td style="border: 1px solid black;">{dependency.word}</td>
            <td style="border: 1px solid black;">{dependency.dependency}</td>
            <td style="border: 1px solid black;">{dependency.head}</td>
        </tr>
'''
    markup_paragraphed += '</table>'

    return render_template('result2.html', markup=markup_paragraphed)

if __name__ == '__main__':
    with app.app_context():
       db.create_all()
    app.run(debug=True)
