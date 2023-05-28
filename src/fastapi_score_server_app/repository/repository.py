# Standard Library
from abc import ABC
from abc import abstractmethod

# Third Party Library
from pydantic import BaseModel


class ScoreDB(BaseModel):
    id: int
    username: str
    value: int


class ScoreToRegister(BaseModel):
    username: str
    value: int


class BaseRepository(ABC):
    @abstractmethod
    def get_scores(self) -> list[ScoreDB]:
        raise NotImplementedError

    @abstractmethod
    def find_a_score(self, id: int) -> ScoreDB:
        raise NotImplementedError

    @abstractmethod
    def register_score(self, score: ScoreToRegister) -> ScoreDB:
        raise NotImplementedError
