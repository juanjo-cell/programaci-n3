from model.pet import Pet
from service.service import ABBService
from fastapi import APIRouter, HTTPException, status

abb_service = ABBService()
abb_route = APIRouter(prefix="/abb", tags=["ABB"])

@abb_route.get("/inorder")
async def inorder():
    return {"pets": abb_service.get_all_inorder()}

@abb_route.get("/preorder")
async def preorder():
    return {"pets": abb_service.get_all_preorder()}

@abb_route.get("/postorder")
async def postorder():
    return {"pets": abb_service.get_all_postorder()}

@abb_route.get("/breed/{breed}")
async def get_pets_by_breed(breed: str):
    result = abb_service.get_pets_by_breed(breed)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

@abb_route.get("/")
async def get_all_pets():
    pets = abb_service.get_all_inorder()
    if not pets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No pets found")
    return {"pets": pets}

@abb_route.post("/", status_code=status.HTTP_201_CREATED)
async def create_pet(pet: Pet):
    result = abb_service.add_pet(pet)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return result

@abb_route.put("/{pet_id}")
async def update_pet(pet_id: int, updated_pet: Pet):
    result = abb_service.update_pet(pet_id, updated_pet)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

@abb_route.delete("/{pet_id}")
async def delete_pet(pet_id: int):
    result = abb_service.remove_pet(pet_id)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result["error"])
    return result

@abb_route.get("/{pet_id}")
async def get_pet_by_id(pet_id: int):
    pet = abb_service.get_pet_by_id(pet_id)
    if pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
    return {"pet": pet}
