from typing import Optional, List

from project.dao import UsersDAO
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_token, update_token


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[User]:
        return self.dao.get_all(page=page)

    def create_user(self, email, password):
        return self.dao.create_user(email=email, password=password)

    def get_user_by_email(self, email) -> User:
        return self.dao.get_user_by_email(email=email)

    def check(self, email, password):
        user = self.get_user_by_email(email)
        return generate_token(email=email, password=password, password_hash=user.password)

    def update_token(self, access_token, refresh_token):
        return update_token(refresh_token=refresh_token)


