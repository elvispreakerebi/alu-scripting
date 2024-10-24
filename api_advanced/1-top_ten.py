#!/usr/bin/python3

""" script """

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None: Prints the titles of the first 10 hot posts or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates success
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        # If there is any exception (e.g. network issues), print None
        print(None)
