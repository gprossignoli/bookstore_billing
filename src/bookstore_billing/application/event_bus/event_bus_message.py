from dataclasses import dataclass


@dataclass(frozen=True)
class EventBusMessage:
    event_id: str
    created_at: str
    payload: dict
