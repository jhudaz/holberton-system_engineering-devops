#!/usr/bin/python3
from requests import get

def recurse(subreddit, hot_list=[]):
    url='https://api.reddit.com/r/{}?sort=hot&limit=100'.format(subreddit)
    user_agent = "application/x-www-form-urlencoded"
    response = get(url, headers={'User-Agent': user_agent}).json()

    data = response.get('data')

    after = data.get('after')


    if(after is None):
        return hot_list
    else:
        articles =  data.get('children')
        for article in  articles:
            title = article.get('data').get('title')
            hot_list.append(title)
        
        recurse(subreddit, hot_list)
    




