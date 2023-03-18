from flask import Blueprint

from bookstore_billing.application.purchase_book.event_bus_message_to_purchase_book_created_event_translator import (
    EventBusMessageToPurchaseBookCreatedEventTranslator,
)
from bookstore_billing.application.purchase_book.purchase_created_event import (
    PurchaseCreatedEvent,
)
from bookstore_billing.infrastructure.event_buses.kafka.kafka_event_bus_consumer_factory import (
    KafkaEventBusConsumerFactory,
)
from bookstore_billing.infrastructure.purchase_book.kafka_purchase_book_created_subscriber import (
    KafkaPurchaseBookCreatedSubscriber,
)
from bookstore_billing.settings import logger

cli_commands = Blueprint(name="cli", import_name="cli")


@cli_commands.route("/test")
def load_test():
    subscriber = KafkaPurchaseBookCreatedSubscriber(
        logger=logger,
        message_to_event_translator=EventBusMessageToPurchaseBookCreatedEventTranslator(),
        event_bus_consumer_factory=KafkaEventBusConsumerFactory(
            consumer_group_id="subscriber.purchase.purchase_book.on_purchase_created",
            topic_name="event.purchase.purchase_book.purchase_created",
        ),
    )
    subscriber.consume()
