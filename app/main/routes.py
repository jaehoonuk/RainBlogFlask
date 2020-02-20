from flask import render_template, flash, redirect, request

from app import db
from app.main import bp
from app.main.forms import SignupForm
from app.models import User, Forecast, City


@bp.route('/')
@bp.route('/<name>')
def index(name='rain'):
    forecasts = Forecast.query.join(City).with_entities(Forecast.forecast, Forecast.comment, Forecast.datetime, City.city_name.label('city_name')).all()
    return render_template('index.html', name=name, forecasts=forecasts)


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect('/')
    return render_template('signup.html', form=form)

@bp.route('/search', methods=['POST', 'GET'])
def search():
    term = request.form['q']
    if term == "":
        flash("Enter a search query!")
        return redirect('/')
    results = Forecast.query.filter(Forecast.forecast.contains(term)).all()
    if not results:
        flash("No forecasts found.")
        return redirect('/')
    return render_template('index.html', forecasts=results)
