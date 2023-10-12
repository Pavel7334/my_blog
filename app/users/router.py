from fastapi import APIRouter, Response, Depends

from app.exceptions import UserAlreadyExistsException, UserEmailAlreadyExistsException, \
    IncorrectEmailOrPasswordOrUsernameException
from app.users.authorization import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUser, SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_dat: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_dat.email, username=user_dat.username)
    if existing_user:
        raise UserEmailAlreadyExistsException
    hashed_password = get_password_hash(user_dat.password)
    await UserDAO.add(email=user_dat.email, hashed_password=hashed_password, username=user_dat.username)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password, user_data.username)
    if not user:
        raise IncorrectEmailOrPasswordOrUsernameException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("my_blog_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("my_blog_access_token")
    return f"Пользователь вышел из системы"


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/create")
async def create_user(user_data: SUser):
    existing_user = await UserDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        raise UserAlreadyExistsException
    await UserDAO.add(username=user_data.username, is_admin=user_data.is_admin)

