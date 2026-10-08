from dataclasses import dataclass, field
from uuid import UUID

from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class OrderLine(Entity):
    product_id: UUID = field(doc="Order line product ID")
    quantity: int = field(doc="Order line quantity")
