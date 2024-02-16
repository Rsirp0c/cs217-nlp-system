# spaCy - web server

## Description
This project is a simple web server that uses the spaCy library to perform Named Entity Recognition (NER) and Dependency Parsing (DEP) on a given text. The server is implemented using three different web frameworks: FastAPI, Flask, and Streamlit.

## Requirements
- Python version: 3.11.4

## How to run
- app_fastapi.py
  - `uvicorn app_fastapi:app --reload`
  - Aceess the API using:
  ```bash
    - curl http:/127.0.0.1:8000
    - curl -X POST http:/127.0.0.1:8000/ner \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json  
    - curl -X POST http:/127.0.0.1:8000/dep \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json  
  ```
- app_flask.py
  - `python3 app_flask.py`
  - load the page at `http://localhost:5000`
  - 
- app_streamlit.py 
  - `streamlit run app_streamlit.py`
  - load the page at `http://localhost:8501`


## Dependencies
To run this code, you need to install the following modules:

- `app_fastapi.py`
  - fastapi
  - uvicorn
  - json
  - pydantic

- `app_flask.py`
  - flask
  - pandas

- `app_streamlit.py`
  - streamlit
  - graphviz

- `ner.py`
  - io
  - spacy
  - spacy_streamlit
  - displacy - `from spacy import displacy`
