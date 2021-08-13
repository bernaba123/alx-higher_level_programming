#!/usr/bin/python2
""" Class definition of State InstanceBase = declarative_base() """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True)
    name = Column(String(128),
                  nullable=False)
