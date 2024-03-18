from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.js
from anvil_extras.animation import animate, Transition

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dom_node = anvil.js.get_dom_node(self)
    #dom_node.style.background = f"url(_/theme/TLbackground.jfif)"
    body_tag = anvil.js.window.document.body
    self.image_1.background = None
    body_tag.style.background =  "#6750A4"#f"url(_/theme/TLbackground.jfif)"
    self.eye.tooltip = 'view password'
    self.pass_state = False
    slide_in_up = Transition(translateY=["100%", 0])
    slide_in_down = Transition(translateY=["-100%", 0])
    zoom_in = Transition(scale=[.3, 1])
    fade_in = Transition(opacity=[0, 1])
    fly_in_down = slide_in_down | zoom_in | fade_in
    animate(self.image_1, fly_in_down, duration=4000)
    self.password.hide_text = True

    # Any code you write here will run before the form opens.

  def eye_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.pass_state == False:
      self.password.hide_text = False
      self.eye.icon = 'fa:eye-slash'
      self.pass_state = True
      self.eye.foreground = '#FFFFFF'
      self.eye.background = '#FF0000'
      self.eye.tooltip = 'hide password'
      
    else:
      self.password.hide_text = True
      self.eye.icon = 'fa:eye'
      self.pass_state = False
      self.eye.background = '#FFFFFF'
      self.eye.foreground = '#21005E'
      self.eye.tooltip = 'view password'
