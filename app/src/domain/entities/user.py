from dataclasses import dataclass, field

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class User(AggregateRoot, Entity):
    name: str = field(default="", doc="User name")
    description: str = field(default="", doc="User description")
    profile_picture: str = field(default="", doc="User profile picture")
    cover_picture: str = field(default="", doc="User cover picture")
    email: str = field(default="", doc="User email")
    mobile_number: str = field(default="", doc="User mobile number")
    order_ids: list = field(default_factory=list, doc="User order IDs")
