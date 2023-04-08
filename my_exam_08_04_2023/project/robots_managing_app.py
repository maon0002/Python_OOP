from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot,
                         "FemaleRobot": FemaleRobot, }
    VALID_SERVICE_TYPES = {"MainService": MainService,
                           "SecondaryService": SecondaryService, }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in RobotsManagingApp.VALID_SERVICE_TYPES.keys():
            raise Exception("Invalid service type!")
        self.services.append(RobotsManagingApp.VALID_SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in RobotsManagingApp.VALID_ROBOT_TYPES.keys():
            raise Exception("Invalid robot type!")
        self.robots.append(RobotsManagingApp.VALID_ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService") or \
                (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService"):
            return "Unsuitable service."

        if len(service.robots) >= service.SERVICE_CAPACITY:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in service.robots if r.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")
        self.robots.append(robot[0])
        service.robots.remove(robot[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        for r in service.robots:
            r.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        # it can be in separate func because of the repetition
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
#
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
