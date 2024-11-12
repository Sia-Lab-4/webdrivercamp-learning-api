import requests

from my_token import my_token


def update_repo(url):
    token = my_token
    headers = {
        "Authorization": f"token {token}"
    }
    data = {
        "description": "I know Python Requests!"
    }
    response = requests.patch(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()

if __name__=="__main__":
    url = "https://api.github.com/repos/Sia-Lab-4/repo-created-with-api"
    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'















