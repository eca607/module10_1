import json
import requests
from flask import Flask, jsonify

# API endpoint URL's and access keys
#WMATA_API_KEY = "22485471cdef46d8b8bd20b312d7bf52"
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
#headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents = []

  # use 'requests' to do a GET request to the WMATA Incidents API
  # retrieve the JSON from the response
  response  = requests.get(INCIDENTS_URL, verify=False)
  data = response.json()

  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list
  for incident in data.get("ElevatorIncidents", []):
     # Logic to compare "UnitType from passed in "ElevatorIncidents" dictionary.
     if incident.get("UnitType") == unit_type.upper():
        incident_data = {
                    "StationCode": incident.get("StationCode"),
                    "StationName": incident.get("StationName"),
                    "UnitName": incident.get("UnitName"),
                    "UnitType": incident.get("UnitType")
        }
        incidents.append(incident_data)

  # return the list of incident dictionaries using json.dumps()
  return_data = json.dumps(incidents)

  return return_data

if __name__ == '__main__':
    app.run(debug=True)