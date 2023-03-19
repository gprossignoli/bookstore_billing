from bookstore_billing.application.command import Command

from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command import \
	GenerateSimplifiedBillCommand
from bookstore_billing.application.generate_simplified_bill.generate_simplified_bill_command_handler import \
	GenerateSimplifiedBillCommandHandler
from bookstore_billing.infrastructure.repositories.sqlalchemy_simplified_bill_repository import \
	SqlAlchemySimplifiedBillRepository
from bookstore_billing.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository


class CommandExecutor:
	__mapper = {
		GenerateSimplifiedBillCommand.fqn(): GenerateSimplifiedBillCommandHandler(simplified_bill_repository=SqlAlchemySimplifiedBillRepository(), user_repository=SqlAlchemyUserRepository()),
	}

	def execute(self, command: Command) -> None:
		self.__mapper.get(command.fqn()).execute(command=command)
