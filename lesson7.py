from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Set a variable to a value
    nameValue = "Bob"
    # Set the template name to our variable
    return render_template('index.html', name=nameValue)

app.run(debug=True, port=5000)