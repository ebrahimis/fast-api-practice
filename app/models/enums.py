from enum import Enum


class SubscriptionStatus(Enum):
    Active = 1
    Expired = 2
    Cancelled = 3
    PendingCancellation = 4
    PendingActivation = 5


class SubscriptionEventType(Enum):
    StatusChange = 1
    Renewal = 2
    MailingAddressChange = 3
    Cancellation = 4
    Reactivation = 5
    Creation = 6
