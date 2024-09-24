from dataclasses import dataclass


@dataclass
class DataRequest:
    id: int
    name: str

@dataclass
class DataResponse:
    id: int
    name: str


