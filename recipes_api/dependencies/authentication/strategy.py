from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy, AccessTokenDatabase

from core.config import settings

from .access_tokens import get_access_token_db

if TYPE_CHECKING:
    from core.models import AccessToken

def get_database_strategy(
    access_token_db: Annotated[AccessTokenDatabase["AccessToken"],Depends(get_access_token_db)]):
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.access_token.lifetime_seconds)

