from model.abb_avl import ABB
from model.pet import Pet
from typing import Optional

class ABBService:
    def __init__(self):
        self.abb = ABB()

    def add_pet(self, pet: Pet) -> dict:
        if self.abb.exists(pet.id):
            return {"error": "Pet ID already exists"}
        self.abb.add(pet)
        return {"message": f"Pet '{pet.name}' added successfully!"}

    def remove_pet(self, pet_id: int) -> dict:
        if not self.abb.exists(pet_id):
            return {"error": "Pet not found"}
        self.abb.remove(pet_id)
        return {"message": "Pet deleted successfully"}

    def update_pet(self, pet_id: int, updated_pet: Pet) -> dict:
        if not self.abb.exists(pet_id):
            return {"error": "Pet not found"}
        self.abb.update(pet_id, updated_pet)
        return {"message": "Pet updated successfully"}

    def get_pet_by_id(self, pet_id: int) -> Optional[Pet]:
        return self.abb.get_pet_by_id(pet_id)

    def get_pets_by_breed(self, breed: str) -> dict:
        pets = self.abb.get_by_breed(breed)
        if not pets:
            return {"error": "No se encontraron mascotas de esta raza"}
        return {"pets": pets}

    def get_all_inorder(self):
        return self.abb.inorder()

    def get_all_preorder(self):
        return self.abb.preorder()

    def get_all_postorder(self):
        return self.abb.postorder()

