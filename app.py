import os
import json
import settings
from flask import Flask, request
from flask_cors import CORS, cross_origin
from services.elasticsearch import init_elasticsearch
from services.drupal import init_drupal

app = Flask(__name__)
CORS(app)
es_client = init_elasticsearch()


@app.before_request
@cross_origin(allow_headers=['Content-Type', 'Token'])
def do_before_request():
    uid = request.get_json().get('uid')
    token = request.headers.get('Token')
    # Drupal Authentication
    if token is not None:
        drupal_client = init_drupal()
        cursor = drupal_client.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM dr_jcasessions WHERE uid = {uid}")
        session = cursor.fetchone()
        cursor = drupal_client.close()
        print(session[1])
        if token == session[1]:
            return {
                'status': 'success',
                'message': 'User authenticated',
            }, 200
        else:
            return {
                'status': 'error',
                'message': 'Error en el token.'
            }, 401
    else:
        return {
            'status': 'error',
            'message': 'Token inválido'
        }, 401


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    #print(test_es())
    return {
        'status': 'ok',
    }, 200


def test_es():
    res = None
    try:
        res = es_client.search(index='crm-palmas-search', query={
            "match_phrase_prefix": {
                "title": {
                    "query": "NN001465"
                }
            }
        })
    except Exception as e:
        print(e)

    return res

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
