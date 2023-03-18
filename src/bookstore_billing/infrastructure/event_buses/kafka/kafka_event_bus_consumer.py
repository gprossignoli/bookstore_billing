from logging import Logger
from typing import Tuple, Optional

from confluent_kafka import Message

from bookstore_billing.infrastructure.event_buses import EventBusConsumer
from bookstore_billing.infrastructure.event_buses.consumer_error_exception import ConsumerErrorException
from bookstore_billing.infrastructure.event_buses.kafka.kafka_consumer_factory import KafkaConsumerFactory


class KafkaEventBusConsumer(EventBusConsumer):
	def __init__(self, logger: Logger, consumer_group_id: str, topic_name: str):
		self.__logger = logger
		self.__topic_name = topic_name
		self.__kafka_consumer = KafkaConsumerFactory(consumer_group_id=consumer_group_id).build()
		self.__kafka_consumer.subscribe(topics=[self.__topic_name])

	def consume(self) -> Optional[Tuple[str, str]]:
		try:
			while True:
				msg: Message = self.__kafka_consumer.poll(timeout=1.0)
				if msg is None:
					pass
				elif msg.error():
					raise ConsumerErrorException(reason=msg.error().str())
				else:
					return msg.key().decode('utf-8'), msg.value().decode('utf-8')
		except Exception as e:
			self.__logger.error(e)
			self.__kafka_consumer.close()
