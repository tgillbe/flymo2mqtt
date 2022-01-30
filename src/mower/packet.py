from typing import List, Optional

class Parameter():
    name: str
    type: str

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

class Response():
    head: int
    head2: Optional[int]
    parameters: List[Parameter]

    def __init__(self, head: int, head2: Optional[int], parameters: Optional[List[Parameter]] = None):
        self.head = head
        self.head2 = head2
        self.parameters = parameters or []

class Request():
    head: int
    head2: Optional[int]
    parameters: List[Parameter]
    response: type

    def __init__(self, head: int, head2: Optional[int], response: type, parameters: Optional[List[Parameter]] = None):
        self.head = head
        self.head2 = head2
        self.response = response
        self.parameters = parameters or []
