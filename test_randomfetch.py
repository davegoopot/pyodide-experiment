"""
    Developer tests to help build the python code.
"""

import randomfetch

def test_randomfetch():
    """
        getRabndomNumber() should return a number between 0 and 100.
    """

    x = randomfetch.getRandomNumber()
    assert x >= 0 and x <= 100