import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# stateless API call and capture response
url = 'https://api.github.com/search/repositories?q=language:lua&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)
response_dict = r.json()

print("Total repos: ", response_dict['total_count'])

repo_dictionaries = response_dict['items']
#print("Repos returned: ", len(repo_dictionaries))

names, stars = [], []
for repo_dictionary in repo_dictionaries:
    names.append(repo_dictionary['name'])
    stars.append(repo_dictionary['stargazers_count'])

# Build the visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend = False)
chart.title = 'Most-Starred Lua Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('lua_repos.svg')

repo_dictionary = repo_dictionaries[0]

print("\nSelected info about first repo:")
print('Name: ', repo_dictionary['name'])
print('Owner: ', repo_dictionary['owner']['login'])
print('Stars: ', repo_dictionary['stargazers_count'])
print('Description: ', repo_dictionary['description'])