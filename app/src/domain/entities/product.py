from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import Image, Price


@dataclass(kw_only=True)
class Product(AggregateRoot, Entity):
    store_id: UUID = field(doc="Store ID")
    name: str = field(doc="Product name")
    description: str = field(doc="Product description")
    price: Price = field(doc="Product price")
    quantity: Optional[int] = field(default=0, doc="Product quantity")
    photos: Optional[List[Image]] = field(default=None, doc="Product photos")
