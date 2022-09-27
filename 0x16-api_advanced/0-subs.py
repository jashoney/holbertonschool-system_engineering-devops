#!/usr/bin/python3
""" a function to return subscribers of a subreddit """


from requests import get


def number_of_subscribers(subreddit):
    """ function to get the subscribers of a subreddit"""

    if subreddit is None:
        return 0

    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    my_header = {"User-Agent": "James devops project 0x16"}
    resp = get(url, headers=my_header, verify=False).json()
    all_data = resp.get("data", {})
    subs = all_data.get('subscribers', 0)
    return subs
