#!/usr/bin/python3
"""
all cities order by city.id
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for cities, state in query:
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
    session.close()
