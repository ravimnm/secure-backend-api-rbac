from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import router as auth_router
from .tasks import router as tasks_router

app = FastAPI(title="Backend Internship API")

# CORS settings
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "API Running"}