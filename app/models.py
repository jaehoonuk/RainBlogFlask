from app import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class City(db.Model):
    __tablename__ = 'city'

    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.Text)

    def __repr__(self):
        return '<City {}>'.format(self.name)


class Forecast(db.Model):
    __tablename__ = 'forecast'

    forecast_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.Text)
    forecast = db.Column(db.Text)
    comment = db.Column(db.Text)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return '<Forecast {}>'.format(self.name)
