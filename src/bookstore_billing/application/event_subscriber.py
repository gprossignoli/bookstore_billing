from abc import ABC, abstractmethod
from logging import Logger
from typing import Generator

from bookstore_billing.application.event_bus import (
    EventBusConsumerFactory,
    EventBusConsumer,
)
from bookstore_billing.application.message_to_event_translator import (
    MessageToEventTranslator,
)
from bookstore_billing.domain import Event


class EventSubscriber(ABC):
    def __init__(
        self,
        logger: Logger,
        event_bus_consumer_factory: EventBusConsumerFactory,
        message_to_event_translator: MessageToEventTranslator,
    ):
        self._logger = logger
        self._event_bus_consumer_factory = event_bus_consumer_factory
        self._message_to_event_translator = message_to_event_translator
        self.__event_consumer = None

    @abstractmethod
    def consume(self) -> Generator[Event, None, None]:
        event_bus_consumer = self._obtain_event_bus_consumer()

        while True:
            msg = event_bus_consumer.consume()
            event = self._message_to_event_translator.translate(msg)
            yield event

    def _obtain_event_bus_consumer(self) -> EventBusConsumer:
        if self.__event_consumer is None:
            self.__event_consumer = self._event_bus_consumer_factory.build()
        return self.__event_consumer
