import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
responser_dict = r.json()

# Process result.
print(responser_dict.keys())
print(f"Total repositories: {responser_dict['total_count']}")

# Explore information about the repositories. 
repo_dicts = responser_dict['items']
print(f"repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")


# print("\nThe list description of the 30 projects in the python:")
# for i in range(0,30):
#     repo_dict = repo_dicts[i]
#     print(f"Description: {repo_dict['description']}")

total_count = responser_dict['total_count']
print(f"Total_count is:{total_count}")

