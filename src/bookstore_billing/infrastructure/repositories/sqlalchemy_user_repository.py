from typing import Optional

from bookstore_billing.application.user_repository import UserRepository
from bookstore_billing.domain.user.user import User


class SqlAlchemyUserRepository(UserRepository):
    def find_by_id(self, user_id: str) -> Optional[User]:
        return User.query.filter_by(id=user_id).first()
