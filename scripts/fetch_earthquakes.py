import requests
import json
import os

def fetch_earthquakes():
    # 1. Configuration

    # URL for earthquakes in a coordinate box covering Mexico (approx.)

    # Minimum magnitude 2.5 to avoid excessive noise
    URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": "2023-01-01",
        "endtime": "2024-01-01",
        "minmagnitude": "2.5",
        "minlatitude": "14.0",
        "maxlatitude": "33.0",
        "minlongitude": "-120.0",
        "maxlongitude": "-86.0"
    }
    
    save_path = "../data/raw/earthquakes.json"
    
    # Ensure the folder exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    try:
        print(f"Downloading data from {URL}...")
        response = requests.get(URL, params=params)
        response.raise_for_status() # Throw error if the request fails
        
        data = response.json()
        
        # 2. Save JSON
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"✅ Success: {len(data['features'])} earthquakes saved to {save_path}")
        
    except Exception as e:
        print(f"❌ Error in the download: {e}")

if __name__ == "__main__":
    fetch_earthquakes()