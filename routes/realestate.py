from pathlib import Path
import secrets
import string
from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import Realestate_Model
from config.db import realestate_collection ,  user_collection
from auth import TokenData, get_current_active_user
from schemas import get_realestates
import magic

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

    return {"realestate_id" : realestate_new["realestate_Id"]}
    



@realestateRouter.get('/realestate/fetch')
async def create_realestate(current_user: Annotated[TokenData, Depends(get_current_active_user)]):  
    
    real =  get_realestates(realestate_collection.find())
    
    reallist = list()
    dic = dict()

    for i in real :
        reallist.append(i)             
    
    dic.update({"count" : len(reallist) , "result" : reallist})
        
    return dic


SUPPORTED_FILE_TYPES = {
    'image/png' : 'png',
    'image/jpeg' : 'jpeg',
    'image/jpg' : 'jpg'
}

tmp = "images/"

@realestateRouter.post('/resource/upload/{rid}')
async def upload_file(rid : str , file:UploadFile = File(...) ):

    try:
        contents = await file.read()

        file_type = magic.from_buffer(buffer=contents , mime=True)
        file.filename = f"{uuid.uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}"
        with open(f"{tmp}{file.filename}","wb") as f:
            f.write(contents)

        realestate_collection.find_one_and_update({"realestate_Id" : rid},{"$push" : { "realestate_images_ids" :  file.filename }})

        return {
        "uploaded" : 1
        }
     
    except:
        return {
        "uploaded" : 0
        }
    

@realestateRouter.get('/get_image/{iid}')
async def get_image(iid:str):
    print(iid)
    image_path = Path(f"images/{iid}")
    print(image_path)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)

@realestateRouter.get("/get_image_ids/{rid}")
async def get_image_ids(rid:str):
    return realestate_collection.find_one({"realestate_Id" : rid},{"_id":0,"realestate_images_ids" : 1})