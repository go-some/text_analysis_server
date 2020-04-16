import time

import spacy
import pytextrank

from flask import Flask, request, jsonify


app = Flask(__name__)


# NER
nlp = spacy.load('en_core_web_sm')
target_labels = set(['PERSON', 'ORG', 'PRODUCT', 'PERCENT', 'MONEY', 'QUANTITY'])

# TEXT-SUM
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)


@app.route('/sum', methods=['POST'])
def sum_():
    text = request.form.get('text')

    doc = nlp(text)
    sents = []
    for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=3):
        sents.append(str(sent))
    sum_text = ' '.join(sents)
    return jsonify({'status': 200, 'sum_text': sum_text })


@app.route('/ner', methods=['POST'])
def ner():
    text = request.form.get('text')
    doc = nlp(text)
    visited = set()
    ent_list = []
    for ent in doc.ents:
        if ent.label_ not in target_labels:
            continue
        if ent.text in visited:
            continue
        ent_list.append({'label': ent.label_, 'text': ent.text})
        visited.add(ent.text)

    return jsonify({'status': 200, 'ent_list': ent_list }) 
