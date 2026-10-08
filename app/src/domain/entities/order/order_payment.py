from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID

from app.src.domain.shared.entities.aggregate_root import AggregateRoot
from app.src.domain.shared.entities.entity import Entity
from app.src.domain.value_objects import PaymentMethod, PaymentStatus, Price


@dataclass(kw_only=True)
class OrderPayment(Entity):
    payment_id: UUID = field(default="", doc="Order payment ID")
    payment_method: PaymentMethod = field(doc="Order payment method")
    payment_date: datetime = field(doc="Order payment date")
    total_amount: Price = field(doc="Order total amount")
    payment_status: Optional[PaymentStatus] = field(
        default_factory=lambda: PaymentStatus(), doc="Order payment status"
    )
