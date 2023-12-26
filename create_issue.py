import requests

# GitHub repository information
owner = "your_username"
repo = "your_repository"
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Your personal access token
token = "your_personal_access_token"

# Issue data
issue_data = {
    "title": "New Issue",
    "body": "This is the content of the new issue.",
}

# Headers with authorization
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json",
}

# Make a POST request to create a new issue
response = requests.post(url, json=issue_data, headers=headers)

# Check the response
if response.status_code == 201:
    print("Issue created successfully.")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.json())
