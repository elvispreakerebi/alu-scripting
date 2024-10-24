#!/usr/bin/python3

""" script """

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the subreddit or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates success
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        # If there is any exception (e.g. network issues), return 0
        return 0
