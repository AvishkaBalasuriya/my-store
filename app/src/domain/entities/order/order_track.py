from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import TrackingStage


@dataclass(kw_only=True)
class OrderTrack(Entity):
    external_tracking_id: UUID = field(doc="Order tracking ID")
    delivery_partner_id: UUID = field(doc="Order delivery partner ID")
    stage: Optional[TrackingStage] = field(
        default_factory=lambda: TrackingStage(), doc="Order tracking stage"
    )
    estimated_delivery_date: Optional[datetime] = field(
        default=None, doc="Order delivery date"
    )
    actual_delivery_date: Optional[datetime] = field(
        default=None, doc="Order actual delivery date"
    )
