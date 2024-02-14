#!/usr/bin/python3
"""
Queries the Reddit API recursively and counts occurrences of given keywords
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively queries the Reddit API

    Args:
        subreddit: The name of the subreddit
        word_list: A list of keywords to count occurrences of
        hot_list: A list to store the titles of hot articles
        after: A parameter used for pagination to get the next set of results
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return

    data = response.json()["data"]
    children = data["children"]

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data["after"]
    if after is not None:
        count_words(subreddit, word_list, hot_list, after)
    else:
        word_count = {}
        for title in hot_list:
            for word in word_list:
                if word.lower() in title.lower().split():
                    word_count[word.lower()] = word_count.get(
                        word.lower(), 0) + 1

        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
