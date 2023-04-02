from typing import Dict, List, TypeVar

from peewee import ModelBase

from database.common.models import ModelBase
from ..common.models import db

T = TypeVar("T")

def _store_date(db: db, model: T, *data: list[Dict]) -> None:
    with db.atomic():
        model.insert_many(*data).execute()


def _retrive_all_data(db: db, model: T, *columns: list[Dict]):
    with db.atomic():
        response = model.select(*columns)

    return response

class CRUDInterface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrive():
        return _retrive_all_data


if __name__ == "__main__":
    _store_date()
    _retrive_all_data()
    CRUDInterface()