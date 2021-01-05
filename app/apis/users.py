from app.handlers.response_handlers import ResponseHandler
from app.services.users_service import usersService
from app.models.user import Users
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import Optional, Dict
from uuid import UUID


users_router = APIRouter()

user_service = usersService()


@users_router.delete('/<id>',
                    tags=['Users'],
                    summary='Delete user by id')
def delete_user(id: UUID):
    try:
        deleted = user_service.delete_user(id)
        if not deleted:
            return ResponseHandler.get_bad_request_400("User already deleted")

        return ResponseHandler.get_deleted_204()
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@users_router.get('/<id>',
                    tags=['Users'],
                    summary='Get user by id')
def get_user_by_id(id: UUID):
    try:
        user = user_service.get_user(id)
        if not user:
            return ResponseHandler.get_not_found_404()

        return ResponseHandler.get_ok_200(jsonable_encoder(user))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@users_router.get('/',
                    tags=['Users'],
                    summary='Get all users')
def get_all_users():
    try:
        users = user_service.get_all_users()
        return ResponseHandler.get_ok_200(jsonable_encoder(users))
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@users_router.patch('/<id>',
                    tags=['Users'],
                    summary='Update user by id')
def update_user(id: UUID, user_data: Users):
    try:
        user_service.update_user(id, jsonable_encoder(user_data))
        return ResponseHandler.get_ok_200("User updated successfully")
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))


@users_router.post('/',
                    tags=['Users'],
                    summary='Create new user')
def create_user(user_data: Users):
    try:
        user = user_service.create_user(jsonable_encoder(user_data))
        return ResponseHandler.get_created_201(user)
    except Exception as e:
        return ResponseHandler.get_bad_request_400(str(e))
        