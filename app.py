import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(os.environ.get('DR_DATABASE_USER'))
    return {
        'status': 'ok',
    }, 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
