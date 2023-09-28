from marshmallow import Schema, fields

class PostSchema(Schema):
    # when we make id, we get id. if we are requesting info, id not required
    id = fields.Str(dump_only=True)
    body = fields.Str(required=True)
    timestamp = fields.Str(dump_only=True)
    user_id = fields.Int(dump_only=True)
    # user = fields.Nested(UserSchema(), dump_only = True)

class UserSchema(Schema):
    # not expecting id, but we will send one back = dump only
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    # we expect a password but never send one back = load only
    password = fields.Str(required=True, load_only = True)
    # taking an optional first name, last name
    first_name = fields.Str()
    last_name = fields.Str()
    

class UserSchemaNested(UserSchema):
   posts = fields.List(fields.Nested(PostSchema), dump_only=True)
   followed = fields.List(fields.Nested(UserSchema), dump_only=True)

class UpdateUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class AuthUserSchema(Schema):
   username = fields.Str()
   email = fields.Str()
   password = fields.Str(required=True, load_only = True)