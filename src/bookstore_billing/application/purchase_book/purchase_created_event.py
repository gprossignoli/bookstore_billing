from dataclasses import dataclass

from bookstore_billing.domain.event import Event


@dataclass(frozen=True)
class PurchaseCreatedEvent(Event):
    book_id: int
    quantity: int
    price: int
    user_id: str

    @property
    def unique_identifier(self) -> str:
        return "event.purchase.purchase_book.purchase_created"
