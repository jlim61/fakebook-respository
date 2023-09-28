from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt

from resources.users.models import UserModel

from sqlalchemy.exc import IntegrityError
from.PostModel import PostModel
from schemas import PostSchema
from . import bp
from db import posts

@bp.route('/')
class PostList(MethodView):

  # get all posts
  # in insomnia, to send access token, is "Bearer {valid access token}"
  @jwt_required()
  @bp.response(200, PostSchema(many=True))
  def get(self):
    return PostModel.query.all()

# create post
  @jwt_required()
  @bp.arguments(PostSchema)
  @bp.response(200, PostSchema)
  def post(self, post_data):
    user_id = get_jwt_identity()
    p = PostModel(**post_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message='Invalid User ID')

@bp.route('/<post_id>')
class Post(MethodView):

  # get one post
  @jwt_required()
  @bp.response(200, PostSchema)
  def get(self,post_id):
    p = PostModel.query.get(post_id)
    if p:
      return p
    abort(400, message='Invalid Post ID')

# edit a post
  @jwt_required()
  @bp.arguments(PostSchema)
  @bp.response(200, PostSchema)
  # data comes before our dynamic URL variable (post_id)
  def put(self, post_data, post_id):
    p = PostModel.query.get(post_id)
    if p and post_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = post_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Post Data')

# delete a post
  @jwt_required()
  def delete(self,post_id):
    user_id = get_jwt_identity()
    p = PostModel.query.get(post_id)
    if p:
      if p.user_id == user_id:
        p.delete()
        return {'message': 'Post Deleted'}, 202
      abort(400, message='User doesn\'t have rights')
    abort(400, message='Invalid Post ID')