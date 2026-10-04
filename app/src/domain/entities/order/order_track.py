from dataclasses import dataclass, field

from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class OrderTrack(Entity):
    external_tracking_id: str = field(default="", doc="Order tracking ID")
    delivery_partner: str = field(default="", doc="Order delivery partner")
    stage: str = field(default="", doc="Order tracking stage")
    estimated_delivery_date: str = field(default="", doc="Order delivery date")
    actual_delivery_date: str = field(default="", doc="Order actual delivery date")
