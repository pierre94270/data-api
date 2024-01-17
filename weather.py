# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    
    """Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)"""
    # "https://weather.lewagon.com/geo/1.0/direct?q=Paris,France&limit=1"
    #api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"https://weather.lewagon.com/geo/1.0/direct?q={query}"
    #response = requests.get(base_url).json() 
    response = requests.get(url).json()
    if len(response)==1:
        return response[0]
    elif len(response)>1:
        cities = []
        for city in response :
            cities.append(f'{response["name"]}, {response["country"]}' )       
        for index, citis in enumerate(cities,start=1) :
            print( f"{index}. {citis}" )
        choice=input("Multiple matches found, which city did you mean?\n >")
        return response[int(choice)-1] 
    else:
        return None
    
        #return response[i] for i in range(len(response))
        
        
    

    # YOUR CODE HERE

def weather_forecast(lat, lon):
    url ="https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}
    response = requests.get(url).json()
    #liste des options, villes, prendre5 premmiers
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    #if coord[lat]== && coord[lon]==)
    name = ville[0]
    list_dict={}
    for i  in range(5):
        list_dict[i]= f"{day}: {weather} ({temperature})"
    return list_dict
    #pass  # YOUR CODE HERE

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    # TODO: Display weather forecast for a given city
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
