from app.handlers.response_handlers import ResponseHandler
from app.services.subscription_service import subscriptionsService
from app.services.subscriptions_audit_service import subscriptionsAuditService, SubscriptionEventType
from app.models.subscription import Subscription, SubscriptionStatus
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import Optional, Dict
from uuid import UUID


subscriptions_router = APIRouter()

subscription_service = subscriptionsService()
subscription_audit_service = subscriptionsAuditService()


@subscriptions_router.get('/<id>',
                    tags=['Subscriptions'],
                    summary='Get subscription by id')
def get_subscription_by_id(id: UUID):
    try:
        subscription = subscription_service.get_subscription(id)
        if not subscription: 
            return ResponseHandler.get_not_found_404()

        return ResponseHandler.get_ok_200(jsonable_encoder(subscription))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@subscriptions_router.get('/',
                    tags=['Subscriptions'],
                    summary='Get all subscriptions')
def get_all_subscriptions():
    try:
        subscriptions = subscription_service.get_all_subscriptions_with_users()
        return ResponseHandler.get_ok_200(jsonable_encoder(subscriptions))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@subscriptions_router.patch('/<id>',
                    tags=['Subscriptions'],
                    summary='Update subscription by id')
def update_subscription(id: UUID, subscription_data: Subscription):
    try:
        subscription = subscription_service.update_subscription(id, jsonable_encoder(subscription_data))
        # adding audit record as logs for operations
        # IMPORTANT to update the UPDATED_BY by a user id you created
        subscription_audit_service.create_subscription_audit({
            'subscription_id' : id,
            'event_type': SubscriptionEventType.StatusChange.value,
            'event': jsonable_encoder(subscription),
            'updated_by': 'test'
        })
        return ResponseHandler.get_ok_200("Subscription updated successfully")
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@subscriptions_router.post('/',
                    tags=['Subscriptions'],
                    summary='Create new subscription')
def create_subscription(subscription_data: Subscription):
    try:
        subscription = subscription_service.create_subscription(jsonable_encoder(subscription_data))
        # adding audit record as logs for operations
        # IMPORTANT to update the UPDATED_BY by a user id you created
        subscription_audit_service.create_subscription_audit({
            'subscription_id' : subscription.get('id'),
            'event_type': SubscriptionEventType.Creation.value,
            'event': jsonable_encoder(subscription),
            'updated_by': 'test'
        })
        return ResponseHandler.get_created_201(subscription)
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))
        