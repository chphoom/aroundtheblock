from ..models import Challenge
import requests
import random

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

def colors(number: int | None) -> list:
    if number == None:
        return []
    else:
        params = {"generator": "hex-code-gen", "list": "output"}
        result = []
        for i in range(number):
            result.append(requests.get(API_URL, params=params).text)
        return result

def generate(n: bool, v: bool, a: bool, e: bool, s: bool, c: bool) -> Challenge:
    _noun = _verb = _adj = _style = _emo = "" #init to empty strings
    _colors = []

    if n:
        _noun = noun()
    if v:
        _verb = verb()
    if a:
        _adj = adj()
    if e:
        _emo = emotion()
    if s:
        _style = style()
    if c:
        _colors = colors(3)

    result = Challenge(
        id=None,
        posts=[],
        noun=_noun, 
        verb=_verb, 
        adj=_adj, 
        style=_style, 
        emotion=_emo,
        colors=_colors)
    return result

def generateWe() -> Challenge:
    _noun = _verb = _adj = _style = _emo = "" #init to empty strings
    _colors = []
    options = [False, False, False, False, False, False]
    selected = random.sample(range(0,6), 3)

    #if one of the selected is colors
    #remove the third option
    if 5 in selected:
        selected.remove(5)
        selected.pop()
        selected.append(5)

    for i in selected:
        options[i] = True

    if options[0]:
        _noun = noun()
    if options[1]:
        _verb = verb()
    if options[2]:
        _adj = adj()
    if options[3]:
        _emo = emotion()
    if options[4]:
        _style = style()
    if options[5]:
        _colors = colors(1)

    result = Challenge(
        id=None,
        posts=[],
        noun=_noun, 
        verb=_verb, 
        adj=_adj, 
        style=_style, 
        emotion=_emo,
        colors=_colors)
    return result