from logging import Logger

from bookstore_billing.application.event_subscriber import EventSubscriber
from bookstore_billing.infrastructure.event_buses.consumer_error_exception import (
    ConsumerErrorException,
)
from bookstore_billing.infrastructure.event_buses.kafka.kafka_event_bus_consumer_factory import (
    KafkaEventBusConsumerFactory,
)
from bookstore_billing.application.purchase_book.event_bus_message_to_purchase_book_created_event_translator import (
    EventBusMessageToPurchaseBookCreatedEventTranslator,
)


class KafkaPurchaseBookCreatedSubscriber(EventSubscriber):
    def __init__(
        self,
        logger: Logger,
        message_to_event_translator: EventBusMessageToPurchaseBookCreatedEventTranslator,
        event_bus_consumer_factory: KafkaEventBusConsumerFactory,
    ):
        super().__init__(
            logger=logger,
            message_to_event_translator=message_to_event_translator,
            event_bus_consumer_factory=event_bus_consumer_factory,
        )

    def consume(self) -> None:
        while True:
            try:
                for event in super().consume():
                    print(event)
                    # activate use case, save purchase or create billing or smth
            except ConsumerErrorException as e:
                self._logger.error(e)
                pass
            except Exception as e:
                self._logger.error(e)
                self._logger.warning(
                    f"Stopping {self.unique_identifier} due to unexpected error"
                )
                break
