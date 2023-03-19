from bookstore_billing.application.command_handler import CommandHandler
from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command import \
    GenerateSimplifiedBillCommand


class GenerateSimplifiedBillCommandHandler(CommandHandler):
    def __init__(self, simplified_bill_repository: SimplifiedBillRepository):
        self.__simplified_bill_repository = simplified_bill_repository

    def execute(self, command: GenerateSimplifiedBillCommand) -> None:
        print(command)
