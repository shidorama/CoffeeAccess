import datetime
import uuid

from mongoengine import fields

from models import db


class ControllerState(db.Document):
    state_update = fields.DateTimeField(required=True, default=lambda: datetime.datetime.now())
    # wallet_id = fields.UUIDField(required=True, default=lambda: str(uuid.uuid4()), primary_key=True)
