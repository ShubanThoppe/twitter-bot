import json as _json
import random as _random

def _get_quotes():
    with open("info.json") as quotes_file:
        quotes = _json.load(quotes_file)
    return quotes

def _get_random_quote():
    quotes = _get_quotes()
    quote = _random.choice(quotes)
    return quote

def _form_tweet(quote):
    tweet = f"{quote['quote']}"
    return tweet

def _is_valid_char(tweet):
    return len(tweet) <= 280

def _get_tweet():
    while True:
        quote = _get_random_quote()
        tweet = _form_tweet(quote)
        if _is_valid_char(tweet):
            return tweet

print(_get_tweet())
