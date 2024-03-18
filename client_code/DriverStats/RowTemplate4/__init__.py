from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item['origins'] = str(self.item['origins'])
    self.item['origins'] = self.item['origins'].replace("[", "").replace("]", "").replace("'", "")

    # Any code you write here will run before the form opens.
