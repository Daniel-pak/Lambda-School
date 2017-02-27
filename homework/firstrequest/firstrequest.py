import requests
# importing the requests package
r = requests.get('http://google.com')
# using get request from package to grab the get response from google.com
print(r.text)
# printing the text using the requests response method
