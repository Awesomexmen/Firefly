from swarm import Swarm
import sched, time

s = sched.scheduler(time.time, time.sleep)

swarm = Swarm(18, s)
swarm.begin_flashing(60, 1, 0.01)

import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(swarm.print_status, 0.05)
s.run()
