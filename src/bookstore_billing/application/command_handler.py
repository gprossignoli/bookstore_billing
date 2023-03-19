from abc import ABC, abstractmethod

from bookstore_billing.application.command import Command


class CommandHandler(ABC):
	@abstractmethod
	def execute(self, command: Command) -> None:
		pass
