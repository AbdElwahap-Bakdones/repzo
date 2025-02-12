from marshmallow import Schema, fields, validate


class OrderCreateValidationSchema(Schema):
    partner_id = fields.Int(required=True, error_messages={
                            "required": "Partner ID is required."})
    order_line = fields.List(fields.Dict(), required=True, error_messages={
                             "required": "Order lines are required."})
    date_order = fields.Date(required=False)
    state = fields.Str(required=False, validate=validate.OneOf(
        ["draft", "sent", "sale", "done", "cancel"]))

    # Additional fields can be added as per your requirements
