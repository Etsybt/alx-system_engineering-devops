#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit
        hot_list: A list to store the titles of hot articles
        after: A parameter used for pagination to get the next set of result
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()["data"]
    children = data["children"]

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data["after"]
    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
