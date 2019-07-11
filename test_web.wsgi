import sys

#app's path
sys.path.insert(0,r"C:/Users/xh/Documents/GitHub/love")

from sightseeing import app

#Initialize WSGI app object
application = app
