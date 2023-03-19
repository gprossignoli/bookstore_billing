from dataclasses import dataclass


@dataclass(frozen=True)
class PurchaseBook:
    book_id: int
    quantity: int
    price: int
