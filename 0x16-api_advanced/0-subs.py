#!/usr/bin/python3
"""
api request
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    except requests.exceptions.RequestException:
        return 0
