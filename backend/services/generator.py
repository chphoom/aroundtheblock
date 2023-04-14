from ..models import Challenge
from urllib.request import urlopen
import random
import nltk
import requests

API_URL = "https://grizzly-fifth-citrine.glitch.me/api"

def noun() -> str:
    params = {"generator": "common-noun", "list": "noun"}
    return requests.get(API_URL, params=params).text

def verb() -> str:
    params = {"generator": "verb", "list": "verb"}
    return requests.get(API_URL, params=params).text

def adj() -> str:
    params = {"generator": "adjective", "list": "adjective"}
    return requests.get(API_URL, params=params).text

def style() -> str:
    params = {"generator": "artism", "list": "output"}
    return requests.get(API_URL, params=params).text

def emotion() -> str:
    params = {"generator": "emotion", "list": "emotion"}
    return requests.get(API_URL, params=params).text

def emotion() -> str:
    params = {"generator": "emotion", "list": "emotion"}
    return requests.get(API_URL, params=params).text

def colors(number: int | None) -> list:
    if number == None:
        return []
    else:
        params = {"generator": "hex-code-gen", "list": "output"}
        result = []
        for i in range(number):
            result.append(requests.get(API_URL, params=params).text)
        return result

def generate(x) -> Challenge:
    result = Challenge(
        id=None,
        posts=[],
        noun=noun(), 
        verb=verb(), 
        adj=adj(), 
        style=style(), 
        emotion=emotion(),
        colors=colors(x))
    return result