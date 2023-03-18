from abc import ABC, abstractmethod


class NonExecutives(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}"


class LazyWorker(NonExecutives):
    @staticmethod
    def work():
        print("I'm here, everything is on track!! Wanna smoke?")


class Worker(NonExecutives):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(NonExecutives):

    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, NonExecutives), f'`worker` must be of type {NonExecutives}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class ElonFckinMusk:

    @staticmethod
    def work():
        print("Let's meet in my office after 2 minutes!!!")


worker = Worker()
me = SuperWorker()
you = LazyWorker()
unknown_person = ElonFckinMusk()
manager = Manager()
manager.set_worker(worker)
manager.manage()
manager.set_worker(me)
manager.manage()
manager.set_worker(you)
manager.manage()

ambitious_desk_neighbour = SuperWorker()


try:
    manager.set_worker(worker)
    manager.set_worker(ambitious_desk_neighbour)
    manager.set_worker(me)
    manager.set_worker(you)
    manager.set_worker(unknown_person)
except AssertionError:
    print("manager fails to support himself....")
