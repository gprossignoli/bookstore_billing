from bookstore_billing.application.command import Command

from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command import \
	GenerateSimplifiedBillCommand
from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command_handler import \
	GenerateSimplifiedBillCommandHandler


class CommandExecutor:
	__mapper = {
		GenerateSimplifiedBillCommand.fqn(): GenerateSimplifiedBillCommandHandler(),
	}

	def execute(self, command: Command) -> None:
		self.__mapper.get(command.fqn()).execute(command=command)
