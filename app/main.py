from fastapi import FastAPI


app = FastAPI()


@app.get("/my_blog")
def get_my_blog():
    return "Блог Игонина Павла Владимировича"
