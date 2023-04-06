from sqlalchemy import Table, Column, ForeignKey
from .entity_base import EntityBase

#savedChallenge relationship
savedChallenge = Table(
    "savedChallenge_table",
    EntityBase.metadata,
    Column("users", ForeignKey("users.email")),
    Column("challenges", ForeignKey("challenges.id"))
)