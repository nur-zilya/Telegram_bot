from typing import Dict, List, TypeVar

from peewee import ModelBase

from database.common.models import ModelBase
from ..common.models import db

T = TypeVar("T")

def store_date(db: db, model: T, *data: list[Dict]) -> None:
    with db.atonic():
        model.inser_many(*data).execute()


def retrive_all_data(db: db, model: T, *columns: list[Dict]) -> ModelSelect:
    with db.atonic():
        response = model.select(*columns)

    return response

