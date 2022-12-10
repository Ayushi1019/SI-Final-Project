from flask import Flask, request
import requests
import json
from dotenv import load_dotenv
import os
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()

lang_url = os.getenv('LANG_RES') + ':analyze-text?api-version=2022-05-01'
key = os.getenv('API_KEY')
query_url = os.getenv('LANG_RES') + ':query-text?api-version=2021-10-01'

headers = {
        'Content-Type' : 'application/json',
        'Ocp-Apim-Subscription-Key': key
}

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SI - Final Project"
    }
)

@app.route('/detect_language',methods=["POST"])
def detect_language():
    record = json.loads(request.data)
    
    r = requests.post(url=lang_url,json=record, headers=headers)
    res = r.json()

    detected_languages = []

    for ele in res["results"]["documents"]:
        lang_obj = {
            "id" : ele["id"],
            "detected_language": ele["detectedLanguage"]["name"],
            "confidence_score" : ele["detectedLanguage"]["confidenceScore"],
            "abbv" : ele["detectedLanguage"]["iso6391Name"],
        }
        detected_languages.append(lang_obj)
    return detected_languages

@app.route('/pii',methods = ['POST'])
def pii():
    record = json.loads(request.data)
    
    r = requests.post(url=lang_url,json=record, headers=headers)
    res = r.json()

    pii_entities = []

    for ele in res["results"]["documents"]:
        
        for entity in ele["entities"]:
            curr_entity = {
                "category" : entity["category"],
                "text" : entity["text"],
                "confidence_score": entity["confidenceScore"]
            }
            pii_entities.append(curr_entity)
    return pii_entities


@app.route('/entity_linking',methods = ['POST'])
def entity_linking():
    record = json.loads(request.data)
    
    r = requests.post(url=lang_url,json=record, headers=headers)
    res = r.json()

    entities = []

    for ele in res["results"]["documents"]:
        for entity in ele["entities"]:
            curr_entity = {
                "name" : entity["name"],
                "url" : entity["url"],
                "data_source" : entity["dataSource"],
                "matches" : {"text":entity["matches"][0]["text"],"confidence_score": entity["matches"][0]["confidenceScore"]}
            }
            entities.append(curr_entity)
    return entities


@app.route('/qa',methods = ['POST'])
def qa():
    record = json.loads(request.data)
    question = record['question']

    r = requests.post(url=query_url,json=record, headers=headers)

    answers = []

    for ele in r.json()["answers"]:
        answers.append(ele["answer"])

    return {"Q":question,"A":",".join(answers)}


app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run()