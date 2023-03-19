from bookstore_billing.domain.simplified_bill.simplified_bill import SimplifiedBill


class SimplifiedBillSerializer:
    def serialize(self, bill: SimplifiedBill) -> dict:
        return {
            "id": bill.id,
            "user_first_name": bill.user_first_name,
            "user_last_name": bill.user_last_name,
            "user_email": bill.user_email,
            "book_id": bill.book_id,
            "unit_price": bill.unit_price,
            "quantity": bill.quantity,
            "total_cost": bill.total_cost,
            "created_at": bill.created_at,
        }
