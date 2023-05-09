"""Sample Comment models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Comment
from datetime import datetime

c0 = Comment(
    id=1,
    commenter="lucy@lucy.com",
    post=7,
    replies=[],
    text="Very nice.",
    created=datetime.now()
)

c1 = Comment(
    id=2,
    commenter="olivia@olivia.com",
    post=1,
    replies=[],
    text="I love it!",
    created=datetime.now()
)

c2 = Comment(
    id=3,
    commenter="elaine13@email.unc.edu",
    post=18,
    replies=[],
    text="sorry <3",
    created=datetime.now()
)

models = [
    c0, c1, c2
]
