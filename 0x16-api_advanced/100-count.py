#!/usr/bin/python3

"""
queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    lk = subreddit
    a = after

    if counts is None:
        counts = Counter()
    if a is None:
        a = ''

    url = f"https://www.reddit.com/r/{lk}/hot.json?limit=100&after={a}"
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                for keyword in word_list:
                    if f' {keyword} ' in f' {title.lower()} ':
                        counts[keyword.lower()] += 1

            a = data['data']['after']
            if a:
                return count_words(l, word_list, a, counts)

        elif response.status_code == 404:
            return
        else:
            return
    except Exception as e:
        return

    for w, c in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{w}: {c}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Please pass an argument for the subreddit")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
