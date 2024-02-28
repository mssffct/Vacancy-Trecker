from fastapi import FastAPI

from app.routers import users, jobs, results

app = FastAPI(
    description="This application allows you to track statistics on various vacancies and job seekers",
    dependencies=[]
)

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(results.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
