# SWDV 660 2W 19/SU1 - Week 1 Assignment
# Joe Dent


import urllib.request
import urllib.parse
import json
from pretty_json import format_json
from jsontraverse.parser import JsonTraverseParser



url = 'https://api.weather.gov/stations?state=MO&limit=100'
f = urllib.request.urlopen(url)
j = f.read().decode('utf-8')
parser = JsonTraverseParser(j)

# Pull out a subset of the weather result
ksus = parser.traverse('features.3')

# Format the message.
print(format_json(ksus))

