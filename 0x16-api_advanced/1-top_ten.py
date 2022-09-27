#!/usr/bin/python3
""" a function to print a subreddit's top ten posts """


from requests import get


def top_ten(subreddit):
    """ as above """

    if subreddit is None:
        print(None)
        return

    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    my_header = {"User-Agent": "James devops project 0x16"}
    limit = {"limit": 10}
    resp = get(url, headers=my_header, verify=False, params=limit).json()

    all_data = resp.get("data", {})
    all_posts = all_data.get("children", 0)

    if all_posts is None or resp.get("error") == 404:
        print(None)
    else:
        for each_post in all_posts:
            post_title = each_post.get("data", {}).get("title")
            print(post_title)
