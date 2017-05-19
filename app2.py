#Flask hello world#
from flask import Flask

#create application object
app = Flask(__name__)

#dynamic route
@app.route("/")

@app.route("/float/<float:value>")


#define the view using a function, which returns a string


def float_type(value):
	print (value + 1)
	return "correct"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()