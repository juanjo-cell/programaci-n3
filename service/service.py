from model.abb_avl import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.abb = ABB()

    def add_pet(self, pet: Pet):
        if self.exists(pet.id):
            return {"error": "Pet ID already exists"}
        self.abb.add(pet)
        return {"message": f"Pet {pet.name} added successfully!"}

    def remove_pet(self, pet_id: int):
        if not self.exists(pet_id):
            return {"error": "Pet not found"}
        self.abb.remove(pet_id)
        return {"message": "Pet deleted successfully"}

    def update_pet(self, pet_id: int, updated_pet: Pet):
        if not self.exists(pet_id):
            return {"error": "Pet not found"}
        self.abb.update(pet_id, updated_pet)
        return {"message": "Pet updated successfully"}

    def get_pets_by_breed(self, breed: str):
        pets = self.abb.get_by_breed(breed)
        if not pets:
            return {"error": "No pets found for this breed"}
        return {"pets": pets}

    def exists(self, pet_id: int) -> bool:
        return self.abb.root and self._exists(self.abb.root, pet_id)

    def _exists(self, node, pet_id: int) -> bool:
        if node is None:
            return False
        if node.pet.id == pet_id:
            return True
        elif pet_id < node.pet.id:
            return self._exists(node.left, pet_id)
        else:
            return self._exists(node.right, pet_id)


