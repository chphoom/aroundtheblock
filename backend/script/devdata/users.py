"""Sample User models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import User, Post
from datetime import datetime, timedelta

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


keaw = User(email="keaw@email.unc.edu", 
            displayName="keaw",
            password="4ho00o76i1", 
            created=datetime.now(), 
            private=True, 
            bio="Mostly focused on backend.", 
            pronouns="they/them", 
            pfp="", 
            userPosts=[], 
            connectedAccounts=["instagram.com/khaamkeaw", "pinterest.com/twofacedsatyr"], 
            savedPosts=[], 
            savedChallenges=[])

lucy = User(email="lucy@lucy.com", 
            displayName="lucy123",
            password="test", 
            created=datetime.now(), 
            private=False, 
            bio="Hi there! I'm Lucy, a recent college grad with a passion for art. I work at an animation stupid in New York and love experimenting with new styles.", 
            pronouns="she/her", 
            pfp="lucy.png", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

olivia = User(
            email="olivia@olivia.com", 
            displayName="olivia567",
            password="test", 
            created=datetime.now(), 
            private=False, 
            bio="", 
            pronouns="she/her", 
            pfp="olivia.png", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

ian = User(
            email="ian@ian.com", 
            displayName="ian8910",
            password="test", 
            created=datetime.now(), 
            private=True, 
            bio="that guy", 
            pronouns="he/him", 
            pfp="ian.png", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

elaine = User(
            email="elaine13@email.unc.edu", 
            displayName="elaine",
            password="test", 
            created=datetime.now(), 
            private=True, 
            bio="it's me", 
            pronouns="she/her", 
            pfp="78145235_p0_master1200.jpeg", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

liya = User(
            email="lplaceholder@email.unc.edu", 
            displayName="liya",
            password="test", 
            created=datetime.now(), 
            private=True, 
            bio="", 
            pronouns="she/her", 
            pfp="", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

anonymous = User(
            email="anonymous", 
            displayName="anonymous",
            password="test", 
            created=datetime.now(), 
            private=True, 
            bio="the profile used for private or anonymous users", 
            pronouns="they/them", 
            pfp="", 
            userPosts=[], 
            connectedAccounts=[], 
            savedPosts=[], 
            savedChallenges=[])

models = [
    keaw,
    lucy,
    olivia,
    ian,
    elaine,
    liya,
    anonymous
]
