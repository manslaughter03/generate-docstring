"""
Username module
"""
import json

class Username:
    """

    Username class

    Attributes:
        username (str): TODO: to complete
        password (str): TODO: to complete

    """
    username: str
    password: str

    def json(self) -> str:
        """

        json function

        Returns:
            str: TODO: to complete

        """
        return json.dumps({'username': self.username, 'password': self.password})

class Scope:
    """

    Scope class

    """
    pass
