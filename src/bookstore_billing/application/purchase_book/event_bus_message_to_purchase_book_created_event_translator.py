from bookstore_billing.application.event_bus.event_bus_message import EventBusMessage
from bookstore_billing.application.message_to_event_translator import (
    MessageToEventTranslator,
)
from bookstore_billing.application.purchase_book.purchase_created_event import (
    PurchaseCreatedEvent,
)


class EventBusMessageToPurchaseBookCreatedEventTranslator(MessageToEventTranslator):
    def translate(self, message: EventBusMessage) -> PurchaseCreatedEvent:
        return PurchaseCreatedEvent.reconstruct(
            event_id=message.event_id,
            created_at=message.created_at,
            payload=message.payload,
        )
