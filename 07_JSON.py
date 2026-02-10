# working with JSON data
# key value pairs, just like dictonaries

import urllib.request
import json # lets us work with JSON code.

web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print(f"Status Code: {web_url.getcode()}") # prints our status code

data = web_url.read() # we get the data from the read function
# print(f"{data}") # prints from the JSON source. 

# if we want to access specific fields from the JSON format we can use the json.load() function with the data we got and then print the field. 
theJSON = json.loads(data) # we have to load the web data 
print(theJSON["text"])