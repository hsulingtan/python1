#Flask hello world#
from flask import Flask

#create application object
app = Flask(__name__)

# error handling
app.config["Debug"] = True

#use the decorator pattern to link the view fn to url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, world???!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
	    return "Hello, {}".format(name)
	else:
	    return "Not found", 404

#start the development server using the run() method
if __name__ == "__main__":
	app.run()