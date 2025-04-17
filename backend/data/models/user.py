import dataclasses

import bcrypt


@dataclasses
class User:
    __first_name: str
    __last_name: str
    __email: str
    __password: str

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.__password.encode('utf-8'))

