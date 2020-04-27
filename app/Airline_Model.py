from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer






def add_flight(
            flight_date,
            flight_status,
            departure_airport,
            departure_timezone,
            departure_airport_iata,
            departure_time_scheduled,
            arrival_airport,
            arrival_airport_iata,
            arrival_timezone,
            arrival_time_scheduled
            ):
    engine = create_engine('sqlite:///Nick:mydatabasetest:', echo = True)
    Base = declarative_base()

    class FlightData(Base):
        __tablename__ = "JFK_Flight_Data"

        id = Column(Integer, primary_key=True)
        flight_date =              Column(String)
        flight_status =            Column(String)
        departure_airport =        Column(String)
        departure_timezone =       Column(String)
        departure_airport_iata =   Column(String)
        departure_time_scheduled = Column(String)
        arrival_airport =          Column(String)
        arrival_airport_iata =     Column(String)
        arrival_timezone =         Column(String)
        arrival_time_scheduled =   Column(String)


    #Base.metadata.create_all(engine)
    #print(FlightData.__table__)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    flight = FlightData(flight_date= flight_date,
                        flight_status=flight_status,
                        departure_airport= departure_airport,
                        departure_timezone = departure_timezone,
                        departure_airport_iata = departure_airport_iata,
                        departure_time_scheduled = departure_time_scheduled,
                        arrival_airport = arrival_airport,
                        arrival_airport_iata = arrival_airport_iata,
                        arrival_timezone = arrival_timezone,
                        arrival_time_scheduled = arrival_time_scheduled 
                        )
    print(flight.id)
    session.add(flight)

    session.commit()