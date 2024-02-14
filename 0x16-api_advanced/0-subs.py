#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API

    Args:
    subreddit: The name of the subreddit
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

