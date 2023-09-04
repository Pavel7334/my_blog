from fastapi import APIRouter

from app.exceptions import UserAlreadyExistsException
from app.users.dao import UsersDAO
from app.users.schemas import SUser

router = APIRouter(
    prefix="/auth",
    tags=["Пользователи"]
)


@router.post("/create")
async def create_user(user_data: SUser):
    existing_user = await UsersDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        raise UserAlreadyExistsException
    await UsersDAO.add(username=user_data.username)

