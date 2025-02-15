
from fastapi import APIRouter , Body
from schema import  Contact 
router = APIRouter()    

@router.get("/")
def root():
    return "Hello World"


@router.put("/contact/{contact_id}")
def read_path(contact: Contact =Body()):
    return {**contact.dict()}

@router.post("/contact")
def create_contact(contact: Contact =Body()):
    return {**contact.dict()}

@router.delete("/contact/{contact_id}")
def delete_contact(contact_id):
    return {"contact_id":contact_id , "status":"deleted"}

