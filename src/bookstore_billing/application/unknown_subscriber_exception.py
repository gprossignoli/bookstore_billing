class UnknowSubscriberException(Exception):
    def __init__(self, event_unique_identifier: str):
        self.event_unique_identifier = event_unique_identifier
        self.message = f"There is no subscriber registered for the event: {self.event_unique_identifier}"
        super().__init__(self.message)
