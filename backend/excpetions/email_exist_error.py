class EmailExistError(Exception):
    def __init__(self, email):
        self.message = f"Email already exist: {email}"
        super().__init__(self.message)