import requests

from my_token import my_token


def get_created_repo(url):
    token = my_token
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        repo = response.json()
        assert repo['has_wiki'] == False
        assert repo['private'] == True
        assert repo['name'] == 'repo-created-with-api'
        assert repo['owner']['login'] == 'Sia-Lab-4'

    else:
        print(f"Response status code: {response.status_code}")

if __name__=="__main__":
    url = "https://api.github.com/repos/Sia-Lab-4/repo-created-with-api"
    get_created_repo(url)















