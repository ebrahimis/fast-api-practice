from app.models.enums import SubscriptionEventType
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID


class SubscriptionAudit(BaseModel):
    """
    Represents a subscription record. For any given order,
    we'd create a subscription record per
    """
    id: Optional[UUID]
    subscription_id: UUID
    event_type: SubscriptionEventType
    event: Any
    updated_by: str

    class Config:
        orm_mode = True
