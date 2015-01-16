# within the flask app import the Flask class
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return '<h3>Hello World Champion!</h3>'
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)