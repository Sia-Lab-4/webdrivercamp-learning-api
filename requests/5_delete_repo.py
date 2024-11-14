import requests

from my_token import my_token


def delete_repo(url):
    token = my_token
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.delete(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    return response.status_code
if __name__=="__main__":
    url = f'https://api.github.com/repos/Sia-Lab-4/repo-created-with-api-3'
    delete_repo(url)















