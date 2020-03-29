import time

import spacy

from flask import Flask, request, jsonify


app = Flask(__name__)

# NER
nlp = spacy.load('en_core_web_sm')
target_labels = set(['PERSON', 'ORG', 'PRODUCT', 'PERCENT', 'MONEY', 'QUANTITY'])

# TEXT-SUM
# [TODO]


@app.route('/ner', methods=['POST'])
def ner():
    text = request.form.get('text')
    doc = nlp(text)

    ent_list = []
    for ent in doc.ents:
        if ent.label_ not in target_labels:
            continue
        ent_list.append({'label': ent.label, 'text': ent.text})

    return jsonify({'status': 200, 'ent_list': ent_list }) 
