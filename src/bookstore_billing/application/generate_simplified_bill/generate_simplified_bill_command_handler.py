from bookstore_billing.application.command_handler import CommandHandler
from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command import \
    GenerateSimplifiedBillCommand
from bookstore_billing.application.simplified_bill_repository import SimplifiedBillRepository
from bookstore_billing.application.user_repository import UserRepository
from bookstore_billing.domain.simplified_bill.simplified_bill import SimplifiedBill


class GenerateSimplifiedBillCommandHandler(CommandHandler):
    def __init__(self, simplified_bill_repository: SimplifiedBillRepository, user_repository: UserRepository):
        self.__simplified_bill_repository = simplified_bill_repository
        self.__user_repository = user_repository

    def execute(self, command: GenerateSimplifiedBillCommand) -> None:
        user = self.__user_repository.find_by_id(command.user_id)
        if user is not None:
            # simplified_bill = SimplifiedBill(user_id=command.user_id, )
            pass
