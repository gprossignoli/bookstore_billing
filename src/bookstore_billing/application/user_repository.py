from abc import ABC, abstractmethod

from bookstore_billing.domain.user.user import User


class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: str) -> User:
        pass
