from dataclasses import dataclass, field

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class Store(AggregateRoot, Entity):
    name: str = field(default="", doc="Store name")
    description: str = field(default="", doc="Store description")
    profile_picture: str = field(default="", doc="Store profile picture")
    cover_picture: str = field(default="", doc="Store cover picture")
    email: str = field(default="", doc="Store email")
    mobile_number: str = field(default="", doc="Store mobile number")
