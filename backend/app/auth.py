from fastapi import APIRouter, HTTPException
from .database import users_collection
from .schemas import UserRegister, UserLogin
from .security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/api/v1/auth")


@router.post("/register")
async def register(user: UserRegister):

    existing = await users_collection.find_one({"email": user.email})

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)

    await users_collection.insert_one(user_dict)

    return {"message": "User registered"}


@router.post("/login")
async def login(data: UserLogin):

    user = await users_collection.find_one({"email": data.email})

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
