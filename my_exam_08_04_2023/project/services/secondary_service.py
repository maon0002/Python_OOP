from project.services.base_service import BaseService


class SecondaryService(BaseService):
    SERVICE_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.SERVICE_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"

        result = [f"{self.name} Secondary Service:", "Robots: " + " ".join(r.name for r in self.robots)]
        # robots = "Robots: " + " ".join(r.name for r in self.robots)
        return "\n".join(result)
