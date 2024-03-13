from flask import Flask, request, render_template
import pandas as pd
import ner

app = Flask(__name__)

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
    df = pd.DataFrame(dependencies_markup, columns=['Word', 'Dependency', 'Head'])

    html_table = df.to_html(index=False)
    for line in html_table.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line
    return render_template('result2.html', markup=markup_paragraphed)


if __name__ == '__main__':

    app.run(debug=True)