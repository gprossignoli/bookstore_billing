from typing import Type

from bookstore_billing.application.event_subscriber import EventSubscriber
from bookstore_billing.application.unknown_subscriber_exception import (
    UnknowSubscriberException,
)


class SToMapper:
    __mapper = {}

    @classmethod
    def get_event_subcriber(cls, event_unique_identifier: str) -> Type[EventSubscriber]:
        subscriber = cls.__mapper.get(event_unique_identifier)
        if subscriber is None:
            raise UnknowSubscriberException(event_unique_identifier)
        return subscriber

    @classmethod
    def register_subscriber(
        cls, event_unique_identifier: str, subscriber: Type[EventSubscriber]
    ) -> None:
        cls.__mapper[event_unique_identifier] = subscriber
