# server/schemas.py
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)

class GuestSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    occupation = fields.Str(required=True)

class EpisodeSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    number = fields.Str(required=True)
    appearances = fields.Nested('AppearanceSchema', many=True, exclude=('episode',))

class AppearanceSchema(Schema):
    id = fields.Int(dump_only=True)
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    guest_id = fields.Int(required=True)
    episode_id = fields.Int(required=True)
    guest = fields.Nested(GuestSchema, only=('id', 'name', 'occupation'))
    episode = fields.Nested(EpisodeSchema, only=('id', 'date', 'number'))