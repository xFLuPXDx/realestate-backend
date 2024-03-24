from typing import Annotated
from fastapi import APIRouter, Depends
from models import Realestate_Model
from config.db import realestate_collection
from auth import TokenData, get_current_active_user

realestateRouter = APIRouter()

@realestateRouter.post('/realestate/create')
async def create_realestate(realestate:Realestate_Model,current_user: Annotated[TokenData, Depends(get_current_active_user)]):
    realestate_collection.insert_one(dict(realestate))
    return True