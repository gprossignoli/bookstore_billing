from abc import ABC, abstractmethod

from bookstore_billing.application.event_bus import EventBusConsumer


class EventBusConsumerFactory(ABC):
    @abstractmethod
    def build(self) -> EventBusConsumer:
        pass
