"""
Username module
"""
import json


class Username:
    """

    Username class

    Args:
        username (str): TODO: to complete
        password (str): TODO: to complete

    """
    def __init__(self, username: str, password: str):
        """

        __init__ function

        Args:
            username (str): TODO: to complete
            password (str): TODO: to complete

        """
        self.username = username
        self.password = password

    def json(self) -> str:
        """

        json function

        Returns:
            str: TODO: to complete

        """
        return json.dumps({'username': self.username, 'password': self.password})
