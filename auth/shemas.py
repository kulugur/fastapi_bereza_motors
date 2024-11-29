from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    phone: str


class UserUpdate(schemas.BaseUserUpdate):
    pass