from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret-Key"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('form.html')

