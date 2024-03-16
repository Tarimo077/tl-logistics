from ._anvil_designer import TripStatsTemplate
from anvil import *
import anvil.server
import json
from collections import Counter

class TripStats(TripStatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    response = anvil.server.call('getTrips')
    text = response.get_bytes().decode('utf-8')
    trips = json.loads(text)
    self.trips = trips
    filtered_data = [record for record in self.trips if '-' in record['location']]
    obj = self.extract_top_origins_destinations(filtered_data)
    self.repeating_panel_1.items = obj
    self.item['data'] = obj
    # Any code you write here will run before the form opens.

  def extract_top_origins_destinations(self, data, **event_args):
    locations = [entry["location"] for entry in data]
    # Count occurrences of each location
    location_counts = Counter(locations)
    # Find the most common locations
    top_locations = location_counts.most_common(10)  # Change 5 to desired number of top locations
    # Extract top origins and destinations
    top_origins = []
    top_destinations = []
    for loc, _ in top_locations:
        origin, destination = loc.split("-")
        top_origins.append(origin)
        top_destinations.append(destination)

    return {'origins': top_origins, 'destinations': top_destinations}