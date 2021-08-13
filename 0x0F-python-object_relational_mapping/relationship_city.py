#!/usr/bin/python3
""" City class:

    No change """
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ City Object"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
