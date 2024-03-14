import justpy as jp
import inspect

from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp import page

# Global gives all of the imports and stuff
#including hasattr() method
#convert to list to avoid runtime error (dynamic list size)
imports = list(globals().values())

# Issubclass also filters page.Page
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)