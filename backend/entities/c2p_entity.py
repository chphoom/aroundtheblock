from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase


#challenge -> posts relationship
c2p = Table(
    "c2p_table",
    EntityBase.metadata,
    Column("challenges", ForeignKey("challenges.id")),
    Column("posts", ForeignKey("posts.id"))
)