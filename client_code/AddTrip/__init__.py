from ._anvil_designer import AddTripTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
from time import sleep
from anvil_extras import MessagePill
from datetime import datetime

class AddTrip(AddTripTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.msgPill.visible = False
    self.background = "#FFFFFF"
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
      self.msgPill.message = "CHOOSE DRIVER"
      self.msgPill.visible = True
      #alert('Choose driver', buttons=None)
      return
    if self.amount.text is None or self.txtFrom.text is None or self.txtTo.text is None or self.date.date is None:
      self.msgPill.message = "ENTER ALL FIELDS"
      self.msgPill.visible = True
      return
    if self.amount.text is not None or self.dropdownDriver.selected_value is not None or self.txtFrom.text is not None or self.txtTo.text is not None or self.date.date is not None:
      self.msgPill.visible = False
      amnt = "${:,.0f}".format(self.amount.text)
      route = self.txtFrom.text.upper() + "-" + self.txtTo.text.upper()
      date = str(self.date.date)
      # Parse the input date string into a datetime object
      input_date = datetime.strptime(date, '%Y-%m-%d')
# Format the datetime object into the desired format
      output_date_str = input_date.strftime('%d-%b-%y')
      amnt = amnt + ".00"
      driver = self.dropdownDriver.selected_value
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
          self.dropdownDriver.text = None
          self.amount.text = ""
          self.txtFrom.text = ""
          self.txtTo.text = ""
          self.date.date = None
        elif(c==False):
          open_form('TripStats')
        else:
          pass
      else:
        pass