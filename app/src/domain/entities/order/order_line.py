from dataclasses import dataclass, field

from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class OrderLine(Entity):
    product_id: str = field(default="", doc="Order line product ID")
    quantity: int = field(default=0, doc="Order line quantity")
