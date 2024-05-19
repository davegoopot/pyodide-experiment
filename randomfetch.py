"""
Code to fetch numbers from random.org
"""

import requests

def getRandomNumber():
    """
        Fetch a random number from random.org. The result is a number
        between 0 and 100.
    """
    url = "https://www.random.org/integers/?num=1&min=0&max=100&col=1&base=10&format=plain&rnd=new"
    response = requests.get(url)
    return int(response.text)