from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import OrderStatus


@dataclass(kw_only=True)
class Order(AggregateRoot, Entity):
    store_id: UUID = field(doc="Store ID")
    user_id: UUID = field(doc="User ID")
    tracking_id: UUID = field(default="", doc="Order tracking")
    payment_id: UUID = field(default="", doc="Order payment information")
    order_line_ids: List[UUID] = field(default_factory=list, doc="Order lines")
    status: Optional[OrderStatus] = field(
        default_factory=lambda: OrderStatus(),
        doc="Order status",
    )
