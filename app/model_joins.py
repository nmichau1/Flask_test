from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from Airline_Model import FlightData
from coord_model import Airport_Coords
import json
engine = create_engine('sqlite:///Nick:mydatabasetest:', echo = True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

Coordinates = {}
for u , a in session.query(FlightData,Airport_Coords).\
            filter(FlightData.arrival_airport_iata == Airport_Coords.iata_code).\
                all():
    
    Coordinates[u.arrival_airport] =[a.latitude,a.longitude]


Coordinates = json.dumps(Coordinates)

