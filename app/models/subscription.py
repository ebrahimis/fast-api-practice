from app.models.enums import SubscriptionStatus
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional, Any
from uuid import UUID


class Subscription(BaseModel):
    """
    Represents a subscription record. For any given order,
    we'd create a subscription record per
    """
    id: Optional[UUID]
    client_id: UUID
    offer_id: UUID
    offer_instance_id: UUID
    purchaser_id: UUID
    is_gift: bool
    begin_date: Optional[datetime]
    end_date: Optional[datetime]
    is_trial: bool
    num_trials: int
    is_auto_renew: bool
    last_renew_date: Optional[datetime]
    next_renew_date: Optional[datetime]
    updated_at: Optional[datetime]
    status_id: SubscriptionStatus


    class Config:
        orm_mode = True
