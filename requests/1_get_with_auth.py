import requests

from my_token import my_token


def get_with_auth(url):
    token = my_token
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        repos = response.json()
        repos_count = len(repos)
        return repos_count, response.headers
    else:
        print(f"Response status code: {response.status_code}")
        return 0, response.headers
if __name__=="__main__":
    url = "https://api.github.com/user/repos"
    num_of_repos, headers = get_with_auth(url)
    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")














