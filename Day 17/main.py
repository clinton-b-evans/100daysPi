class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        print(f"{username} successfully created")

user_1 = User("01","Clinton")
