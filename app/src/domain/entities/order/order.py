from dataclasses import dataclass, field

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class Order(AggregateRoot, Entity):
    store_id: str = field(default="", doc="Store ID")
    user_id: str = field(default="", doc="User ID")
    status: str = field(default="", doc="Order status")
    order_line_ids: list = field(default_factory=list, doc="Order lines")
    tracking_id: str = field(default="", doc="Order tracking")
    payment_id: str = field(default="", doc="Order payment information")
