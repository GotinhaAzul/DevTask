import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)


class logs:
    '''Então, isso aqui é basicamente obsoleto. Mas, que surpresa, ela faz logs.'''
    def process(self, message):
        logger.debug(f"{message}")
    def action(self, message):
        logger.info(f"{message}")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time

        logging.info(f"{request.method} {request.url.path} Completado em {process_time:.4f}s")
        return response
