#!/usr/bin/python3
"""Function to query API and returns number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """User agent to avoid too many requests"""
    headers = {'User-Agent': 'My-User_Agent'}

    """ Send a GET request to the Rddit API"""
    response = requests.get('https://www.reddit.com/r/{}/about.json'
            .format(subreddit),
            headers=headers,
            allow_redirects=False)

    """ Check if response is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            """ Extract and return the number of subscribers"""
            return data['data']['subscribers']
        except (KeyError, ValueError):
            return 0
    elif response.status_code == 404:
        return 0
    else:
        return 0
