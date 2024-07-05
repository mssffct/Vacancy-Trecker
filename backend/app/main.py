from fastapi import FastAPI

from routers import *
from database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    description="This application allows you to track statistics on various vacancies and job seekers",
    dependencies=[]
)


# Dependency
def get_db():
    #TODO fix db connection issue
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(results_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
