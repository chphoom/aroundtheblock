from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

#savedPost relationship
savedPost = Table(
    "savedPost_table",
    EntityBase.metadata,
    Column("users", ForeignKey("users.email")),
    Column("posts", ForeignKey("posts.id"))
)