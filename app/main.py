from fastapi import FastAPI

from app.users.router import router as router_users
from app.blogs.router import router as router_blogs

app = FastAPI()


@app.get("/my_blog")
def get_my_blog():
    return "Блог Игонина Павла Владимировича"


app.include_router(router_users)
app.include_router(router_blogs)