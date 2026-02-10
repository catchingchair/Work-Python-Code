import urllib.request

web_url = urllib.request.urlopen("https://www.example.com")

print(f"Result code: {web_url.getcode()}") # gives us the response code. 200 400 etc. error codes. 

print(f"{web_url.read()}") # this will read the data of the website in HTML format

