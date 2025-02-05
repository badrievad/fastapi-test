from typing import Annotated
from annotated_types import MinLen, MaxLen
from fastapi import Path
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Annotated[int, Path(gt=0)]
    name: Annotated[str, MinLen(3), MaxLen(50)]
    email: EmailStr
