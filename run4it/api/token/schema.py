from marshmallow import Schema, validate, fields


class TokenSchema(Schema):
	id = fields.Integer(dump_only=True, required=True)
	tokenType = fields.Str(attribute='token_type', dump_only=True, required=True)
	username = fields.Str(dump_only=True, required=True)
	revoked = fields.Bool(dump_only=True, required=True)
	expires = fields.DateTime(dump_only=True, required=True)
	
	class Meta:
		strict = True
		datetimeformat = '%Y-%m-%dT%H:%M:%S+00:00' # not: sets timezone to UTC, should only be used on dump


class TokenUpdateSchema(Schema):
	revoked = fields.Bool(load_only=True, required=True)

	class Meta:
		strict = True


token_schema = TokenSchema()
tokens_schema = TokenSchema(many=True)
token_update_schema = TokenUpdateSchema()
