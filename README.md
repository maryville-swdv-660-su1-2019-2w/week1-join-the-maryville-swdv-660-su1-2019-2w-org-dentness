# Weather Station

This app will pull the Weather Station details from https://weather.gov for the state of Missouri.  This returns a 
JSON formatted document that we will then retrieve and display the information for KSUS (Spirit of St. Louis Airport).

## Dependencies
- **pyinstaller** - To created stand-alone executables
- **json-traverse** - To retrieve sub-sections of the JSON document
- **pretty-json** - To pretty-print a JSON node and its descendents

## How to run
From source:
```
python weather.py
```

From exe:
```
weather
```