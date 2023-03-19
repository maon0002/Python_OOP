from abc import ABC, abstractmethod
import time


class Work(ABC):
    @abstractmethod
    def work(self):
        pass


class Eat(ABC):

    @abstractmethod
    def eat(self):
        pass


class Digest(ABC):

    @abstractmethod
    def digest(self):
        pass


class Develop(ABC):

    @abstractmethod
    def develop(self):
        pass


class Recharge(ABC):

    @abstractmethod
    def recharge(self):
        pass


class Worker(Work, Eat, Digest):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(1)

    def digest(self):
        print("I'm digesting....(69 secs)")
        time.sleep(2)


class SuperWorker(Work, Eat, Develop):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(1)

    def develop(self):
        print("Watching the last training for the next Python version ....(6 mins * 1.5 speedup)")
        time.sleep(2)


class Robot(Work, Recharge):

    def work(self):
        print("I'm a robot. I'm working....")

    def recharge(self):
        print("I'm Recharging now....")
        time.sleep(2)


class Manager(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def set_worker(self, worker):
        ...


class NastyManager(Manager):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Work), "`worker` must be of type {}".format(Work)

        self.worker = worker

    def manage(self):
        self.worker.work()

    def develop(self):
        self.worker.develop()


class GenerousManager(Manager):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Eat) or isinstance(worker, Recharge), "`worker` must be of type {}".format(Eat or Recharge)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()

    def recharge(self):
        self.worker.recharge()


mother_tereza = GenerousManager()
jeff_bezos = NastyManager()

mother_tereza.set_worker(Worker())
jeff_bezos.set_worker(Worker())
jeff_bezos.manage()
mother_tereza.lunch_break()

mother_tereza.set_worker(SuperWorker())
jeff_bezos.set_worker(SuperWorker())
jeff_bezos.manage()
mother_tereza.lunch_break()
jeff_bezos.develop()

jeff_bezos.set_worker(Robot())
mother_tereza.set_worker(Robot())
jeff_bezos.manage()
mother_tereza.recharge()
