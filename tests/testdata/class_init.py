import json


class Username:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def json(self) -> str:
        return json.dumps({'username': self.username, 'password': self.password})
