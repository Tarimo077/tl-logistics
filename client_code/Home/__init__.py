from ._anvil_designer import HomeTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import json
from collections import defaultdict, Counter
from ..Password import Password
import anvil.js
from datetime import datetime


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.seecash = False
    if(self.seecash==False):
      self.hide_cash()
    else:
      self.view_cash()
    response = anvil.server.call('getDrivers')
    text = response.get_bytes().decode('utf-8')
    drivers = json.loads(text)
    response = anvil.server.call('getTrips')
    text = response.get_bytes().decode('utf-8')
    trips = json.loads(text)
    self.trips = trips
    driversNew = []
    for x in drivers:
      if x != "Joshua/Brian" or x != "NA" or x != "Patrick/Vincent" or x != "N/A":
        driversNew.append(x)
    driverCount = len(driversNew)
    tripCount = len(trips)
    self.driverCount.text = str(driverCount) +" DRIVERS"
    self.tripCount.text = str(tripCount) + " TRIPS"
    amount_generated = defaultdict(float)
    grouped_data = defaultdict(list)
    trip_count = defaultdict(int)
    for trip in trips:
      amount_generated[trip['name']] += float(trip['amount'].strip('$').replace(',', ''))
      trip_count[trip['name']] += 1
      date_str = trip['date']
      if date_str:
        date = datetime.strptime(date_str[:10], '%Y-%m-%d')
        grouped_data[date].append(trip)

    total_amount = sum(amount_generated.values())
    total_amount_formatted = "${:,.2f}".format(total_amount)
    self.moneyin.text = str(total_amount_formatted) + "\t"
    grouped_data = dict(sorted(grouped_data.items()))

# Print or plot the grouped data
    dates = list(grouped_data.keys())
    counts = [len(group) for group in grouped_data.values()]
    primary_color = '#6750A4'
    self.plot_1.data = go.Bar(x=dates, y=counts, marker=dict(color=primary_color),
                        hovertemplate='<b>%{x}</b><br>' + 'Trips: %{y}')
    # Configure the plot layout
    self.plot_1.layout = {
      'title': 'TRIPS PER DAY',
      'xaxis': {
        'title': 'DAYS'
      },
      'yaxis': {
        'title': 'TRIPS'
      }
    }
    
    # Any code you write here will run before the form opens.

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(self.seecash==True):
      nw_frm = Password()
      alert_instance = alert(
        content=nw_frm,
        large=False,
        title=None,
        dismissible=False,
        buttons=[('Cancel', 0)],
        role='outlined'
      )
      if(alert_instance is None):
        self.view_cash()  
      else:
        self.hide_cash()
    else:
      self.hide_cash()

  def view_cash(self, **event_args):
    self.button_5.background = '#ff0000'
    self.button_5.icon = 'fa:eye-slash'
    self.button_5.tooltip = 'hide cash in'
    label_element = anvil.js.get_dom_node(self.moneyin)
    label_element.style.filter = "blur(0px)"
    self.seecash = False

  def hide_cash(self, **event_args):
    self.button_5.background = '#6750A4'
    self.button_5.icon = 'fa:eye'
    self.button_5.tooltip = 'view cash in'
    label_element = anvil.js.get_dom_node(self.moneyin)
    label_element.style.filter = "blur(25px)"
    self.seecash = True

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DriverStats')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('TripStats')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('DriverStats')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('TripStats')


