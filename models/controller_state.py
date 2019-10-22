import datetime

from mongoengine import fields

from consts.maintenance_state import MaintenanceState
from models import db


class ControllerState(db.Document):
    state_update = fields.DateTimeField(required=True, default=lambda: datetime.datetime.now())
    mm_state = fields.StringField(required=True, default=lambda: MaintenanceState.NONE)
    em_state = fields.StringField(required=True, default=lambda: MaintenanceState.NONE)
    em_due = fields.DateTimeField()
    mm_due = fields.DateTimeField()

    # wallet_id = fields.UUIDField(required=True, default=lambda: str(uuid.uuid4()), primary_key=True)
