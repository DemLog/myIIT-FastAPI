from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, account

api_router = APIRouter()
api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(account.router, tags=["Account"])
