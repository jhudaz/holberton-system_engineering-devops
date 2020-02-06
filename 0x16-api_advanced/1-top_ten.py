#!/usr/bin/python3
from requests import get


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    user_agent = "application/x-www-form-urlencoded"
    response = get(url, headers={'User-Agent': user_agent})

    if response.status_code == 200:
        data = response.json()
        top = data.get('data').get('children')
        for new in top:
            title = new.get('data').get('title')
            print(title)
    else:
        print('None')
