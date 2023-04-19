"""Sample Post models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Post
from datetime import datetime, timedelta

post0 = Post(id=0,
            img="post0",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=3,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post1 = Post(id=1,
            img="post1",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=5,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post2 = Post(id=2,
            img="post2",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=6,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post3 = Post(id=3,
            img="",
            desc="test",
            private=True,
            created=datetime.now(),
            challenge=10,
            user_id="anonymous",
            comments=[],
            tags=[])
elaine1 = Post(id=4,
              img="IMG_3058.jpeg",
              private=False,
              created=datetime.now(),
              challenge=1,
              user_id="elaine13@email.unc.edu",
              comments=[],
              tags=[])
elaine2 = Post(id=5,
               img="IMG_2954.jpeg",
               private=False,
               created=datetime.now(),
               challenge=1,
               user_id="elaine13@email.unc.edu",
               comments=[],
               tags=["impressionism"])

models = [
    post0,
    post1,
    post2,
    post3,
    elaine1,
    elaine2
]
