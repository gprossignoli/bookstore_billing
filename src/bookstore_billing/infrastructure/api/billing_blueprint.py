from flask import Blueprint

from bookstore_billing.application.simplified_bill_serializer import SimplifiedBillSerializer
from bookstore_billing.infrastructure.repositories.sqlalchemy_simplified_bill_repository import \
    SqlAlchemySimplifiedBillRepository

billing_blueprint = Blueprint(name="billing", import_name=__name__, url_prefix="/billing")


@billing_blueprint.route("user/<user_id>")
def get_user_billing(user_id: str):
    simplified_bill_repository = SqlAlchemySimplifiedBillRepository()

    bills = simplified_bill_repository.find_by_user_id(user_id=user_id)
    simplified_bill_serializer = SimplifiedBillSerializer()
    serialized_bills = [simplified_bill_serializer.serialize(bill) for bill in bills]
    return serialized_bills, 200
