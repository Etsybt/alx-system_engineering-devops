#!/usr/bin/python3
"""
api request
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API

    Args:
        subreddit: The name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
