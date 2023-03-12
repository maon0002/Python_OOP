from typing import List

from project import exercise_plan
from project.class_id_mixin import ClassIdMixin
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym(ClassIdMixin):

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self,
                     customer: Customer):  # - add the customer in the customer list if the customer is not already in it
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self,
                    trainer: Trainer):  # - add the trainer to the trainers' list, if the trainer is not already in it
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self,
                      equipment: Equipment):  # - add the equipment to the equipment list, if the equipment is not already in it
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):  # - add the plan to the plans' list, if the plan is not already in it
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self,
                         subscription: Subscription):  # - add the subscription in the subscriptions list if the subscription is not already in it
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self,
                          subscription_id: int):  # - get the subscription, the customer, the trainer, the equipment, and the plan. Then return their string representations each on a new line.
        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = [x for x in self.customers if x.id == subscription.customer_id][0]
        trainer = [x for x in self.trainers if x.id == subscription.trainer_id][0]
        plan = [x for x in self.plans if x.id == subscription.exercise_id][0]
        equipment = [x for x in self.equipment if x.id == plan.equipment_id][0]

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

