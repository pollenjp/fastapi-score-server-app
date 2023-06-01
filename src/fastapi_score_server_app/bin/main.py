# Third Party Library
from fastapi import FastAPI

# Local Library
from ..handler.handler import define_error_handler
from ..handler.handler import define_handlers
from ..repository.memory_repository import MemoryRepository

repository = MemoryRepository()

app = FastAPI()

define_error_handler(app, repository)
define_handlers(app, repository)
