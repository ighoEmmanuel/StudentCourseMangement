class IncorrectLoginCredentialsException(Exception):
    def __init__(self):
        self.message = "Incorrect login credentials."
        super().__init__(self.message)
