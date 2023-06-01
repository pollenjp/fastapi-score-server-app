# Third Party Library
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Local Library
from ..repository.repository import BaseRepository
from ..repository.repository import ScoreToRegister
from ..service import service
from .schema import Error
from .schema import ScoreRequest
from .schema import ScoreResponse
from .schema import ScoresResponse


class DefaultException(Exception):
    def __init__(self, status_code: int, error_code: int, message: str):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message


def define_error_handler(app: FastAPI, repo: BaseRepository) -> None:
    @app.exception_handler(DefaultException)
    async def default_exception_handler(request: Request, exc: DefaultException) -> JSONResponse:
        error = Error(code=exc.error_code, message=exc.message)
        return JSONResponse(
            status_code=exc.status_code,
            content=error.dict(),
        )


class EmptyResponse(BaseModel):
    pass


def define_handlers(app: FastAPI, repo: BaseRepository) -> None:
    @app.get("/")
    async def root() -> dict[str, str]:
        return {"msg": "Hello World"}

    @app.get("/scores", response_model=ScoresResponse)
    async def get_scores() -> ScoresResponse:
        try:
            scores = list(
                map(
                    lambda score: ScoreResponse(id=score.id, username=score.username, value=score.value),
                    service.get_scores(repo),
                )
            )
            scores_res = ScoresResponse(__root__=scores)
        except Exception as e:
            raise DefaultException(status_code=500, error_code=1, message=str(e))
        return scores_res

    @app.post("/scores", response_model=ScoreResponse)
    async def post_score(body: ScoreRequest) -> ScoreResponse:
        print("helo")
        try:
            score = service.register_a_score(repo, ScoreToRegister(username=body.username, value=body.value))
            score_res = ScoreResponse(id=score.id, username=score.username, value=score.value)
            return score_res
        except Exception as e:
            raise DefaultException(status_code=500, error_code=1, message=str(e))

    @app.get("/scores/{score_id}", response_model=ScoreResponse)
    async def get_a_score(score_id: int) -> ScoreResponse:
        try:
            score = service.find_a_score(repo, score_id)
            score_res = ScoreResponse(id=score.id, username=score.username, value=score.value)
        except Exception as e:
            raise DefaultException(status_code=500, error_code=1, message=str(e))
        return score_res
