import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name = Column(String(250))
    description = Column(Text, nullable=False)
    climate = Column(String, nullable=False)
    population = Column(Integer)
    terrain = Column(String(250), nullable=False)
    diameter = Column(Float)
    surface_water = Column(Integer)
    orbital_period = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    birth_year = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250))
    name = Column(String(250))
    description = Column(Text, nullable=False)
    model_name = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    price = Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String(250))
    body = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment = Column(Text)
    created_at = Column(DateTime)

class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    user = relationship(Users)

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')