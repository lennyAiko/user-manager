from typing import List
from models import User, Gender, Role
from uuid import UUID

db: List[User] = [
    User(
        id=UUID('aa03fa2d-a4fd-431d-a8de-6333a3059d6d'), 
        first_name="Lennox", 
        last_name="Charles",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID('0e5ae6de-8e13-41f5-bae7-927bdc719f9b'), 
        first_name="Hikmah", 
        last_name="Adunni",
        gender=Gender.female,
        roles=[Role.student]
    ),
]