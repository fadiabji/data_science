import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_names, stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visulaizaton.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y':stars,
    'marker':{
        'color': 'rgb(60,100,150)',
        'line': {'width':1.5, 'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]
my_layout = {
    'title': 'Most-starred Python projects on GitHub',
    'xaxis': {'title':'Repository'},
    'yaxis': {'title':'Stars'},
}

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename= 'python_repos.html')
