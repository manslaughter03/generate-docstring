"""
Username module
"""
import typing


class Bidule:
    """

    Bidule class

    Args:
        label (str): TODO: to complete
        data (typing.Dict[str, int]): TODO: to complete
        override (bool): TODO: to complete

    Attributes:
        data (typing.Dict): TODO: to complete
        idx (int): TODO: to complete

    """
    data: typing.Dict
    idx: int

    def __init__(self, label: str, data: typing.Dict[str, int], override: bool=True):
        """

        __init__ function

        Args:
            label (str): TODO: to complete
            data (typing.Dict[str, int]): TODO: to complete
            override (bool): TODO: to complete

        """
        self.label = label
        self.data = data
        self.override = override

    async def run(self, data: typing.Dict[str, str]) -> typing.Dict:
        """

        run function

        Args:
            data (typing.Dict[str, str]): TODO: to complete

        Returns:
            typing.Dict: TODO: to complete

        """
        return {"aa": "aa"}

    def __repr__(self):
        """

        __repr__ function

        """
        return f"<data: {data} idx: {idx}>"
