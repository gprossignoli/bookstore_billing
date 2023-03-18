from abc import ABC, abstractmethod

from bookstore_billing.infrastructure.event_buses import EventBusConsumer


class EventBusConsumerFactory(ABC):
	@abstractmethod
	def build(self) -> EventBusConsumer:
		pass
