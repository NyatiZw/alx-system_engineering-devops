#!/usr/bin/python3
"""Function to query API and returns top ten posts"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """User agent to avoid too many requests"""
    headers = {'User-Agent': 'My-User_Agent'}

    """Prepare parametrs for the Reddit API request"""
    params = {'after': after} if after else {}

    """ Send a GET request to the Rddit API"""
    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers,
                            params=params)

    """ Check if response is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            if not posts:
                return hot_list
            else:
                """APpend titles to hot_list"""
                for post in posts:
                    hot_list.append(post['data']['title'])
                """Recursive call with the next 'after' parameter"""
                return recurse(subreddit, hot_list, data['data']['after'])
        except (KeyError, ValueError):
            return ("None")
    elif response.status_code == 404:
        return ("None")
    else:
        return ("None")
