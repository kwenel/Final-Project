import requests
import json
from tabulate import tabulate

def get_access_token():
    """
    Retrieves an access token from the Amadeus API.
    """
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "W72oIGXQ9XccCo6LiIkwGdGokn1VKEVu",
        "client_secret": "oZYxrhGhrTP3unMe"
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        return None

def get_flight_prices(origin, destination, date):
    """
    Fetches flight prices from the Amadeus API.
    """
    access_token = get_access_token()
    if not access_token:
        print("Failed to retrieve access token.")
        return None

    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "max": 5
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        flight_options = []

        for offer in data.get("data", []):
            price = offer.get("price", {}).get("total", "N/A")

            airlines = []
            itineraries = offer.get("itineraries", [])
            if itineraries:
                for itinerary in itineraries:
                    segments = itinerary.get("segments", [])
                    for segment in segments:
                        airline = segment.get("carrierCode", "Unknown")
                        airlines.append(airline)

            airline_names = ", ".join(set(airlines)) if airlines else "Unknown Airline"
            flight_options.append([airline_names, f"${price}"])

        return flight_options
    else:
        print(f"Error fetching flight data: {response.status_code}")
        return None

def main():
    """
    Main function to execute flight price retrieval and comparison.
    """
    name = input("Enter your name: ")
    origin = input("Enter origin airport code: ")
    destination = input("Enter destination airport code: ")
    date = input("Enter departure date (YYYY-MM-DD): ")
    
    flight_options = get_flight_prices(origin, destination, date)
    
    if flight_options:
        print(f"\n{name}, here are the available flight options:")
        print(tabulate(flight_options, headers=["Airline", "Price"], tablefmt="grid"))
    else:
        print(f"Sorry {name}, failed to retrieve flight prices.")

if __name__ == "__main__":
    main()
