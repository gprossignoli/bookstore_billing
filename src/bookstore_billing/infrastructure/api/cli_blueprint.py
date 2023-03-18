from flask import Blueprint

from bookstore_billing.infrastructure.event_buses.kafka.kafka_event_bus_consumer_factory import \
    KafkaEventBusConsumerFactory

cli_commands = Blueprint(name="cli", import_name="cli")


@cli_commands.route("/test")
def load_test():
    consumer = KafkaEventBusConsumerFactory(consumer_group_id="test_group",
                                            topic_name="event.purchase.purchase_book.purchase_created").build()

    while True:
        msg = consumer.consume()
        print("eeh")
