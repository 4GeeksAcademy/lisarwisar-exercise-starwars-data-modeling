import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = "characters"
    name = Column(String(250), primary_key=True)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = "planets"
    name = Column(String(250), primary_key=True)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)

class Items(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True)

                                                 

class Favorite_Characters(Base):
    __tablename__ = "favorite characters"
    user_character_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_name = Column(String(250), ForeignKey("character.name"))
    character = relationship(Characters)
    user = relationship(User)

class Favorite_Planets(Base):
    __tablename__ = "favorite planets"
    user_planer_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_name = Column(String(250), ForeignKey("planet.name"))
    user = relationship(User)
    planet = relationship(Planets)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
