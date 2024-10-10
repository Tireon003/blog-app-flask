from flask import Blueprint
from flask_pydantic import validate

from app.core import db
from .services import RoleService
from .repository import RoleRepository
from .schemas import (
    CreateRoleQueryParams,
)


bp = Blueprint("roles", __name__, url_prefix="/api/roles")


@bp.route("/", methods=["POST"])
@validate(on_success_status=201)
def create_role(query: CreateRoleQueryParams):
    role_name = query.name
    try:
        service = RoleService(RoleRepository(db))
        service.create_role(role_name=role_name)
        return {"message": "Role created"}, 201
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=["GET"])
def get_all_roles():
    try:
        service = RoleService(RoleRepository(db))
        roles = service.get_roles()
        return roles, 200
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:role_id>", methods=["DELETE"])
def delete_role(role_id: int):
    try:
        service = RoleService(RoleRepository(db))
        service.delete_role(role_id=role_id)
        return {"message": "Role deleted"}, 204
    except Exception as e:
        return {"message": str(e)}, 500
