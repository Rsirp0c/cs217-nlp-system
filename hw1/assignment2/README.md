# spaCy - web server

## Description
This project is a simple web server that uses the spaCy library to perform Named Entity Recognition (NER) and Dependency Parsing (DEP) on a given text. The server is implemented using `Flask`, `Sqlite`.

## Requirements
- Python version: 3.11.4

## How to run
- app_flask.py
  - `python3 app_flask.py`
  - load the page at `http://localhost:5000`
  

## Dependencies
To run this code, you need to install the following modules:

- `app_flask.py`
  - flask
  - flask_sqlalchemy

- `ner.py`
  - io
  - spacy
  - spacy_streamlit
  - displacy - `from spacy import displacy`
