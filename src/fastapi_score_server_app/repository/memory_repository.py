# Local Library
from .repository import BaseRepository
from .repository import ScoreDB
from .repository import ScoreToRegister


class MemoryRepository(BaseRepository):
    def __init__(self) -> None:
        self.store: dict[int, ScoreDB] = dict()

    def get_scores(self) -> list[ScoreDB]:
        return list(self.store.values())

    def find_a_score(self, id: int) -> ScoreDB:
        return self.store[id]

    def register_score(self, score: ScoreToRegister) -> ScoreDB:
        new_id = len(self.store) + 1
        new_score = ScoreDB(id=new_id, username=score.username, value=score.value)
        self.store[new_id] = new_score
        return new_score
