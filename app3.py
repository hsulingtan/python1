#Flask hello world#
from flask import Flask

#create application object
app = Flask(__name__)

#dynamic route
@app.route("/")
@app.route("/path/<path:value>")

#define the view using a function, which returns a string

def path_type(value):
	print(value)
	return "correct"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()