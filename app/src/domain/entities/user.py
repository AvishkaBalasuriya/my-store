from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from src.domain.shared.entities.aggregate_root import AggregateRoot
from src.domain.shared.entities.entity import Entity
from src.domain.value_objects import Email, Image, Mobile


@dataclass(kw_only=True)
class User(AggregateRoot, Entity):
    name: str = field(doc="User name")
    profile_image: Optional[Image] = field(default=None, doc="User profile image")
    cover_image: Optional[Image] = field(default=None, doc="User cover image")
    email: Optional[Email] = field(default=None, doc="User email")
    mobile_number: Optional[Mobile] = field(default=None, doc="User mobile number")
    order_ids: Optional[list[UUID]] = field(
        default_factory=lambda: list(), doc="User order IDs"
    )

    @classmethod
    def create(cls, **kwargs):
        kwargs = {
            "name": kwargs.get("name"),
            "profile_image": (
                Image(url=kwargs.get("profile_image"))
                if kwargs.get("profile_image")
                else None
            ),
            "cover_image": (
                Image(url=kwargs.get("cover_image"))
                if kwargs.get("cover_image")
                else None
            ),
            "email": Email(address=kwargs.get("email")) if kwargs.get("email") else None,
            "mobile_number": (
                Mobile(
                    country_code=kwargs.get("country_code"),
                    number=kwargs.get("mobile_number"),
                )
                if kwargs.get("mobile_number") and kwargs.get("country_code")
                else None
            ),
            "order_ids": kwargs.get("order_ids") or [],
        }

        return cls(**kwargs)
