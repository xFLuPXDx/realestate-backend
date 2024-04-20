import secrets
import string
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import Realestate_Model
from config.db import realestate_collection ,  user_collection
from auth import TokenData, get_current_active_user
from schemas import get_realestates

realestateRouter = APIRouter()

@realestateRouter.post('/realestate/create')
async def create_realestate(realestate:Realestate_Model,current_user: Annotated[TokenData, Depends(get_current_active_user)]):
    realestate_new = dict(realestate)
    while True:
            code = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
            if not(realestate_collection.find_one({"realestate_Id" : code})):
                realestate_new["realestate_Id"] = code
                break

    realestate_collection.insert_one(realestate_new)

    user_collection.find_one_and_update({ 'user_Email' : current_user.user_Email} , {"$push" : {"realestate_Ids" : realestate_new["realestate_Id"]}})

    return realestate_new["realestate_Id"]
    



@realestateRouter.get('/realestate/fetch')
async def create_realestate(current_user: Annotated[TokenData, Depends(get_current_active_user)]):  
    
    real =  get_realestates(realestate_collection.find())
    
    reallist = list()
    dic = dict()

    for i in real :
        reallist.append(i)             
    
    dic.update({"count" : len(reallist) , "result" : reallist})
        
    return dic
