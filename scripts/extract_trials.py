import requests
import pandas as pd

url = "https://clinicaltrials.gov/api/v2/studies"

params = {
    "query.term": "cancer",
    "fields": "NCTId,Condition,Phase,StudyType,LocationCountry,EnrollmentCount,StartDate",
    "pageSize": 200
}

response = requests.get(url, params=params)
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

data = response.json()
studies_raw = data.get("studies", [])

flattened_data = []
for study in studies_raw:
    protocol = study.get("protocolSection", {})
    
    # Identification
    nct_id = protocol.get("identificationModule", {}).get("nctId")
    
    # Conditions (list to string)
    conditions = protocol.get("conditionsModule", {}).get("conditions", [])
    condition_str = "|".join(conditions)
    
    # Phases (list to string)
    phases = protocol.get("designModule", {}).get("phases", [])
    phase_str = "|".join(phases)
    
    # Study Type
    study_type = protocol.get("designModule", {}).get("studyType")
    
    # Locations (list of countries to unique string)
    locations = protocol.get("contactsLocationsModule", {}).get("locations", [])
    countries = list(set([loc.get("country") for loc in locations if loc.get("country")]))
    country_str = "|".join(countries)
    
    # Enrollment
    enrollment = protocol.get("designModule", {}).get("enrollmentInfo", {}).get("count")
    
    # Start Date
    start_date = protocol.get("statusModule", {}).get("startDateStruct", {}).get("date")
    
    flattened_data.append({
        "NCTId": nct_id,
        "Condition": condition_str,
        "Phase": phase_str,
        "StudyType": study_type,
        "LocationCountry": country_str,
        "EnrollmentCount": enrollment,
        "StartDate": start_date
    })

df = pd.DataFrame(flattened_data)

# Ensure data directory exists
import os
os.makedirs("data", exist_ok=True)

df.to_csv("data/clinical_trials_raw.csv", index=False)

print(f"Extraction complete. {len(df)} trials saved to data/clinical_trials_raw.csv")
