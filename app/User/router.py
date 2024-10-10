from flask import Blueprint
from flask_pydantic import validate

from .schemas import (
    UserID,
    ResponseUserSchema,
    UserCreateBodySchema,
    UserResponseSchema,
    UserUpdateBodySchema,
)
from .services import UserService
from .repository import UserRepository
from app.core import db


bp = Blueprint("users", __name__, url_prefix="/api/users")


@bp.route("/", methods=["GET"])
@validate(on_success_status=200)
def get_user(query: UserID) -> ResponseUserSchema:
    user_id = query.id
    try:
        service = UserService(UserRepository(db))
        user = service.get_by_id(user_id)
        if user:
            return ResponseUserSchema.model_validate(user)
        return {"message": "User not found"}, 404
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=['POST'])
@validate(on_success_status=201)
def create_new_user(body: UserCreateBodySchema) -> UserResponseSchema:
    try:
        service = UserService(UserRepository(db))
        service.create_user(
            username=body.username,
            hashed_password=body.password,  # todo implement hashing
            role_id=body.role_id,
            email=body.email,
            date_of_birth=body.date_of_birth,
        )
        return UserResponseSchema(**{
            "message": "User created",
            "status": 201,
        })
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=['PATCH'])
@validate(on_success_status=200)
def update_user_data(body: UserUpdateBodySchema, query: UserID) -> UserResponseSchema:
    user_id = query.id
    to_update_data = body.model_dump()
    try:
        service = UserService(UserRepository(db))
        service.set_new_params(
            user_id=user_id,
            **to_update_data
        )
        return UserResponseSchema(**{
            "message": "User edited",
            "status": 200,
        })
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=['DELETE'])
@validate(on_success_status=204)
def create_user(query: UserID) -> UserResponseSchema:
    try:
        service = UserService(UserRepository(db))
        service.remove_user(query.id)
        return UserResponseSchema(**{
            "message": "User removed",
            "status": 204,
        })
    except Exception as e:
        return {"message": str(e)}, 500
