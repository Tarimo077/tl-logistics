from ._anvil_designer import AddTripDriverTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep
from anvil_extras import MessagePill
from datetime import datetime

class AddTripDriver(AddTripDriverTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.msgPill.visible = False

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AddTrip')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.driverName.text is None or self.amount.text is None or self.fromRoute.text is None or self.toRoute.text is None or self.date.date is None:
      self.msgPill.message = "ENTER ALL FIELDS"
      self.msgPill.visible = True
      return
    if self.driverName.text is not None or self.amount.text is not None or self.fromRoute.text is not None or self.toRoute.text is not None or self.date.date is not None:
      self.msgPill.visible = False
      amnt = "${:,.0f}".format(self.amount.text)
      route = self.fromRoute.text.upper() + "-" + self.toRoute.text.upper()
      date = str(self.date.date)
      # Parse the input date string into a datetime object
      input_date = datetime.strptime(date, '%Y-%m-%d')
# Format the datetime object into the desired format
      output_date_str = input_date.strftime('%d-%b-%y')
      amnt = amnt + ".00"
      driver = self.driverName.text
      dt = {
        "name": driver,
        "amount": str(amnt),
        "location": route,
        "date": output_date_str
      }
      c = confirm('Are you sure you want to add this trip?', buttons=[("Yes", True),("No", False)])
      if(c==True):
        anvil.server.call('addTrip', dt)
        self.msgPill.level = "success"
        self.msgPill.message = "TRIP ADDED SUCCESSFULLY"
        self.msgPill.visible = True
        sleep(3)
        self.msgPill.visible = False 
        open_form('TripStats')
      elif(c==False):
        c1 = confirm('Do you want to add a new trip?', buttons=[("Yes", True), ("No", False)])
        if(c1==True): 
          self.driverName.text = ""
          self.amount.text = ""
          self.fromRoute.text = ""
          self.toRoute.text = ""
          self.date.date = None
        elif(c==False):
          open_form('TripStats')
        else:
          pass
      else:
        pass
      
