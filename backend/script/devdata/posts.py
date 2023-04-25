"""Sample Post models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Post
from datetime import datetime, timedelta

post0 = Post(id=0,
            img="post0.png",
            title="post 0",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=14,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post1 = Post(id=1,
            img="post1.png",
            desc="test",
            private=False,
            created=datetime.now(),
            challenge=14,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post2 = Post(id=2,
            img="post2.png",
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
              title="Dreamy Mountains",
              desc="I love the idea of using unique colors to paint landscapes.",
              private=False,
              created=datetime.now(),
              challenge=16,
              user_id="elaine13@email.unc.edu",
              comments=[],
              tags=["landscape", "impressionism","meChallenge"])
elaine2 = Post(id=5,
               img="IMG_2954.jpeg",
               title="Venice on Fire",
               desc="Made with acrylics, inspired by Leonid Afremov.",
               private=False,
               created=datetime.now(),
               challenge=17,
               user_id="elaine13@email.unc.edu",
               comments=[],
               tags=["impressionism", "meChallenge"])
elaine3 = Post(id=6,
               img="IMG_3054.jpeg",
               title="Love Birds",
               desc="I wanted to draw a cityscape but also fit the prompt, so this is my rather loose interpretation.",
               private=False,
               created=datetime.now(),
               challenge=18,
               user_id="elaine13@email.unc.edu",
               comments=[],
               tags=["urban", "meChallenge"])

models = [
    post0,
    post1,
    post2,
    post3,
    elaine1,
    elaine2,
    elaine3
]
