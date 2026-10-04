from dataclasses import dataclass, field

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class Product(AggregateRoot, Entity):
    store_id: str = field(default="", doc="Store ID")
    name: str = field(default="", doc="Product name")
    description: str = field(default="", doc="Product description")
    photos: str = field(default="", doc="Product photos")
    quantity: int = field(default=0, doc="Product quantity")
    price: float = field(default=0.0, doc="Product price")
