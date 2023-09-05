from fastapi import FastAPI

from app.users.router import router as router_user
from app.blogs.router import router as router_blog

app = FastAPI()


@app.get("/my_blog")
def get_my_blog():
    return "Блог Игонина Павла Владимировича"


app.include_router(router_user)
app.include_router(router_blog)
