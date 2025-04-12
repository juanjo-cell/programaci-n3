from model.pet import Pet
from service.service import ABBService
from fastapi import APIRouter, HTTPException

abb_service = ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    if abb_service.abb.root:
        return {"pets": abb_service.abb.root}
    return {"message": "No pets found"}

@abb_route.post("/")
async def create_pet(pet: Pet):
    if is_id_duplicate(pet.id):
        raise HTTPException(status_code=400, detail="Pet ID already exists")
    abb_service.abb.add(pet)
    return {"message": f"Pet {pet.name} added successfully!"}

@abb_route.delete("/{pet_id}")
async def delete_pet(pet_id: int):
    if not abb_service.abb.remove(pet_id):
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted successfully"}

@abb_route.put("/{pet_id}")
async def update_pet(pet_id: int, updated_pet: Pet):
    if not abb_service.abb.update(pet_id, updated_pet):
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet updated successfully"}

@abb_route.get("/breed/{breed}")
async def get_pets_by_breed(breed: str):
    pets = abb_service.abb.get_by_breed(breed)
    if not pets:
        raise HTTPException(status_code=404, detail="No pets found for this breed")
    return {"pets": pets}


def is_id_duplicate(pet_id: int) -> bool:
    return abb_service.abb.exists(pet_id)