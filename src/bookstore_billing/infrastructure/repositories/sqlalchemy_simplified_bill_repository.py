from bookstore_billing.application.simplified_bill_repository import SimplifiedBillRepository
from bookstore_billing.domain.simplified_bill.simplified_bill import SimplifiedBill


class SqlAlchemySimplifiedBillRepository(SimplifiedBillRepository):
    def save(self, simplified_bill: SimplifiedBill) -> None:
        raise NotImplementedError()

    def find_by_user_id(self, user_id: str) -> SimplifiedBill:
        raise NotImplementedError()
