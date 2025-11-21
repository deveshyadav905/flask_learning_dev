
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello Friends! it's Day 1"

@app.route("/contact")
def contact():
	con_details = {'Name':'Devesh Yadav','Phone No.':'+917060693600','Email':'deveshyadav7060@gmail.com'}
	return con_details

@app.route("/about")
def aboute():
	return  "Hello, I'm Python Developer, Experties in Web Scraping!"

@app.route("/hello/<name>")
def hello():
	name = request.args.get('name','Guest')
	return jsonify(status = "oK",message = f"Hello {name.title()} Welcome to Flask Development!")
	

if __name__ == "__main__":
	app.run(debug=True)
