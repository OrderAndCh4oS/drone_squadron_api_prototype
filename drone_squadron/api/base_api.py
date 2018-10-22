from abc import ABCMeta

from sqlalchemy.engine import ResultProxy


class BaseApi(metaclass=ABCMeta):

    def __init__(self, crud):
        self.crud = crud

    def get(self):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            data = result.fetchall()
        return data

    def get_by_id(self, item_id):
        with self.crud() as crud:
            result = crud.select_by_id(item_id)  # type: ResultProxy
            data = result.fetchone()
        return data

    def post(self, data):
        with self.crud() as crud:
            result = crud.insert(**data)  # type: ResultProxy
            data = result.last_inserted_params()
            data['id'] = result.inserted_primary_key[0]
        return data

    def put(self, item_id, data):
        with self.crud() as crud:
            result = crud.update(item_id=item_id, **data)  # type: ResultProxy
            data = result.last_updated_params()
        return data

    def delete(self, item_id):
        with self.crud() as crud:
            result = crud.delete(item_id=item_id)  # type: ResultProxy
            matched_rows = result.rowcount
        return {"deleted_rows": matched_rows}
