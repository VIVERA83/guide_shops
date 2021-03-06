class UserLogin:
    def __init__(self, user_id: str):
        self.__user_id = user_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.__user_id  # обязательно str
