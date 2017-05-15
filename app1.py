#Flask hello world#
from flask import Flask

#create application object
app = Flask(__name__)

#dynamic route
@app.route("/")
@app.route("/test/<search_query>")
@app.route("/integer/<int:value>")
@app.route("/float/<float:value>")
@app.route("/path/<path:value>")

#define the view using a function, which returns a string
def search(search_query):
    return search_query

def int_type(value):
	print(value+1)
	return "correct"

def float_type(value):
	print (value + 1)
	return "correct"

def path_type(value):
	print(value)
	return "correct"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()