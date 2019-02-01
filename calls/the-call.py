import requests

# stateless API call and capture response
url = 'https://api.github.com/search/repositories?q=language:lua&sort=stars'
# call get(), pass the url to this function
r = requests.get(url)
# Test whether or not the call is successful
print("Status Code: ", r.status_code)

# Store the response as the value of a variable
response_dict = r.json()

# Output the results
print(response_dict.keys())