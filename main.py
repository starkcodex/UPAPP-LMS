

from fastapi import FastAPI, Path, Query
from typing import Optional, List

from pydantic import BaseModel

app = FastAPI(
    title="UPSC LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "mcodex",
        "email": "marfleyTech@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/users')
async def create_user(user: User):
    users.append(user)
    return 'Success'


# url parameters and query params
@app.get('/users/{id}')
async def get_user(id: int = Path(..., description='the is of user available in db.', gt=2),
    q: str = Query(None, max_length=5)
    ):
    return { "user": users[id], "query":q }