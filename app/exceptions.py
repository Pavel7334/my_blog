from fastapi import HTTPException, status


class BasesException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserEmailAlreadyExistsException(BasesException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с таким email уже существует"


class UserAlreadyExistsException(BasesException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с таким username уже существует"


class BlogAlreadyExistException(BasesException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Блог с таким title уже существует"


class BlogDoesNotExistException(BasesException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого блога не существует"


class PostDoesNotExistException(BasesException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого поста не существует"


class CommentDoesNotExistException(BasesException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого коментария не существует"


class IncorrectEmailOrPasswordOrUsernameException(BasesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта, пароль или имя пользователя"


class TokenAbsentException(BasesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(BasesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"


class TokenExpiredException(BasesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Срок действия токена истек"


class UserIsNotPresentException(BasesException):
    status_code = status.HTTP_401_UNAUTHORIZED
