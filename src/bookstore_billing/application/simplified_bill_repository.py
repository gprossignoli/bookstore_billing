from abc import ABC, abstractmethod
from typing import Iterable

from bookstore_billing.domain.simplified_bill.simplified_bill import SimplifiedBill


class SimplifiedBillRepository(ABC):
    @abstractmethod
    def save(self, simplified_bill: SimplifiedBill) -> None:
        pass

    @abstractmethod
    def find_by_user_id(self, user_id: str) -> Iterable[SimplifiedBill]:
        pass
