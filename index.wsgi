import sae
import os
import sys

root = os.path.dirname(__file__)

from sound import wsgi

application = sae.create_wsgi_app(wsgi.application)