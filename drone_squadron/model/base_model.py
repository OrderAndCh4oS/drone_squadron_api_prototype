from abc import ABCMeta, abstractmethod


class BaseModel(metaclass=ABCMeta):

    def __init__(self):
        self._errors = {}

    def add_error(self, field, error):
        self._errors[field] = error

    def get_errors(self):
        return self._errors

    def check_field(self, field, validation):
        if not validation.is_valid():
            self.add_error(field, validation.get_error_message())

    def is_valid(self):
        return not bool(self._errors)

    @abstractmethod
    def validate(self):
        pass
