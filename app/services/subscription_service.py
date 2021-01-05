from app.database.subscription import subscriptions
from app.database.user import users
from app.models.subscription import Subscription, SubscriptionStatus
from sqlalchemy import select, and_
from typing import Optional, Dict, List
from uuid import UUID, uuid4


class subscriptionsService():
    """
    Used to handle CRUD operations on database on subscriptions table
    """

    def create_subscription(self, subscription_data: Dict) -> Optional[Subscription]:
        """
        Create new subscription

        :subscription_data: Object of class subscriptions to be inserted to DB
        """
        if not subscription_data.get('id'):
            subscription_data['id'] = str(uuid4())
        subscriptions.insert().values(subscription_data).execute()
        return subscription_data


    def get_all_subscriptions(self) -> Optional[List]:
        """
        Get all subscriptions registered in DB

        :return: list of subscriptions object for all subscriptions in DB
        """
        all_subscriptions = select([subscriptions]).execute().fetchall()
        return all_subscriptions


    def get_all_subscriptions_with_users(self):
        """
        Get all subscriptions with users related to them registered in DB

        :return: list of details for users and subscriptions object from DB
        """
        all_data = select([subscriptions, users.c.name, users.c.email]).select_from(
            subscriptions.join(
                users,
                users.c.id == subscriptions.c.purchaser_id
            )
        ).execute().fetchall()

        return all_data


    def get_subscription(self, id: UUID) -> Optional[Subscription]:
        """
        get subscription record from DB by id

        :param id: string the subscription id
        :return: subscriptions object for the targeted subscription by id
        """
        subscription = select([subscriptions]).where(subscriptions.c.id == id).execute().first()
        return subscription


    def update_subscription(self, id: UUID, data: Dict):
        """
        Update subscription data by id by passing object of updated data

        :param id: UUID subscription id
        :param data: dictionary of data to be updated for this subscription
        """
        subscriptions.update().where(subscriptions.c.id == id).values(data).execute()
        return data
