from abc import ABC, abstractmethod

from bookstore_billing.application.event_bus.event_bus_message import EventBusMessage
from bookstore_billing.domain import Event


class MessageToEventTranslator(ABC):
    @abstractmethod
    def translate(self, message: EventBusMessage) -> Event:
        pass
