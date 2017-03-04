from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	template = "index.html"
	return render_template(template)


#if this script is being run from the command line
if __name__=="__main__":
#fire up the Flask test server
    app.run(debug=True,use_reloader=True)


