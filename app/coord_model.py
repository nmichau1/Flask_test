from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
import requests


engine = create_engine('sqlite:///Nick:mydatabasetest:', echo = True)
Base = declarative_base()

class Airport_Coords(Base):
        __tablename__ = "Airport Coordinates"

        id = Column(Integer, primary_key=True)
        iata_code = Column(String)
        latitude = Column(String)
        longitude = Column(String)


def add_airport_coords(
            iata_code,
            latitude,
            longitude
            ):
    


    #Base.metadata.create_all(engine)
    #print(FlightData.__table__)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Airport = Airport_Coords(iata_code = iata_code,
                             latitude = latitude,
                             longitude =longitude
                        )
    print(Airport.iata_code)
    session.add(Airport)

    session.commit()



#
#response = requests.get('https://pkgstore.datahub.io/core/airport-codes/airport-codes_json/data/e678ee2a5122b8c01caf12c065058b22/airport-codes_json.json')
#data =response.json()
#
#print(type(str(data[0]['coordinates'])))
#lat,lon = str(data[0]['coordinates']).split(",")
#
#for x in range(0,len(response.json())):
#    if data[x]['iata_code'] != None:
#        lat,lon = str(data[x]['coordinates']).split(",")
#        add_airport_coords(data[x]['iata_code'],lat,lon)
#        


