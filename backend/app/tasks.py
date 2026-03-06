from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from datetime import datetime

from .database import tasks_collection
from .schemas import TaskCreate
from .security import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/api/v1/tasks")
security = HTTPBearer()


def get_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


@router.post("/")
async def create_task(task: TaskCreate, user=Depends(get_user)):

    data = task.dict()
    data["owner_id"] = user["user_id"]
    data["status"] = "pending"
    data["created_at"] = datetime.utcnow()

    result = await tasks_collection.insert_one(data)

    return {"task_id": str(result.inserted_id)}


@router.get("/")
async def get_tasks(user=Depends(get_user)):

    if user["role"] == "admin":
        tasks = await tasks_collection.find().to_list(100)

    else:
        tasks = await tasks_collection.find(
            {"owner_id": user["user_id"]}
        ).to_list(100)

    for t in tasks:
        t["_id"] = str(t["_id"])

    return tasks
