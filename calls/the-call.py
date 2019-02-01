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
# uncomment below for initial display test
##print(response_dict.keys())

print("Total repos: ", response_dict['total_count'])

# Check out certain items from the repositories
repo_dictionaries = response_dict['items']
print("Repos returned: ", len(repo_dictionaries))

# Refined look
# Check out the first repository
repo_dictionary = repo_dictionaries[0]
##print("\nKeys: ", len(repo_dictionary))
##for key in sorted(repo_dictionary.keys()):
##    print(key)
print("\nSelected info about first repo:")
print('Name: ', repo_dictionary['name'])
print('Owner: ', repo_dictionary['owner']['login'])
print('Stars: ', repo_dictionary['stargazers_count'])
print('Description: ', repo_dictionary['description'])