# spaCy - web server

## Description
This project use `docker` to wrap three previous projects.

## Requirements
- Python version: 3.11.4
- Docker desktop or cli

## How to run
- **Streamlit and SpaCy**
  - CD into `hw3/streamlit` repo
  - run command `docker compose up`
  - go to `localhost:8501` to view it
- **Flask and SQLite**
  - CD into `hw3/flask_sql`
  - run command `docker compose up`
  - go to `localhost:5000` to view it
- **REST api and SpaCy**
  - CD into `hw3/REST` repo
  - run command `docker compose up`
  - Access the api using:
   ```bash
    - curl http://localhost:8000
   
    - curl -X POST http://localhost:8000/ner \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json
   
    - curl -X POST http://localhost:8000/dep \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d@input.json  
  ```
  


