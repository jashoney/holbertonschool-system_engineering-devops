#!/usr/bin/python3
""" Returns a list containing tites of ALL hot articles in a subreddit.
        Done recursively. None if not a valid subreddit """

from requests import get


def recurse(subreddit, hot_list=[], count=0, after=None):
    """ as above """

    if subreddit is None or not type(str):
        return (None)

    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    my_headers = {"User-Agent": "James project 0x16"}
    r_options = {"count": count, "after": after}
    resp = get(url, headers=my_headers, verify=False, params=r_options).json()

    all_posts = resp.get("data", {}).get("children", 0)
    after = resp.get('data', {}).get('after', None)

    if all_posts is None or resp.get("error") == 404:
        if len(hot_list) == 0:
            return (None)
        return (hot_list)
    else:
        for each_post in all_posts:
            hot_list.append(each_post.get('data', {}).get('title'))

    if after is None:
        if len(hot_list) == 0:
            return None
        return (hot_list)
    else:
        count = len(hot_list)
        return recurse(subreddit, hot_list, count, after)
