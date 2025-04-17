from backend.data.repositories.user_repository import UserRepository

import bcrypt

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")



class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo = user_repo


    def create_user(self, data:dict) -> dict:
        data["password"] = hash_password(data["password"])
        user = self.user_repo.create_user(data)
        return user


    def login_user(self,email,password):
        return self.user_repo.login_user(email,password)



