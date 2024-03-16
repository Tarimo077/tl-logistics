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
    # Any code you write here will run before the form opens.

  def extract_top_origins_destinations(self, data, **event_args):
    locations = [entry["location"] for entry in data]
    # Count occurrences of each location
    location_counts = Counter(locations)
    # Find the most common locations
    top_locations = location_counts.most_common(20)  # Change 5 to desired number of top locations
    # Extract top origins and destinations
    unique_locations = set()  # To store unique locations
    result = []

    for loc, _ in top_locations:
        origin, destination = loc.split("-")
        # Check if the origin or destination is already in the unique set
        # If not, add it to the unique set and append to the result list
        if origin not in unique_locations and destination not in unique_locations:
            result.append({'origin': origin, 'destination': destination})
            unique_locations.add(origin)
            unique_locations.add(destination)

    return result

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DriverStats')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('TripStats')
