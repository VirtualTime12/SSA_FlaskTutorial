from flask import Flask
from datetime import datetime

#Create the flask app
app = Flask(__name__)

#Home page route
@app.route("/")
def home():
    
    #Get now and format as Year-Month-Day Hour:Minute:Second
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Setup the page's html
    html = f"""
        <!doctype html>
        <html>
        <head>
            <title>Clock</title>
        </head>
        <body>
            <h1>Welcome to my clock</h1>
            <p>The current date and time is {today}</p>
        </body>
        </html>
    """
    
    #Return the html
    return html

app.run(debug=True, port=5000)