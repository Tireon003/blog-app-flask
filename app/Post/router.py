from flask import Blueprint
from flask_pydantic import validate

from .services import PostService
from .repository import PostRepository
from app.core import db
from .schemas import (
    CreatePostBodyParams,
    UpdatePostBodyParams,
)


bp = Blueprint("posts", __name__, url_prefix="/api/posts")


@bp.route("/", methods=["POST"])
@validate(on_success_status=201)
def create_post(body: CreatePostBodyParams):
    try:
        service = PostService(PostRepository(db))
        service.create_post(**body.model_dump())
        return {"message": "Post created successfully"}, 201
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=["GET"])
def get_posts():
    try:
        service = PostService(PostRepository(db))
        posts = service.get_posts()
        return posts, 200
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id: int):
    try:
        service = PostService(PostRepository(db))
        post = service.get_post(post_id)
        return post, 200
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id: int):
    try:
        service = PostService(PostRepository(db))
        service.delete_post(post_id)
        return {"message": "Post deleted successfully"}, 204
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:post_id>", methods=["PUT"])
@validate(on_success_status=200)
def update_post(post_id, body: UpdatePostBodyParams):
    try:
        service = PostService(PostRepository(db))
        service.edit_post(post_id, **body.model_dump())
        return {"message": "Post edited successfully"}, 200
    except Exception as e:
        return {"message": str(e)}, 500
