import csv
from geopy.geocoders import Photon

def get_address_from_coordinates(latitude, longitude):
    # Initialize Photon geocoder
    geolocator = Photon(user_agent="http")
    
    # Get location with reverse geocode
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    
    # Return address
    return location.address if location else None

def convert_coordinates(input_csv, output_csv):
    with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header to the output CSV
        writer.writerow(['Latitude', 'Longitude', 'Address'])
        
        # Skip header row if your CSV has one
        next(reader, None)
        
        for row in reader:
            latitude, longitude = map(float, row)  # Ensure the values are floats
            address = get_address_from_coordinates(latitude, longitude)
            writer.writerow([latitude, longitude, address])

# Example usage
input_csv = 'coordinates.csv'
output_csv = 'addresses.csv'
convert_coordinates(input_csv, output_csv)
