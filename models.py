from pydantic import BaseModel


class Users_Model(BaseModel):
    user_Id : str
    user_Fname : str
    user_Lname : str
    user_Email : str
    realestate_Ids : list | None = []
    hashed_password : str

   
class Realestate_Model(BaseModel):
    realestate_Id : str
    realestate_price : str
    realestate_name : str
    realestate_location : str
    realestate_address : str
    realestate_area : str
    rooms : str
    bathrooms : str
    balconys : str
    realestate_images_ids : list | None = []
    seller_mobnum : str
    seller_email : str

 