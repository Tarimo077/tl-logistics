from ._anvil_designer import TripStatsTemplate
from anvil import *
import anvil.server
import json
from collections import Counter
from datetime import datetime

class TripStats(TripStatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    response = anvil.server.call('getTrips')
    text = response.get_bytes().decode('utf-8')
    trips = json.loads(text)
    self.trips = trips
    self.tripCount.text = str(len(trips)) + " TRIPS"
    filtered_data = [record for record in self.trips if '-' in record['location']]
    obj = self.extract_top_origins_destinations(filtered_data)
    self.repeating_panel_1.items = obj
    peak, offpeak = self.extract_peaks(filtered_data)
    self.repeating_panel_2.items = peak
    self.repeating_panel_3.items = offpeak
    self.repeating_panel_4.items = trips
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

  def extract_peaks(self, data, **event_args):
    # Parse dates and extract months, skipping over entries with None date
    months = [datetime.strptime(entry['date'], '%Y-%m-%dT%H:%M:%S.%fZ').month
              for entry in data if entry['date'] is not None]
    
    # Count trips for each month
    trip_counts = Counter(months)
    
    # Sort months by trip counts
    sorted_months = sorted(trip_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Calculate threshold for peak and off-peak
    total_months = len(sorted_months)
    peak_threshold = total_months // 2  # Top 50% of months
    off_peak_threshold = total_months - peak_threshold  # Bottom 50% of months
    
    # Rank months into peak and off-peak
    peak_months = [month for month, count in sorted_months[:peak_threshold]]
    off_peak_months = [month for month, count in sorted_months[off_peak_threshold:]]
    month_arr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    peak_string = []
    off_peak_string = []
    for x in peak_months:
      peak_string.append(month_arr[int(x)-1])
    for y in off_peak_months:
      off_peak_string.append(month_arr[int(y)-1])
    off_peak_string = list(reversed(off_peak_string))
    pks = []
    offpks = []
    for i in peak_string:
      pks.append({'peak': i})
    for j in off_peak_string:
      offpks.append({'offpeak': j})
    return pks, offpks
