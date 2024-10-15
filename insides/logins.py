class Logins:
    def __init__(self) -> None:
        self.admins = {"Admin": "democracy"}
        self.custumers = {"user1": "password1", "user2": "password2"}

    def __str__(self):
        return f"Hello, {self.username}"
    
    def log_in(self, username: str, password: str) -> None:
        if username in self.admins and self.admins[username] == password:
            print(f"Hello Admin {username}, you are logged in!")
            return "admin"
        elif username in self.custumers and self.custumers[username] == password:
            print(f"Hello {username}, you are logged in!")
            return "user"
        else:
            print("Login failed. Incorrect username or password.")
            return "failed"