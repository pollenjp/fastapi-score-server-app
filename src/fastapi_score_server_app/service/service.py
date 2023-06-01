# Third Party Library
from pydantic import BaseModel

# Local Library
from ..repository.repository import BaseRepository
from ..repository.repository import ScoreDB
from ..repository.repository import ScoreToRegister


class Score(BaseModel):
    id: int
    username: str
    value: int


def convert_score_db_to_score(score_db: ScoreDB) -> Score:
    return Score(id=score_db.id, username=score_db.username, value=score_db.value)


def get_scores(repo: BaseRepository) -> list[Score]:
    return list(map(convert_score_db_to_score, repo.get_scores()))


def find_a_score(repo: BaseRepository, id: int) -> Score:
    return convert_score_db_to_score(repo.find_a_score(id))


def register_a_score(repo: BaseRepository, score: ScoreToRegister) -> Score:
    return convert_score_db_to_score(repo.register_score(score))
