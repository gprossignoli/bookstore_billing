class UserNotExistsException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.message = f"user with id: {user_id} does not exists"
        super().__init__(self.message)
