from abc import ABCMeta, abstractmethod


class Error(metaclass=ABCMeta):
    def __init__(self, status_code):
        self.status_code = status_code

    def get_status_code(self):
        return self.status_code

    @abstractmethod
    def get_error(self):
        pass


class APIError(Error):

    def __init__(self, message, status_code=400):
        super().__init__(status_code)
        self.message = message

    def get_error(self):
        return {"message": self.message}


class ValidationError(Error):

    def __init__(self, errors, status_code=400):
        super().__init__(status_code)
        self.errors = errors

    def get_error(self):
        return self.errors


if __name__ == '__main__':
    api_error = APIError('blah', 400)
    print(isinstance(api_error, Error))
