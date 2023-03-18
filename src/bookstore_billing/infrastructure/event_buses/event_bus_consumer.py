from abc import ABC, abstractmethod


class EventBusConsumer(ABC):
	@abstractmethod
	def consume(self) -> None:
		pass
