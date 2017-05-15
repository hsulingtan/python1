#Flask hello world#
from flask import Flask

#create application object
app = Flask(__name__)

#dynamic route
@app.route("/")
@app.route("/test/<search_query>")

#define the view using a function, which returns a string
def search(search_query):
    return search_query

#start the development server using the run() method
if __name__ == "__main__":
	app.run()