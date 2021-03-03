from flask import Flask, jsonify, request
from modules import makerequest

app = Flask(__name__)
Q = makerequest.search()


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/', methods=['GET'])
def querySearch():
    query = request.args.get('query', default='', type=str)
    return jsonify(Q.searchQuery(query))


if __name__ == '__main__':
    app.run(host="localhost", port=9000, debug=True)
