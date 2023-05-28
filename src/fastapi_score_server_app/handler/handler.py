# Third Party Library
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

# Local Library
from .schema import Error
from .schema import ScoreRequest
from .schema import ScoreResponse
from .schema import ScoresResponse


class DefaultException(Exception):
    def __init__(self, status_code: int, error_code: int, message: str):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message


def define_error_handler(app: FastAPI) -> None:
    @app.exception_handler(DefaultException)
    async def unicorn_exception_handler(request: Request, exc: DefaultException) -> JSONResponse:
        error = Error(code=exc.error_code, message=exc.message)
        return JSONResponse(
            status_code=exc.status_code,
            content=error.dict(),
        )


def define_handlers(app: FastAPI) -> None:
    @app.get("/")
    async def root() -> dict[str, str]:
        return {"msg": "Hello World"}

    @app.get("/scores", response_model=ScoresResponse)
    async def get_scores() -> ScoresResponse:
        # TODO: replace later
        try:
            scores = ScoresResponse(__root__=[ScoreResponse(id=1, username="user1", value=100)])
        except Exception as e:
            raise DefaultException(status_code=500, error_code=1, message=str(e))
        return scores

    @app.post("/scores")
    async def post_scores(body: ScoreRequest) -> None:
        # TODO: 登録
        return None

    @app.get("/scores/{score_id}", response_model=ScoreResponse)
    async def get_a_score(score_id: int) -> ScoreResponse:
        # TODO: replace later
        score = ScoreResponse(id=1, username="user1", value=100)
        return score
