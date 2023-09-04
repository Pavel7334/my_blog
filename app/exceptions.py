from fastapi import HTTPException, status


class BasesException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BasesException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с таким username уже существует"


class BlogsAlreadyExistException(BasesException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Блог с таким title уже существует"