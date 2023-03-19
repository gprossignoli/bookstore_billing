from dataclasses import dataclass

from bookstore_billing.application.command import Command
from bookstore_billing.domain.purchase_book.purchase_book import PurchaseBook


@dataclass(frozen=True)
class GenerateSimplifiedBillCommand(Command):
    user_id: str
    purchase: PurchaseBook

    @classmethod
    def fqn(cls) -> str:
        return "command.generate_simplified_bill"
