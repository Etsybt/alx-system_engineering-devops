#!/usr/bin/python3
"""
api
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API

    Args:
    subreddit: The name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
