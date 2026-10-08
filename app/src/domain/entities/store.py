from dataclasses import dataclass, field
from typing import Optional

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import Email, Image, Mobile


@dataclass(kw_only=True)
class Store(AggregateRoot, Entity):
    name: str = field(doc="Store name")
    description: str = field(doc="Store description")
    profile_image: Optional[Image] = field(default=None, doc="Store profile image")
    cover_image: Optional[Image] = field(default=None, doc="Store cover image")
    email: Optional[Email] = field(default=None, doc="Store email")
    mobile_number: Optional[Mobile] = field(default=None, doc="Store mobile number")
