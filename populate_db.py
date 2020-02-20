from app.models import User, Forecast, City
from app import db


def populate_db():
    """Populates the rain.db database if it is empty

    :return: None
    """

    if not User.query.first():
        db.session.add_all([User(user_id=123, username='Bart', email='bart@fox.com'),
                            User(user_id=404, username="Ralph", email="ralph@fox.com"),
                            User(user_id=456, username="Milhouse", email="milhouse@fox.com"),
                            User(user_id=888, username="Lisa", email="lisa@fox.com")])

    if not City.query.first():
        db.session.add_all([City(city_id=10001, city_name="London"),
                            City(city_id=10002, city_name="Seoul")])

    if not Forecast.query.first():
        db.session.add_all([Forecast(forecast_id=1234, datetime="2020-02-20", forecast="Sunny", comment="Today is a very sunny day",
                                     city_id=10001, user_id=123),
                            Forecast(forecast_id=1235, datetime="2020-02-19", forecast="Cloudy", comment="Very cloudy, no sun.",
                                     city_id=10002, user_id=404),
                            Forecast(forecast_id=1236, datetime="2020-02-18", forecast="Windy", comment="Wind speed 50 mph!",
                                     city_id=10001, user_id=888)
                            ])

    db.session.commit()
