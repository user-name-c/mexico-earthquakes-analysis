import pandas as pd
import json
import os

def process_earthquakes():
    raw_path = "../data/raw/earthquakes.json"
    processed_path = "../data/processed/earthquakes_clean.csv"
    
    # 1. Load the raw JSON
    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Extract features from GeoJSON (USGS structure)
    features = data['features']
    
    rows = []
    for entry in features:
        prop = entry['properties']
        geom = entry['geometry']['coordinates']
        
        rows.append({
            'time': prop['time'],
            'magnitude': prop['mag'],
            'place': prop['place'],
            'longitude': geom[0],
            'latitude': geom[1],
            'depth': geom[2]
        })

    df = pd.DataFrame(rows)

    # 3. Data Cleaning
    # Convert Unix time (ms) to datetime
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    
    # Drop rows with missing values in critical columns
    df = df.dropna(subset=['magnitude', 'time'])
    
    # 4. Save processed data
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    
    print(f"✅ Success: Processed {len(df)} earthquakes. Saved to {processed_path}")
    print(df.head())

if __name__ == "__main__":
    process_earthquakes()