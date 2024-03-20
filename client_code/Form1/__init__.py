from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def switch_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    state = self.switch_1.checked
    if(state):
      print("ON")
    else:
      print("OFF")
