class UserLogin:
    def __init__(self, user_id: str):
        print("UserLogin ",user_id, type(user_id))
        self.__user_id = user_id

    def is_authenticated(self):
        print("is_authenticated")
        return True

    def is_active(self):
        print("is_active")
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.__user_id  # обязательно str
