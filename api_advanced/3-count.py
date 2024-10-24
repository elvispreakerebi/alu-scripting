#!/usr/bin/python3

""" script """

import requests

def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and counts the occurrences of specified keywords.

    Parameters:
    subreddit (str): The name of the subreddit to query.
    word_list (list): List of keywords to count occurrences of.
    word_count (dict): A dictionary to store counts of each keyword (used during recursion).
    after (str): The `after` value for pagination (None for the first request).

    Returns:
    None: Prints the sorted count of keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            # Initialize word count dictionary if empty
            if not word_count:
                word_count = {word.lower(): 0 for word in word_list}

            # Iterate through the titles of each post
            for post in posts:
                title = post['data']['title'].lower().split()

                # Count occurrences of each word in the word list
                for word in word_list:
                    count_word = word.lower()
                    word_count[count_word] += title.count(count_word)

            # If there's more data, continue recursively
            if after is not None:
                return count_words(subreddit, word_list, word_count, after)

            # Print sorted results once recursion is done
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print("{}: {}".format(word, count))
        else:
            return None  # Invalid subreddit or error

    except requests.RequestException:
        return None  # Handle any network errors
