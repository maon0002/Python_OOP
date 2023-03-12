from project.class_id_mixin import ClassIdMixin


class ExercisePlan(ClassIdMixin):
    id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(
            self):  # - returns the information about the plan in the following format: "Plan <{id}> with duration {duration} minutes"
        return f"Plan <{self.id}> with duration {self.duration} minutes"
