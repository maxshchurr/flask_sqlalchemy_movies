from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviesdb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@dataclass()
class Actor(db.Model):
  __tablename__ = 'actors'
  pk : int
  name : str
  surname: str
  age: int
  # movie: str

  pk = Column(Integer, primary_key=True, auto_increment=True)
  name = Column(db.String(200), nullable=False)
  surname = Column(db.String(200), nullable=False)
  age = Column(db.Integer, nullable=False)

  # Связи между бд пока не разобрал
  # movie = Column(db.Integer, db.ForeignKey('movies.pk'))


@dataclass()
class Movie(db.Model):
  __tablename__ = 'movies'
  pk : int
  name : str
  release_year: int


  pk = Column(Integer, primary_key=True, auto_increment=True)
  name = Column(String(200), nullable=False)
  release_year = Column(Integer, nullable=False)

  # Связи между бд пока не разобрал
  # genres = Column(db.Integer, db.ForeignKey('genres.pk'))
  # actor = relationship('Actor')


@dataclass()
class Genre(db.Model):
  __tablename__ = 'genres'
  pk: int
  genre_type: str


  pk = Column(Integer, primary_key=True, auto_increment=True)
  genre_type = Column(String(200), nullable=False)

  # Связи между бд пока не разобрал
  # movie = relationship('Movie')


@dataclass()
class MovieGenre(db.Model):
  __tablename__ = 'movies_genres'

  pk = Column(Integer, primary_key=True, auto_increment=True)

  #Связи между бд пока не разобрал
  # movie_id = Column(Integer, ForeignKey('movies.pk'))
  # genre_id = Column(Integer, ForeignKey('genre.pk'))


@app.route('/')
def main():
  return '<h3>Main page</h3>'


@app.route('/actors')
def get_actors():
  actors = Actor.query.all()
  return jsonify(actors)


@app.route('/movies')
def get_movies():
  movies = Movie.query.all()
  return jsonify(movies)


@app.route('/genres')
def get_genres():
  genres = Genre.query.all()
  return jsonify(genres)

if __name__ == "__main__":


  movies = Movie(name='Dune', release_year=2021), Movie(name='Finch', release_year=2021),\
           Movie(name='The Dark Knight', release_year=2008), Movie(name='Gladiator', release_year=2000),\
           Movie(name='Gomorrah', release_year=2008),


  actors = Actor(name='Alex', surname='Morozov', age=29), Actor(name='Bob', surname='Maffey', age=22)
  genres = Genre(genre_type='Horror'), Genre(genre_type='Action'), Genre(genre_type='Comedy')

  db.create_all()

  db.session.add_all(actors)
  db.session.add_all(movies)
  db.session.add_all(genres)
  db.session.commit()
