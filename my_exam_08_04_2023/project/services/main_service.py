from project.services.base_service import BaseService


class MainService(BaseService):
    SERVICE_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.SERVICE_CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\nRobots: none"

        result = [f"{self.name} Main Service:", "Robots: " + " ".join(r.name for r in self.robots)]
        # robots = "Robots: " + " ".join(r.name for r in self.robots)
        return "\n".join(result)
