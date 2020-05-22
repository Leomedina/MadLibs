from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret-Key"


debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('form.html', prompts= story.prompts)

@app.route('/madlibs')
def show_madlibs():
    key_lists = request.args

    return render_template('madlibs.html', story_answer=story.generate(key_lists))
