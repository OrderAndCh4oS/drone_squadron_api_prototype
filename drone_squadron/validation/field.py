from abc import ABCMeta

from drone_squadron.validation.validation_link import ValidationLink


class Field(metaclass=ABCMeta):

    def __init__(self, value):
        self._value = value
        self._is_valid = True
        self._error_message = None
        self._validation_links = []

    def is_valid(self):
        return self._is_valid

    def invalidate(self):
        self._is_valid = False

    def set_error_message(self, error_message):
        self._error_message = error_message

    def get_error_message(self):
        return self._error_message

    def add(self, validation):
        ValidationLink(self._validation_links, validation)
        return self

    def validate(self):
        return self._validation_links[0](self)

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
