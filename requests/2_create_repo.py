
import requests
from pprint import pprint

from my_token import my_token


def create_repo(url):
    token = my_token
    headers = {
        "Authorization": f"token {token}",
    }
    data = {
        "name": "repo-created-with-api-1",
        "private": True,
        "has_wiki": False
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()
if __name__=='__main__':
    url = 'https://api.github.com/user/repos'
    repo = create_repo(url)
    pprint(repo)









