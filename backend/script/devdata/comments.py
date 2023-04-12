"""Sample Comment models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Comment
from datetime import datetime, timedelta

c0 = Comment(
    id=0,
    commenter="lucy@lucy.com",
    post=3,
    replies=[],
    text="some comment",
    created=datetime.now()
)

c1 = Comment(
    id=1,
    commenter="olivia@olivia.com",
    post=3,
    replies=[],
    text="some comment",
    created=datetime.now()
)



models = [
    c0, c1
]
