#!/usr/bin/python3
from requests import get


def recurse(subreddit, hot_list=[], after="null"):
    url = 'https://api.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
        subreddit, after)
    user_agent = "application/x-www-form-urlencoded"
    response = get(url, headers={'User-Agent': user_agent})
    if response.status_code != 200:
        return None
    json = response.json()
    data = json.get('data')
    after = data.get('after')

    if not after:
        return hot_list
    else:
        articles = data.get('children')
        hot_list = hot_list + articles
        return recurse(subreddit, hot_list, after)
