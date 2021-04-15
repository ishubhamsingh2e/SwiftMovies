from flask import Flask, jsonify, request, render_template, redirect
from modules import makerequest
from modules import features

app = Flask(__name__)
Q = makerequest.search()
port = 9000

requestData = makerequest.search()

@app.route('/', methods = ['GET'])
def index():
    return render_template('loading.html')

@app.route('/trending', methods = ['GET'])
def home():
    return render_template('index.html',data=requestData.trending())

@app.route('/redirect', methods = ['GET', 'POST'])
def redir():
    query = request.form['query']
    return redirect(f'/find?s={query}')

@app.route('/find', methods = ['GET'])
# url =>  localhost:port/find?s=<value>
def search():
    query = request.args.get('s', default='', type=str)
    return render_template('result.html', data=requestData.searchQuery(query))

@app.route('/result')
# url =>  localhost:port/result?id=<value>
def result():
    query = request.args.get('id', type=int)
    return render_template('show.html', data=requestData.searchId(query))

@app.route('/stack', methods= ['GET'])
def stack():
    run = features.features()
    
    return render_template('stack.html', data=run.fetch_stack())

@app.route('/addstack', methods = ['POST'])
def add():
    run = features.features()
    id = request.args.get('id', type=int)
    run.create_database()
    run.add_to_stack(Q.searchId(id))
    
    return render_template('show.html', data=requestData.searchId(id))
    
    
    

''' api route's '''

@app.route('/api/search', methods=['GET'])
# url =>  localhost:port/api/search?query=<value>
def querySearch():
    query = request.args.get('query', default='', type=str)
    return jsonify(Q.searchQuery(query))

@app.route('/api/idsearch',  methods=['GET'])
# url =>  localhost:port/api/search?id=<value>
def idSearch():
	query = request.args.get('id', default='', type=int)
	return jsonify(Q.searchId(query))

@app.route('/api/trending',  methods=['GET'])
# url =>  localhost:port/api/trending
def trending():
	return jsonify(Q.trending())



if __name__ == '__main__':
    app.run(host="localhost", port=port, debug=True)
