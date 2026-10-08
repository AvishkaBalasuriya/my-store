from dataclasses import dataclass, field
from typing import Optional

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import Email, Image, Mobile


@dataclass(kw_only=True)
class User(AggregateRoot, Entity):
    name: str = field(doc="User name")
    profile_image: Optional[Image] = field(default=None, doc="User profile image")
    cover_image: Optional[Image] = field(default=None, doc="User cover image")
    email: Optional[Email] = field(default=None, doc="User email")
    mobile_number: Optional[Mobile] = field(default=None, doc="User mobile number")
    order_ids: list = field(default_factory=list, doc="User order IDs")
