from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('0-index.html')


if "__main__" == "__main__":
	app.run(debug=True)