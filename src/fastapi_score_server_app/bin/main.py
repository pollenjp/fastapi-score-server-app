# Third Party Library
from fastapi import FastAPI

# Local Library
from ..handler.handler import define_error_handler
from ..handler.handler import define_handlers

app = FastAPI()

define_error_handler(app)
define_handlers(app)
