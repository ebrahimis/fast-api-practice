from app.database.subscription_audit import subscription_audit
from app.models.subscription_audit import SubscriptionAudit, SubscriptionEventType
from sqlalchemy import select, and_
from typing import Optional, Dict, List
from uuid import UUID, uuid4


class subscriptionsAuditService():
    """
    Used to handle CRUD operations on database on subscription_audit table
    """

    def create_subscription_audit(self, subscription_audit_data: Dict) -> Optional[SubscriptionAudit]:
        """
        Create new subscription_audit

        :subscription_audit_data: Object of class subscription_audit to be inserted to DB
        """
        if not subscription_audit_data.get('id'):
            subscription_audit_data['id'] = str(uuid4())
        subscription_audit.insert().values(subscription_audit_data).execute()
        return subscription_audit_data


    def delete_subscription_audit(self, id: UUID):
        """
        Deletes subscription_audit by ID

        :param id: UUID subscription_audit id to be deleted
        """
        subscription_audit.delete().where(subscription_audit.c.id == id).execute()
        return True


    def delete_subscription_audit_by_user_id(self, id: UUID):
        """
        Deletes all subscription_audit records from DB for the user by user_id

        :param id: UUID user_id
        """
        subscription_audit.delete().where(subscription_audit.c.updated_by == id).execute()


    def get_all_subscription_audit(self) -> Optional[List]:
        """
        Get all subscription_audit registered in DB

        :return: list of subscription_audit object for all subscription_audit in DB
        """
        all_subscriptions_audit = select([subscription_audit]).execute().fetchall()
        return all_subscriptions_audit


    def get_all_subscription_audit_by_user_id(self, id: str) -> Optional[SubscriptionAudit]:
        """
        Get all subscription_audit records related to user by user id

        :param id: UUID user_id to be mapped with the updated_by fieled
        :return: list of subscription_audit records for the same user_id and empty list if not
        """
        user_subscription_audits = select([subscription_audit]).where(subscription_audit.c.updated_by == id).execute().fetchall()
        return user_subscription_audits


    def get_subscription_audit(self, id: UUID) -> Optional[SubscriptionAudit]:
        """
        get subscription_audit record from DB by id

        :param id: string the subscription_audit id
        :return: subscription_audit object for the targeted subscription_audit by id
        """
        audit = select([subscription_audit]).where(subscription_audit.c.id == id).execute().first()
        return audit


    def update_subscription_audit(self, id: UUID, data: Dict):
        """
        Update subscription_audit data by id by passing object of updated data

        :param id: UUID subscription_audit id
        :param data: dictionary of data to be updated for this subscription_audit
        """
        subscription_audit.update().where(subscription_audit.c.id == id).values(data).execute()
