"""Sample Post models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Post
from datetime import datetime, timedelta

post0 = Post(id=0,
            img="",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=3,
            postedBy="lucy@lucy.com",
            comments=[],
            tags=[])

post1 = Post(id=1,
            img="",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=5,
            postedBy="lucy@lucy.com",
            comments=[],
            tags=[])

post2 = Post(id=2,
            img="",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=6,
            postedBy="lucy@lucy.com",
            comments=[],
            tags=[])

post3 = Post(id=3,
            img="",
            desc="test",
            private=True,
            created=datetime.now(),
            challenge=10,
            postedBy="lucy@lucy.com",
            comments=[],
            tags=[])

models = [
    post0,
    post1,
    post2,
    post3
]
