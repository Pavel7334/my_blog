from fastapi import FastAPI

from app.users.router import router as router_user
from app.blogs.router import router as router_blog
from app.posts.router import router as router_post
from app.comments.router import router as router_comment

app = FastAPI()


@app.get("/my_blog")
def get_my_blog():
    return "Блог Игонина Павла Владимировича"


app.include_router(router_user)
app.include_router(router_blog)
app.include_router(router_post)
app.include_router(router_comment)
