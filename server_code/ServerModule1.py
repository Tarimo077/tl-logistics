import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.media
import locale
from collections import defaultdict

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def getDrivers():
  url = "https://appliapay.com/getDrivers"
  headers = {
    "Content-Type": "application/json"
  }
  response = anvil.http.request(url, method="GET", headers=headers, username='admin', password='123Give!@#')
  return response

@anvil.server.callable
def getTrips():
  url = "https://appliapay.com/getTrips"
  headers = {
    "Content-Type": "application/json"
  }
  response = anvil.http.request(url, method="GET", headers=headers, username='admin', password='123Give!@#')
  return response

@anvil.server.callable
def setCashVisisbility():
  return False
