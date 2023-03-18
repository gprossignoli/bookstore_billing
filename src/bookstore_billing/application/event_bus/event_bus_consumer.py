from abc import ABC, abstractmethod

from bookstore_billing.application.event_bus.event_bus_message import EventBusMessage


class EventBusConsumer(ABC):
    @abstractmethod
    def consume(self) -> EventBusMessage:
        pass
