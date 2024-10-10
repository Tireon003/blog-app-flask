from flask import Blueprint
from flask_pydantic import validate

from app.core import db
from .repository import CommentRepository
from .services import CommentService
from .schemas import (
    CreateCommentBodyParams,
    GetCommentsQueryParams,
    UpdateCommentBodyParams,
)

bp = Blueprint('comments', __name__, url_prefix='/api/comments')


@bp.route("/", methods=["POST"])
@validate(on_success_status=201)
def create_comment(body: CreateCommentBodyParams):
    try:
        service = CommentService(CommentRepository(db))
        service.add_comment(**body.model_dump())
        return {"message": "Comment created"}, 201
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/", methods=["GET"])
@validate(on_success_status=200)
def get_comments(query: GetCommentsQueryParams):
    post_id = query.post_id
    try:
        service = CommentService(CommentRepository(db))
        comments = service.get_comments(post_id=post_id)
        return comments, 200
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:comment_id>", methods=["PATCH"])
@validate(on_success_status=200)
def update_comment(comment_id: int, body: UpdateCommentBodyParams):
    new_content = body.content
    try:
        service = CommentService(CommentRepository(db))
        service.edit_comment(
            comment_id=comment_id,
            content=new_content,
        )
        return {"message": "Comment updated"}, 200
    except Exception as e:
        return {"message": str(e)}, 500


@bp.route("/<int:comment_id>", methods=["DELETE"])
@validate(on_success_status=204)
def delete_comment(comment_id: int):
    try:
        service = CommentService(CommentRepository(db))
        service.delete_comment(comment_id)
        return {"message": "Comment deleted"}, 204
    except Exception as e:
        return {"message": str(e)}, 500
