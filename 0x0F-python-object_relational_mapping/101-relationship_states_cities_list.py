#!/usr/bin/python3
""" Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).all():
        print("{}: {}". format(state.id, state.name))
        for cities in state.cities:
            print("    {}: {}".format(cities.id, cities.name))
    session.close()
