from ._anvil_designer import AddTripTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
from anvil_extras.animation import animate, get_bounding_rect
from time import sleep

class AddTrip(AddTripTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    response = anvil.server.call('getDrivers')
    text = response.get_bytes().decode('utf-8')
    drivers = json.loads(text)
    driversNew = []
    for x in drivers:
      if x == "Joshua/Brian"  or x == "NA" or x == "Patrick/Vincent" or x == "N/A":
        pass
      else:
        driversNew.append(x)
    self.dropdownDriver.items = driversNew

    # Any code you write here will run before the form opens.

  def newDriver_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AddTripDriver')

  def addTrip_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.dropdownDriver.selected_value is None:
