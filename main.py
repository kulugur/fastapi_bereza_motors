from fastapi_users import  FastAPIUsers

from auth.auth import auth_backend
from auth.manager import get_user_manager 
from auth.shemas import UserRead, UserCreate, UserUpdate
from router import router as user_router

from fastapi import FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.cors import CORSMiddleware

from auth.database import create_db_and_tables, User


@asynccontextmanager
async def lifespan(app):
    print("sub startup")
    await create_db_and_tables()
    yield
    print("sub shutdown")



app = FastAPI(
    title="Bereza_Motors",
    lifespan=lifespan
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(user_router)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
current_active_user = fastapi_users.current_user(active=True)
current_user = fastapi_users.current_user()



@app.post("/protected-route")
def protected_route(user: User = Depends(current_user)):

    return f"Hello, {user.phone}"
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://next-bereza-motors-mflu-dmuxns32p-igors-projects-facaa7af.vercel.app/",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# origins = [
#     "http://127.0.0.1:3000",
#     "http://localhost:3000",
#     "https://10.214.145.197:0"
#     "https://10.214.145.197:80"
#     "https://10.214.145.197"
#     "http://10.214.145.197"
#     "https://next-bereza-motors-6spf-ld880cv4n-igors-projects-facaa7af.vercel.app/"
#     "https://next-bereza-motors-6spf-ld880cv4n-igors-projects-facaa7af.vercel.app"
#     "https://next-bereza-motors-6spf-ld880cv4n-igors-projects-facaa7af.vercel.app:80",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["OPTIONS", "HEAD", "GET", "POST"],
#     allow_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Headers", "Content-Type", "Authorization" ],
# )