from bookstore_billing import settings
from bookstore_billing.infrastructure.event_buses import EventBusConsumerFactory
from bookstore_billing.infrastructure.event_buses.kafka import KafkaEventBusConsumer


class KafkaEventBusConsumerFactory(EventBusConsumerFactory):
    def __init__(self, consumer_group_id: str, topic_name: str):
        self.__consumer_group_id = consumer_group_id
        self.__topic_name = topic_name

    def build(self) -> KafkaEventBusConsumer:
        return KafkaEventBusConsumer(logger=settings.logger, consumer_group_id=self.__consumer_group_id,
                                     topic_name=self.__topic_name)
