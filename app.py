from flask import Flask, render_template, redirect
from forms import SignupForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    return render_template('index.html', my_string="Wheeeee!")

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()
