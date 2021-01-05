from app.handlers.response_handlers import ResponseHandler
from app.services.subscriptions_audit_service import subscriptionsAuditService
from app.models.subscription_audit import SubscriptionAudit
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import Optional, Dict
from uuid import UUID


subscription_audit_router = APIRouter()

subscription_audit_service = subscriptionsAuditService()


@subscription_audit_router.delete('/<id>',
                    tags=['Subscription_audits'],
                    summary='Delete subscription_audit by id')
def delete_subscription_audit(id: UUID):
    try:
        deleted = subscription_audit_service.delete_subscription_audit(id)
        if not deleted:
            return ResponseHandler.get_bad_request_400("Subscription_audit already deleted")

        return ResponseHandler.get_deleted_204()
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@subscription_audit_router.get('/<id>',
                    tags=['Subscription_audits'],
                    summary='Get Subscription_audits by id')
def get_subscription_audit_by_id(id: UUID):
    try:
        subscription_audit = subscription_audit_service.get_subscription_audit(id)
        if not subscription_audit:
            return ResponseHandler.get_not_found_404()

        return ResponseHandler.get_ok_200(jsonable_encoder(subscription_audit))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@subscription_audit_router.get('/',
                    tags=['Subscription_audits'],
                    summary='Get all Subscription_audits')
def get_all_subscription_audits():
    try:
        subscription_audits= subscription_audit_service.get_all_subscription_audit()
        return ResponseHandler.get_ok_200(jsonable_encoder(subscription_audits))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))    


@subscription_audit_router.get('/user_audits/<id>',
                    tags=['Subscription_audits'],
                    summary='Get all Subscription_audits for user')
def get_all_subscription_audits_for_user(id: str):
    try:
        subscription_audits = subscription_audit_service.get_all_subscription_audit_by_user_id(id)

        return ResponseHandler.get_ok_200(jsonable_encoder(subscription_audits))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))
