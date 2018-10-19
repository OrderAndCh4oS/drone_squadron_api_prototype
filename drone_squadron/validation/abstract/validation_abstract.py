from abc import ABCMeta, abstractmethod


class ValidationAbstract(metaclass=ABCMeta):

    def __init__(self, error_message: str):
        self.error_message = error_message

    def __call__(self, field):
        self.validate(field)
        return field

    def validation_check(self, field, check):
        if not check:
            field.invalidate()
            field.set_error_message(self.error_message)

    @abstractmethod
    def validate(self, field):
        pass
