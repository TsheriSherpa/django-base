""" Api Service Class """


class ApiService:

    error_code = 422
    error_message = "Something went wrong"

    def setError(self, error_message="Something went wrong", error_code=422):
        self.error_code = error_code
        self.error_message = error_message

    def getErrorMessage(self):
        return self.error_message

    def getErrorCode(self):
        return self.error_code
