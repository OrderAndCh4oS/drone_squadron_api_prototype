from drone_squadron.validation.abstract.validation_abstract import ValidationAbstract
from drone_squadron.validation.field import Field


class IsRequired(ValidationAbstract):
    def __init__(self, error_message='is required'):
        super().__init__(error_message)

    def validate(self, field: Field):
        self.validation_check(field, bool(field.get_value()))
        return field


class IsString(ValidationAbstract):
    def __init__(self, error_message='is not a string'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, isinstance(field.get_value(), str))
        return field


class IsInteger(ValidationAbstract):
    def __init__(self, error_message='is not an integer'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, isinstance(field.get_value(), int))
        return field


class IsList(ValidationAbstract):
    def __init__(self, error_message='is not a list'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, isinstance(field.get_value(), list))
        return field


class IsCallable(ValidationAbstract):
    def __init__(self, error_message='is not a list'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, True)
        return field


class IsBoolean(ValidationAbstract):
    def __init__(self, error_message='is not a boolean'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, isinstance(field.get_value(), bool))
        return field


class IsFloat(ValidationAbstract):
    def __init__(self, error_message='is not a float'):
        super().__init__(error_message)

    def validate(self, field):
        self.validation_check(field, isinstance(field.get_value(), float))
        return field


class MaxLength(ValidationAbstract):
    def __init__(self, maximum, error_message='is too long'):
        super().__init__(error_message)
        self.max = maximum

    def validate(self, field):
        self.validation_check(field, len(field.get_value()) <= self.max)
        return field


class MinLength(ValidationAbstract):
    def __init__(self, minimum, error_message='is too short'):
        super().__init__(error_message)
        self.min = minimum

    def validate(self, field):
        self.validation_check(field, len(field.get_value()) >= self.min)
        return field


class MaxValue(ValidationAbstract):
    def __init__(self, maximum, error_message='is too high'):
        super().__init__(error_message)
        self.max = maximum

    def validate(self, field):
        self.validation_check(field, field.get_value() <= self.max)
        return field


class MinValue(ValidationAbstract):
    def __init__(self, minimum, error_message='is too low'):
        super().__init__(error_message)
        self.min = minimum

    def validate(self, field):
        self.validation_check(field, field.get_value() >= self.min)
        return field
