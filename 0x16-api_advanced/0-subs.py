#!/usr/bin/python3
from requests import get


def number_of_subscribers(subreddit):
    """subcribers from a subreddit"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    user_agent = "application/x-www-form-urlencoded"
    response = get(url, headers={'User-Agent': user_agent})

    if response.status_code == 200:

        json = response.json()
        data = json.get('data').get('subscribers')
        return int(data)
    else:
        return 0
