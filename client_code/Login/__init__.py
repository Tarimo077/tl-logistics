from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.js

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dom_node = anvil.js.get_dom_node(self)
    #dom_node.style.background = f"url(_/theme/TLbackground.jfif)"
    body_tag = anvil.js.window.document.body
    self.image_1.background = None
    body_tag.style.background =  "#21005E"#f"url(_/theme/TLbackground.jfif)"

    # Any code you write here will run before the form opens.
