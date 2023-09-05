from fastapi import APIRouter

from app.exceptions import UserAlreadyExistsException
from app.users.dao import UserDAO
from app.users.schemas import SUser

router = APIRouter(
    prefix="/auth",
    tags=["Пользователи"]
)


@router.post("/create")
async def create_user(user_data: SUser):
    existing_user = await UserDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        raise UserAlreadyExistsException
    await UserDAO.add(username=user_data.username, is_admin=user_data.is_admin)

