import json


class Username:
    username: str
    password: str

    def json(self) -> str:
        return json.dumps({'username': self.username, 'password': self.password})


class Scope:
    pass
