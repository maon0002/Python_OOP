from typing import List


class Vet:
    animals: List[str] = []
    space = 5

    def __init__(self, name: str):
        self.name: str = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if len(self.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"

        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"

        return f"{animal_name} not in the clinic"

    def info(self):
        space_left_in_clinic = Vet.space - len(self.animals)
        return f"{self.name} has {len(self.animals)} animals. {space_left_in_clinic} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())