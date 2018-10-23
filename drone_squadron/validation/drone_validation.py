from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.squadron_crud import SquadronCrud
from drone_squadron.validation.abstract.validation_abstract import ValidationAbstract


class SquadCanAffordPurchase(ValidationAbstract):
    def validate(self, field):
        squadron_id = field.get_value()[0]
        cost = field.get_value()[1]
        with SquadronCrud() as crud:
            result = crud.select_by_id(squadron_id)  # type: ResultProxy
            squadron = result.fetchone()
        if not squadron:
            self.validation_check(field, False)
            field.set_error_message("Squadron not found")
        if squadron.scrap < cost:
            self.validation_check(field, False)
            field.set_error_message("Not enough scrap")

        return field
