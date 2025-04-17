import os

from bson import ObjectId
from pymongo import MongoClient


from backend.data.models.user import User
from backend.excpetions.creation_error import CreationError
from backend.excpetions.email_exist_error import EmailExistError
from backend.excpetions.invalid_credentials import IncorrectLoginCredentialsException
from backend.excpetions.password_error import PasswordError
from backend.excpetions.patient_error import PatientNotFoundException


class UserRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('USERS_COLLECTION')]



    def existed_email(self, email) -> bool:
        return self.collection.find_one({'email': email})

    def create_user(self,data: dict) -> dict:
        if self.existed_email(data['email']):
            return EmailExistError(data["email"])


        if data['password'].strip() == "" or len(data['password'].strip()) < 6:
            return PasswordError("Password must be at least 6 characters long")

        user = User(**data, hash_password="")
        user.set_password(password=data["password"])
        try:
            result = self.collection.insert_one(user.__dict__)
            user_dict = self.get_user_by_id(result.inserted_id)
            return user_dict
        except Exception:
            raise CreationError("Failed to create user")

    def get_user_by_id(self, user_id: str) -> dict:
        user = self.collection.find_one({'_id': ObjectId(user_id)})
        if not user:
            raise PatientNotFoundException(user_id)
        return user

    def login_user(self, email: str, password: str) -> User:
        user_data = self.get_user_by_email(email)
        if not user_data:
            raise IncorrectLoginCredentialsException()

        user = User(**user_data)
        if not user.check_password(password):
            raise IncorrectLoginCredentialsException()

        return user
