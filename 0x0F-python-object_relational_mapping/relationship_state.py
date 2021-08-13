#!/usr/bin/python3
""" State Class """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State Object"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
