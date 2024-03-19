from ._anvil_designer import AddTripTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
from anvil_extras.animation import animate, get_bounding_rect

class AddTrip(AddTripTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def newDriver_click(self, **event_args):
    """This method is called when the button is clicked"""
    bounding_rect = get_bounding_rect(self.dropdownDriver)
        
        # Create and position the new component using the bounding rect
    new_component = TextBox(text="New Component")
    print(bounding_rect.x)
    new_component.y = bounding_rect.y
    self.dropdownDriver.remove_from_parent()
    self.add_component(new_component, x=bounding_rect.x, y=bounding_rect.y, width=bounding_rect.width, height=bounding_rect.height)
