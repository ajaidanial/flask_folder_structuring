"""Define the routes here"""

from app import app
from views import *

# mapping for routes and views
app.add_url_rule("/", view_func=TestRoute.as_view("index"))
