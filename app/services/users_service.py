from app.database.user import users
from app.models.user import Users
from sqlalchemy import select, and_
from typing import Optional, Dict, List
from uuid import UUID, uuid4


class usersService():
    """
    Used to handle CRUD operations on database on users table
    """

    def create_user(self, user_data: Dict) -> Optional[Users]:
        """
        Create new user

        :user_data: Object of class users to be inserted to DB
        """
        if not user_data.get('id'):
            user_data['id'] = str(uuid4())
        users.insert().values(user_data).execute()
        return user_data


    def delete_user(self, id: UUID):
        """
        Deletes user by ID

        :param id: UUID user id to be deleted
        """
        user = self.get_user(id)
        if not user:
            return False
        
        users.delete().where(users.c.id == id).execute()
        return True


    def get_all_users(self) -> Optional[List]:
        """
        Get all users registered in DB

        :return: list of users object for all users in DB
        """
        all_users = select([users]).execute().fetchall()
        return all_users


    def get_user(self, id: UUID) -> Optional[Users]:
        """
        get user record from DB by id

        :param id: string the user id
        :return: users object for the targeted user by id
        """
        user = select([users]).where(users.c.id == id).execute().first()
        return user


    def update_user(self, id: UUID, data: Dict):
        """
        Update user data by id by passing object of updated data

        :param id: UUID user id
        :param data: dictionary of data to be updated for this user
        """
        users.update().where(users.c.id == id).values(data).execute()
