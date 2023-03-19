import uuid

from bookstore_billing.settings import db


class SimplifiedBill(db.Model):
    __tablename__ = "simplified_bills"

    id = db.Column(db.String, primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    user_first_name = db.Column(db.String, nullable=False)
    user_last_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    book_id = db.Column(db.String, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @property
    def total_cost(self) -> int:
        return self.unit_price * self.quantity
