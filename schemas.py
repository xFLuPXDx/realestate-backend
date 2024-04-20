def get_realestate(group) -> dict:
    return {
        "realestate_Id" : group["realestate_Id"],
        "realestate_name" : group["realestate_name"],
        "realestate_location" : group["realestate_location"],
        "realestate_address" : group["realestate_address"],
        "realestate_area" : group["realestate_area"],
        "rooms" : group["rooms"],
        "bathrooms" : group["bathrooms"],
        "balconys" : group["balconys"],
        "realestate_images_ids" : group["realestate_images_ids"]
    }

def get_realestates(realestates) -> list:
    return [
        get_realestate(realestate) for realestate in realestates
    ]