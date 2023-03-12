from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:
        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"

        if price > self.__budget:
            return f"Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            curr_worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(curr_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        workers_expenses = sum(w.salary for w in self.workers)

        if workers_expenses > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_expenses
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        animals_expenses = sum(a.money_for_care for a in self.animals)

        if animals_expenses > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))
        animal_info = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]
        animal_info.extend(lions)

        animal_info.append(f"----- {len(tigers)} Tigers:")
        animal_info.extend(tigers)

        animal_info.append(f"----- {len(cheetahs)} Cheetahs:")
        animal_info.extend(cheetahs)

        return "\n".join(str(ai) for ai in animal_info)

    def workers_status(self) -> str:
        workers_info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [workers_info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(workers_info['Keeper'])} Keepers:",
            *workers_info['Keeper'],
            f"----- {len(workers_info['Caretaker'])} Caretakers:",
            *workers_info['Caretaker'],
            f"----- {len(workers_info['Vet'])} Vets:",
            *workers_info['Vet'],
        ]

        return "\n".join(result)

    # def workers_status(self) -> str:
    #     keepers = list(filter(lambda w: w.__class__.__name__ == "Keeper", self.workers))
    #     caretakers = list(filter(lambda w: w.__class__.__name__ == "Tiger", self.workers))
    #     vets = list(filter(lambda w: w.__class__.__name__ == "Cheetah", self.workers))
    #     workers_info = [
    #         f"You have {len(self.workers)} workers",
    #         f"----- {len(keepers)} Keepers:"
    #     ]
    #     workers_info.extend(keepers)
    #
    #     workers_info.append(f"----- {len(caretakers)} Caretakers:")
    #     workers_info.extend(caretakers)
    #
    #     workers_info.append(f"----- {len(vets)} Vets:")
    #     workers_info.extend(vets)
    #
    #     return "\n".join(str(wi) for wi in workers_info)