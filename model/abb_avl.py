from model.pet import Pet

class ABB:
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if self.root is None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def remove(self, pet_id: int):
        self.root = self._remove(self.root, pet_id)

    def _remove(self, node, pet_id: int):
        if node is None:
            return None
        if pet_id < node.pet.id:
            node.left = self._remove(node.left, pet_id)
        elif pet_id > node.pet.id:
            node.right = self._remove(node.right, pet_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.pet = min_larger_node.pet
            node.right = self._remove(node.right, min_larger_node.pet.id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def update(self, pet_id: int, updated_pet: Pet):
        self._update(self.root, pet_id, updated_pet)

    def _update(self, node, pet_id: int, updated_pet: Pet):
        if node is None:
            return
        if pet_id == node.pet.id:
            node.pet = updated_pet
        elif pet_id < node.pet.id:
            self._update(node.left, pet_id, updated_pet)
        else:
            self._update(node.right, pet_id, updated_pet)

    def get_pet_by_id(self, pet_id: int):
        return self._get_pet_by_id(self.root, pet_id)

    def _get_pet_by_id(self, node, pet_id: int):
        if node is None:
            return None
        if pet_id == node.pet.id:
            return node.pet
        elif pet_id < node.pet.id:
            return self._get_pet_by_id(node.left, pet_id)
        else:
            return self._get_pet_by_id(node.right, pet_id)

    def get_by_breed(self, breed: str) -> list:
        result = []
        self._collect_by_breed(self.root, breed.lower(), result)
        return result

    def _collect_by_breed(self, node, breed: str, result: list):
        if node is not None:
            self._collect_by_breed(node.left, breed, result)
            if node.pet.breed.lower() == breed:
                result.append(node.pet)
            self._collect_by_breed(node.right, breed, result)

    def remove_by_age_and_gender(self, age: int, gender: str):
        pets_to_remove = []
        self._collect_by_age_and_gender(self.root, age, gender.lower(), pets_to_remove)
        for pet in pets_to_remove:
            self.remove(pet.id)
        return {"message": f"{len(pets_to_remove)} pet(s) removed."}

    def _collect_by_age_and_gender(self, node, age: int, gender: str, result: list):
        if node is not None:
            self._collect_by_age_and_gender(node.left, age, gender, result)
            if node.pet.age == age and node.pet.gender.lower() == gender:
                result.append(node.pet)
            self._collect_by_age_and_gender(node.right, age, gender, result)

    def inorder(self):
        return self.root.inorder() if self.root else []

    def preorder(self):
        return self.root.preorder() if self.root else []

    def postorder(self):
        return self.root.postorder() if self.root else []

    def exists(self, pet_id: int) -> bool:
        return self._exists(self.root, pet_id)

    def _exists(self, node, pet_id: int) -> bool:
        if node is None:
            return False
        if pet_id == node.pet.id:
            return True
        elif pet_id < node.pet.id:
            return self._exists(node.left, pet_id)
        else:
            return self._exists(node.right, pet_id)

    def count_breeds(self):
        count = {}
        self._count_breeds_recursive(self.root, count)
        return count

    def _count_breeds_recursive(self, node, count):
        if node is not None:
            breed = node.pet.breed.lower()
            count[breed] = count.get(breed, 0) + 1
            self._count_breeds_recursive(node.left, count)
            self._count_breeds_recursive(node.right, count)


class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet: Pet):
        if pet.id < self.pet.id:
            if self.left:
                self.left.add(pet)
            else:
                self.left = NodeABB(pet)
        else:
            if self.right:
                self.right.add(pet)
            else:
                self.right = NodeABB(pet)
        self.size += 1

    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.pet)
        if self.right:
            result += self.right.inorder()
        return result

    def preorder(self):
        result = [self.pet]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.pet)
        return result


class NodeAVL(NodeABB):
    def __init__(self, pet: Pet):
        super().__init__(pet)
        self.height = 1