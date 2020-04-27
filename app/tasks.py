import time
import json
import requests
from datetime import datetime
from Airline_Model import add_flight


def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task Completed')


def flights():
    today = datetime.today().strftime('%Y-%m-%d')     
    base_url ="http://api.aviationstack.com/v1/flights"
    api_key = "c86297efab528dacb00207e8f0a74b14"
    response = requests.get(
        base_url +
        "?" +"access_key=" + api_key +
        "&" + "dep_iata=JFK"   
    )
    response = response.json()
    
    data = response['data']
    print(data)
    for x in range(0,100):
        print(data[x]['departure']['iata'])
        add_flight(
                   data[x]['flight_date'] ,        
                   data[x]['flight_status'],          
                   data[x]['departure']['airport'],     
                   data[x]['departure']['timezone'],   
                   data[x]['departure']['iata'],
                   data[x]['departure']['scheduled'], 
                   data[x]['arrival']['airport'],    
                   data[x]['arrival']['iata'],  
                   data[x]['arrival']['timezone'],    
                   data[x]['arrival']['scheduled'],
            )

flights()


