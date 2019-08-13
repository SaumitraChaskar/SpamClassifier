from flask import Fask
app = Flask(__name__)


@app.route('/sample')
def running():
	return "Flask is running"