#!/usr/bin/python3

"""
queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)

        print(f"{num_subscribers}")
