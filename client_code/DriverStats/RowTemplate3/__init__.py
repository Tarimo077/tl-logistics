from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server

class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item['destinations'] = str(self.item['destinations'])
    self.item['destinations'] = self.item['destinations'].replace("[", "").replace("]", "").replace("'", "")
    
    # Any code you write here will run before the form opens.
