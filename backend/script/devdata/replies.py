"""Sample Comment models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Comment
from datetime import datetime

c1 = Comment(
    id=1,
    commenter="olivia@olivia.com",
    post=3,
    replies=[],
    text="some reply",
    created=datetime.now()
)

models = [
    c1
]
