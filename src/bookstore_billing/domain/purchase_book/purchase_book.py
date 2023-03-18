from dataclasses import dataclass


@dataclass(frozen=True)
class PurchaseBook:
    id: int
    book_id: int
    user_id: str
    quantity: int
    price: int
