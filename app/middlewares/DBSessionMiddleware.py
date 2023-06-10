from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.database import SessionLocal


class DBSessionMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        session = SessionLocal()
        request.state.db = session
        response = await call_next(request)
        session.close()

        return response
