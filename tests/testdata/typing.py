import typing


class Bidule:
    data: typing.Dict
    idx: int

    def __init__(self, label: str, data: typing.Dict[str, int], override: bool=True):
        self.label = label
        self.data = data
        self.override = override

    async def run(self, data: typing.Dict[str, str]) -> typing.Dict:
        return {"aa": "aa"}

    def __repr__(self):
        return f"<data: {data} idx: {idx}>"
