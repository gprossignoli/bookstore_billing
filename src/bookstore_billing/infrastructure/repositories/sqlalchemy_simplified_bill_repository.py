from bookstore_billing.application.simplified_bill_repository import (
    SimplifiedBillRepository,
)
from bookstore_billing.domain.simplified_bill.simplified_bill import SimplifiedBill
from bookstore_billing.settings import db


class SqlAlchemySimplifiedBillRepository(SimplifiedBillRepository):
    def save(self, simplified_bill: SimplifiedBill) -> None:
        session = db.session
        try:
            session.add(simplified_bill)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

    def find_by_user_id(self, user_id: str) -> SimplifiedBill:
        raise NotImplementedError()
