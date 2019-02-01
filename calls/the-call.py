import requests

# stateless API call and capture response
url = 'https://api.github.com/search/repositories?q=language:lua&sort=stars'
r = requests.get(url)
# Test whether or not the call is successful
print("Status Code: ", r.status_code)
