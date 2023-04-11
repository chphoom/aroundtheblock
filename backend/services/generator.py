from ..models import Challenge, meChallenge, weChallenge
from urllib.request import urlopen
import random
import nltk
nltk.download('popular')

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = urlopen(word_site)
txt = response.read().decode()
WORDS = txt.splitlines()

tagged = nltk.pos_tag(WORDS)

nouns = [item[0] for item in tagged if item[1][0] == 'N']
verbs = [item[0] for item in tagged if item[1][0] == 'V']
adjs = [item[0] for item in tagged if item[1][0] == 'J']
styles = ['Impressionism', 'Avant-garde', 'Baroque', 'Cubism', 'Pixel Art', 'Expressionism', 'Futurism','Minimalism','Pop Art','Rococo','Surrealism']
emotions = ['Sad','Happy','Terror','Hunger']

def generate_color(x):
    colors = []
    for i in range(0,x):
        color = random.randrange(0, 2**24)
        hex_color = hex(color)
        hexcode = "#" + hex_color[2:]
        colors.append(hexcode)
    return colors

def generate(x) -> Challenge:
    result = Challenge(
        id=None,
        posts=[],
        noun=random.choice(nouns), 
        verb=random.choice(verbs), 
        adj=random.choice(adjs), 
        style=random.choice(styles), 
        emotion=random.choice(emotions),
        colors=generate_color(x))
    return result