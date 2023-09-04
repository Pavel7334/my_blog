from fastapi import FastAPI

from app.users.routers import router as router_users

app = FastAPI()


@app.get("/my_blog")
def get_my_blog():
    return "Блог Игонина Павла Владимировича"


app.include_router(router_users)