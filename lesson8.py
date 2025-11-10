from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Set a variable to a value
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Set the template name to our variables
    return render_template('index.html', logged_in=True, name=nameValue, time=timeValue)

app.run(debug=True, port=5000)