from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud 
from .schemas import Follower, Following
from core.models import db_helper
from core.models import User
from dependencies.authentication.fastapi_users import current_active_user


router = APIRouter(tags=["Profile"])


# Current user's followings, followers, creations and likes

@router.get("/me/likes", tags=["My profile"])
async def get_user_likes(user: User = Depends(current_active_user),
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_likes(session, user.id)


@router.get("/me/created_recipes", tags=["My profile"])
async def get_user_created_recipes(user: User = Depends(current_active_user),
                                   session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_created_recipes(session, user.id)


@router.get("/me/followings", response_model=list[Following], tags=["My profile"])
async def get_my_followings(user: User = Depends(current_active_user),
                            session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_followings(session, user.id)


@router.get("/me/followers", response_model=list[Follower], tags=["My profile"])
async def get_my_followers(user: User = Depends(current_active_user),
                           session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_followers(session, user.id)




# Other users

@router.get("/{user_id}/likes")
async def get_user_likes(user_id: int, 
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_likes(session, user_id)


@router.get("/{user_id}/created_recipes")
async def get_user_created_recipes(user_id: int,
                                   session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_created_recipes(session, user_id)


@router.post("/{user_id}/follow_user")
async def follow_user(user_id: int,
                      user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.follow_user(session, user, user_id)


@router.delete("/{User_id}/stop_following_user", status_code=status.HTTP_204_NO_CONTENT)
async def stop_following_user(user_id: int,
                              user: User = Depends(current_active_user),
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.stop_following_user(session, user, user_id)


@router.get("/{user_id}/followings", response_model=list[Following])
async def get_user_followings(user_id: int,
                              user: User = Depends(current_active_user),
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_followings(session, user_id)


@router.get("/{user_id}/followers", response_model=list[Follower])
async def get_user_followers(user_id: int,
                             user: User = Depends(current_active_user),
                             session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_user_followers(session, user_id)
