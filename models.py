from pydantic import BaseModel


class Users_Model(BaseModel):
    user_Fname : str
    user_Lname : str
    user_Email : str
    realestate_Ids : list | None = []
    hashed_password : str

class Ammenities(BaseModel):
    rooms : str
    bathrooms : str
    balconys : str
   
class Realestate_Model(BaseModel):
    realestate_name : str
    realesatate_location : str
    realesatate_address : str
    realesatate_price : int
    realesatate_ammenities : Ammenities
    realesatate_images_ids : list | None = []

 