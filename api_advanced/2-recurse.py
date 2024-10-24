#!/usr/bin/python3

""" script """

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list of all hot article titles
    for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): The list of hot article titles (used during recursion).
    after (str): The `after` value for pagination (None for the first request).

    Returns:
    list: A list of all hot article titles for the given subreddit.
          If the subreddit is invalid or no articles are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}
    params = {'after': after, 'limit': 100}  # Fetch 100 items per request (Reddit API limit)

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            after = data['data']['after']  # Get the next `after` value for pagination

            # Add the titles of the current batch of hot posts to the hot_list
            hot_list += [post['data']['title'] for post in children]

            # If there's more data to fetch, recursively call `recurse`
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list  # No more pages, return the full hot_list
        else:
            return None
    except requests.RequestException:
        # If there is any exception (e.g., network issues), return None
        return None
