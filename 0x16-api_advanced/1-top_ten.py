#!/usr/bin/python3
"""Function to query API and returns top ten posts"""

import requests


def top_ten(subreddit):
    """User agent to avoid too many requests"""
    headers = {'User-Agent': 'My-User_Agent'}

    """ Send a GET request to the Rddit API"""
    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers,
                            allow_redirects=False)

    """ Check if response is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            """ Extract and return the titles"""
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print("None")
    elif response.status_code == 404:
        print("None")
    else:
        print("None")
