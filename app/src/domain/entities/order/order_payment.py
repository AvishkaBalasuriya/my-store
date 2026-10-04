from dataclasses import dataclass, field

from app.src.domain.shared.entities.entity import Entity


@dataclass(kw_only=True)
class OrderPayment(Entity):
    payment_id: str = field(default="", doc="Order payment ID")
    payment_method: str = field(default="", doc="Order payment method")
    payment_status: str = field(default="", doc="Order payment status")
    payment_date: str = field(default="", doc="Order payment date")
    total_amount: float = field(default=0.0, doc="Order total amount")
