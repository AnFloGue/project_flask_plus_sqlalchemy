from flask_sqlalchemy import SQLAlchemy


"""
This script defines the database models for users and movies in a Flask web application.
It sets up the User and Movie classes, which represent the tables in the SQLite database.
Each user can have multiple movies, and each movie is linked to a user.
"""


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    movies = db.relationship('Movie', backref='user', lazy=True)



class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)