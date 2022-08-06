'''
A simple scheduler class that will can be given
(date_time, task_to_do_at_date_time) as input and will
retrun a list of tasks that are due relative to local time.

Public methods are:
add_task(date: str, task: str) -> None
execute_due() -> list
run_tests() -> None

Use add_task(date, task) method with date in "Tue, 03 Aug 2021 10:45:08"
format


To do:
-could add code to schedule reoccuring
-could add code to change scheduled tasks time and task itself
'''


import heapq
import time
from collections import defaultdict


class Scheduler:
    def __init__(self):
        self.base_epoch = "Wed, 01 Jan 1970 01:00:00"
        self.queue = []
        heapq.heapify(self.queue)
        self.tasks = defaultdict(list)

    def add_task(self, date: str, task: str) -> None:
        date_secs = self._translate_time(date)
        heapq.heappush(self.queue, date_secs)
        self.tasks[date_secs].append(task)

    def execute_due(self) -> list:
        def helper() -> list:
            current_time = time.time()
            for_execusion = []
            while self.queue and current_time > self.queue[0]:
                date_secs = heapq.heappop(self.queue)
                tasks = self.tasks[date_secs]
                del self.tasks[date_secs]
                for_execusion = for_execusion + tasks
            return for_execusion
        return helper()

    def _translate_time(self, date: str) -> float:
        obj = time.strptime(date, "%a, %d %b %Y %H:%M:%S")
        return time.mktime(obj)

    def run_tests(self) -> None:
        print('running tests..')
        print(Scheduler1._translate_time(self.base_epoch) == 0)

        self.__init__()
        self.add_task(self.base_epoch, 'hello world again')
        self.add_task("Wed, 01 Jan 1970 01:00:01", 'wake up first time')
        self.add_task("Tue, 04 Aug 9999 06:10:00", 'coffee')
        self.add_task("Tue, 04 Aug 9999 07:00:00", 'shower')
        self.add_task("Tue, 04 Aug 9999 14:00:00", 'lunch')
        print(['hello world again', 'wake up first time'] ==
              self.execute_due())


# init class instance and run the tests
Scheduler1 = Scheduler()
Scheduler1.run_tests()
print()

# add some tasks and start excecuting what is due.
Scheduler1 = Scheduler()
base_epoch = "Wed, 01 Jan 1970 01:00:00"


Scheduler1.add_task(base_epoch, 'hello world')
# modify so that wake up til shower has past relative to local time and date
Scheduler1.add_task("Tue, 06 Aug 2022 06:00:00", 'wake up')
Scheduler1.add_task("Tue, 06 Aug 2022 06:10:00", 'coffee')
Scheduler1.add_task("Tue, 06 Aug 2022 07:00:00", 'shower')
# modify so that dinner is yet to happen relative to local time and date
Scheduler1.add_task("Tue, 06 Aug 2022 22:00:00", 'dinner')
print('Need to execute:', Scheduler1.execute_due())

# can run until queue is empty
until_empty = False
if until_empty:
    while Scheduler1.queue:
        Scheduler1.execute_due()
        time.sleep(1)
