from flask import Flask

app = Flask(__name__)

### Home page
@app.route("/")
def home():
    html = """
        <h1>Welcome to my home page</h1>
        <p>Click the link below to navigate</p>
        <a href="/about">Go to about page</a>
        <a href="/contact">Go to contacts page</a>
    """
    return html

### About page
@app.route("/about")
def about():
    html = """
        <h1>Welcome to my about page</h1>
        <p>I'm an epic coder</p>
        <a href="/">Go to home page</a>
        <a href="/contact">Go to contacts page</a>
    """
    return html

@app.route("/contact")
def contact():
    html = """
        <h1>Welcome to my contacts page</h1>
        <p>Please ring or message me on 0000 000 000</p>
        <p>Please email me at flask.example@email.com</p>
        <a href="/">Go to home page</a>
        <a href="/about">Go to about page</a>
    """
    return html

app.run(debug=True, port=5000)