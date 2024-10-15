class Logins:
    def __init__(self) -> None:
        self.admins = {"Admin": "democracy"}
        self.customers = {}

    def __str__(self):
        return f"Hello, {self.username}"

    def sign_in(self, username: str, password: str, password_repeat: str) -> None:
        if password_repeat != password:
            print("Passwords don't match.")
        elif username in self.admins or username in self.customers:
            print("Username already taken.")
        else:
            self.customers[username] = password  # Add new user to customers dictionary
            print(f"User '{username}' has been successfully registered!")

    def log_in(self, username: str, password: str) -> str:
        if username in self.admins and self.admins[username] == password:
            print(f"Hello Admin {username}, you are logged in!")
            return "admin"
        elif username in self.customers and self.customers[username] == password:
            print(f"Hello {username}, you are logged in!")
            return "user"
        else:
            print("Login failed. Incorrect username or password.")
            return "failed"
