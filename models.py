import enum


class TodoType(enum.Enum):
    SHOPPING = 'SHOPPING'
    PERSONAL = 'PERSONAL'


class UserStatus(enum.Enum):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    INBLOCKED = 'INBLOCKED'


class UserRole(enum.Enum):
    SUPER_ADMIN = 'SUPER_ADMIN'
    USER = 'USER'
    ADMIN = 'ADMIN'


class User:
    def __init__(self,
                 username: str,
                 password: str,
                 user_id: int | None = None,
                 role: UserRole | None = None,
                 status: UserStatus | None = None,
                 login_try_count: int | None = None
                 ):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role or UserRole.USER.value
        self.status = status.INACTIVE.value
        self.login_try_count = login_try_count or 0

    def __repr__(self) -> str:
        return f'{self.id} - {self.username} - {self.role}'


class Todo:
    def __init__(self,
                 title: str,
                 user_id: int,
                 todo_id: int | None = None,
                 todo_type: TodoType | None = None,
                 ):
        self.id = todo_id
        self.title = title
        self.user_id = user_id
        self.todo_type = todo_type or TodoType.PERSONAL.value

    def __repr__(self) -> str:
        return f'{self.id} - {self.title} - {self.user_id}'

    class UserLogin:
        def __init__(self, username: str, password: str):
            self.username = username
            self.password = password

    class LoginService:
        def __init__(self):
            self.users = {}  # Dictionary to store usernames and passwords

        def register_user(self, user_login: UserLogin):
            # Method to register a user
            if user_login.username in self.users:
                raise ValueError("User already exists.")
            self.users[user_login.username] = user_login.password

        def login(self, user_login: UserLogin) -> User:
            # Method to perform user login
            if user_login.username not in self.users or self.users[user_login.username] != user_login.password:
                raise ValueError("Invalid username or password.")
            return User(user_login.username, user_login.password)

