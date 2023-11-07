#!/usr/bin/python3

"""
queries the Reddit API and returns a list
containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)

        elif response.status_code == 404:
            return None
        else:
            return None
    except Exception as e:
        return None

    return hot_list


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        hot_articles = recurse(subreddit)
        if hot_articles is not None:
            for idx, title in enumerate(hot_articles, start=1):
                print(f"{idx}. {title}")
        else:
            print(None)
