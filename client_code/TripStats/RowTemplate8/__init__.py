from ._anvil_designer import RowTemplate8Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

class RowTemplate8(RowTemplate8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.item['date'] is not None:
      date_obj = datetime.strptime(self.item['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
# Format the date
      self.item['date'] = date_obj.strftime('%d %B %Y')

    # Any code you write here will run before the form opens.
